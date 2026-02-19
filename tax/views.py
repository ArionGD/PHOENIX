from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portfolio.models import Holding
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta

@login_required
def tax_calculator(request):
    # Try to load previous data from session
    cached_report = request.session.get('last_tax_report', {})
    cached_results = cached_report.get('results', {})
    
    # Initialize from POST if available, otherwise from Session, otherwise default to 0
    salary_raw = request.POST.get('salary')
    if salary_raw is not None:
        salary = Decimal(salary_raw or '0')
    else:
        salary = Decimal(str(cached_results.get('salary', '0')))
        
    other_income_raw = request.POST.get('other_income')
    if other_income_raw is not None:
        other_income = Decimal(other_income_raw or '0')
    else:
        other_income = Decimal(str(cached_results.get('other_income', '0')))
        
    occupation_type = request.POST.get('occupation_type')
    if occupation_type is None:
        occupation_type = cached_results.get('occupation_type', 'salary')
    
    results = None
    asset_breakdown = []
    
    # Helper to convert session data back to displayable results if GET request
    if request.method == "GET" and cached_report:
        results = cached_report.get('results')
        asset_breakdown = cached_report.get('asset_breakdown', [])
    
    # Precise Asset Classification Engine (Always run to get latest holdings)
    holdings = Holding.objects.filter(user=request.user)
    
    total_equity_stcg = Decimal('0')
    total_equity_ltcg = Decimal('0')
    total_debt_income_gains = Decimal('0') # Taxed at slab
    total_debt_ltcg = Decimal('0') # Old debt funds
    total_crypto_gain = Decimal('0')
    
    now = timezone.now()
    one_year_ago = now - timedelta(days=365)
    two_years_ago = now - timedelta(days=730)
    april_2023 = timezone.make_aware(timezone.datetime(2023, 4, 1))

    # Market classification constants
    DEBT_GOLD_SYMBOLS = ['GOLDBEES', 'SILVERBEES', 'LIQUIDBEES', 'DEBT_ETF']
    
    # If it's a POST, we calculate everything fresh. 
    # If it's a GET, we only rebuild the asset_breakdown if we don't have it in session, 
    # but we ALWAYS recalculate it to show real-time market profits.
    
    temp_asset_breakdown = []
    for h in holdings:
        profit = h.profit_loss()
        mv = h.market_value()
        
        # Determine Purchase Date
        purchase_date = timezone.make_aware(timezone.datetime.combine(h.purchase_date, timezone.datetime.min.time())) if h.purchase_date else (h.created_at if hasattr(h, 'created_at') else None)
        
        # Rule 1: Crypto (VDA)
        if h.asset_type == 'crypto' or h.symbol.upper() in ['BTC', 'ETH', 'SOL', 'USDT']:
            if profit > 0: total_crypto_gain += profit
            temp_asset_breakdown.append({'symbol': h.symbol, 'profit': profit, 'market_value': mv, 'type': 'Crypto (VDA) 30%', 'tax_rate': Decimal('0.30')})

        # Rule 2: Debt / Gold ETF / Debt Mutual Funds
        elif h.symbol.upper() in DEBT_GOLD_SYMBOLS:
            if purchase_date and purchase_date >= april_2023:
                total_debt_income_gains += profit
                temp_asset_breakdown.append({'symbol': h.symbol, 'profit': profit, 'market_value': mv, 'type': 'Debt/Gold (Income Slab)', 'tax_rate': None})
            else:
                if purchase_date and purchase_date < two_years_ago:
                    total_debt_ltcg += profit
                    temp_asset_breakdown.append({'symbol': h.symbol, 'profit': profit, 'market_value': mv, 'type': 'Debt LTCG (12.5%)', 'tax_rate': Decimal('0.125')})
                else:
                    total_debt_income_gains += profit
                    temp_asset_breakdown.append({'symbol': h.symbol, 'profit': profit, 'market_value': mv, 'type': 'Debt STCG (Income Slab)', 'tax_rate': None})

        # Rule 3: Equity / Equity Mutual Funds / Stock
        else:
            if purchase_date and purchase_date < one_year_ago:
                total_equity_ltcg += profit
                temp_asset_breakdown.append({'symbol': h.symbol, 'profit': profit, 'market_value': mv, 'type': 'Equity LTCG (12.5%)', 'tax_rate': Decimal('0.125')})
            else:
                total_equity_stcg += profit
                temp_asset_breakdown.append({'symbol': h.symbol, 'profit': profit, 'market_value': mv, 'type': 'Equity STCG (20%)', 'tax_rate': Decimal('0.20')})

    # If it's a GET request, we use the recalculated asset breakdown
    if request.method == "GET":
        asset_breakdown = temp_asset_breakdown
        # We also need to calculate the "Receivable" and "Tax" for individual assets 
        # based on the cached marginal rate if available
        marginal_rate = Decimal(str(cached_results.get('marginal_rate', '0')))
        taxable_stcg = Decimal(str(cached_results.get('total_stcg', '0')))
        taxable_ltcg = Decimal(str(cached_results.get('total_ltcg', '0')))
        ltcg_tax = Decimal(str(cached_results.get('ltcg_tax', '0')))
        equity_stcg_tax = Decimal(str(cached_results.get('equity_stcg_tax', '0')))

        for asset in asset_breakdown:
            a_profit = asset['profit']
            a_mv = asset.get('market_value', Decimal('0'))
            tax_est = Decimal('0')
            if a_profit > 0:
                if asset.get('tax_rate') is not None:
                    if 'LTCG' in asset['type']:
                        if taxable_ltcg > 0:
                            original_ltcg_pool = total_equity_ltcg + total_debt_ltcg
                            if original_ltcg_pool > 0:
                                tax_est = (a_profit / original_ltcg_pool) * ltcg_tax
                    else:
                        if 'Crypto' in asset['type']:
                            tax_est = a_profit * asset['tax_rate']
                        else:
                            if taxable_stcg > 0:
                                tax_est = (a_profit / total_equity_stcg) * equity_stcg_tax if total_equity_stcg > 0 else Decimal('0')
                else:
                    tax_est = a_profit * marginal_rate
            tax_est = max(Decimal('0'), tax_est * Decimal('1.04'))
            asset['tax'] = tax_est
            asset['receivable'] = a_mv - tax_est
        asset_breakdown.sort(key=lambda x: x['type'])

    if request.method == "POST":
        asset_breakdown = temp_asset_breakdown
        std_deduction = Decimal('75000') if occupation_type == 'salary' else Decimal('0')
        total_slab_income = salary + other_income + max(Decimal('0'), total_debt_income_gains)
        taxable_income = max(Decimal('0'), total_slab_income - std_deduction)
        
        slabs = [(400000, 0.05), (400000, 0.10), (400000, 0.15), (400000, 0.20), (400000, 0.25), (float('inf'), 0.30)]
        income_tax = Decimal('0')
        temp_income = taxable_income - 400000
        marginal_rate = Decimal('0')
        if temp_income > 0:
            for limit, rate in slabs:
                chunk = min(temp_income, Decimal(str(limit)))
                income_tax += chunk * Decimal(str(rate))
                if chunk > 0: marginal_rate = Decimal(str(rate))
                temp_income -= chunk
                if temp_income <= 0: break
        
        if taxable_income <= 1200000:
            income_tax = Decimal('0')
            marginal_rate = Decimal('0')
            
        net_stcg = total_equity_stcg
        net_ltcg = total_equity_ltcg + total_debt_ltcg
        
        if net_stcg < 0 and net_ltcg > 0:
            set_off_amount = min(abs(net_stcg), net_ltcg)
            net_ltcg -= set_off_amount
        
        taxable_stcg = max(Decimal('0'), net_stcg)
        taxable_ltcg = max(Decimal('0'), net_ltcg)
        ltcg_after_exemption = max(Decimal('0'), taxable_ltcg - Decimal('125000'))
        ltcg_tax = ltcg_after_exemption * Decimal('0.125')
        equity_stcg_tax = taxable_stcg * Decimal('0.20')
        crypto_tax = total_crypto_gain * Decimal('0.30')
        
        total_tax_pre_cess = income_tax + ltcg_tax + equity_stcg_tax + crypto_tax
        cess = total_tax_pre_cess * Decimal('0.04') 
        final_liability = total_tax_pre_cess + cess
        effective_rate = (final_liability / total_slab_income * 100) if total_slab_income > 0 else Decimal('0')

        for asset in asset_breakdown:
            a_profit = asset['profit']
            a_mv = asset.get('market_value', Decimal('0'))
            tax_est = Decimal('0')
            if a_profit > 0:
                if asset.get('tax_rate') is not None:
                    if 'LTCG' in asset['type']:
                        if taxable_ltcg > 0:
                            original_ltcg_pool = total_equity_ltcg + total_debt_ltcg
                            if original_ltcg_pool > 0:
                                tax_est = (a_profit / original_ltcg_pool) * ltcg_tax
                    else: 
                        if 'Crypto' in asset['type']:
                            tax_est = a_profit * asset['tax_rate']
                        else:
                            if taxable_stcg > 0:
                                tax_est = (a_profit / total_equity_stcg) * equity_stcg_tax if total_equity_stcg > 0 else Decimal('0')
                else:
                    tax_est = a_profit * marginal_rate
            
            tax_est = max(Decimal('0'), tax_est * Decimal('1.04'))
            asset['tax'] = tax_est
            asset['net_profit'] = a_profit - tax_est
            asset['receivable'] = a_mv - tax_est

        asset_breakdown.sort(key=lambda x: x['type'])

        results = {
            'taxable_income': taxable_income,
            'income_tax': income_tax,
            'ltcg_tax': ltcg_tax,
            'equity_stcg_tax': equity_stcg_tax,
            'crypto_tax': crypto_tax,
            'cess': cess,
            'total_tax': final_liability,
            'effective_rate': effective_rate,
            'total_stcg': taxable_stcg,
            'total_ltcg': taxable_ltcg,
            'raw_stcg': total_equity_stcg,
            'abs_raw_stcg': abs(total_equity_stcg),
            'raw_ltcg': (total_equity_ltcg + total_debt_ltcg),
            'is_nil_tax_zone': taxable_income <= 1200000,
            'std_deduction': std_deduction,
            'occupation_type': occupation_type,
            'salary': salary,
            'other_income': other_income,
            'marginal_rate': marginal_rate,
        }

        def convert_to_float(v):
            if isinstance(v, Decimal): return float(v)
            if isinstance(v, list): return [convert_to_float(i) for i in v]
            if isinstance(v, dict): return {k: convert_to_float(val) for k, val in v.items()}
            return v

        session_results = convert_to_float(results)
        session_asset_breakdown = convert_to_float(asset_breakdown)
        
        request.session['last_tax_report'] = {
            'results': session_results,
            'asset_breakdown': session_asset_breakdown
        }
        
    return render(request, 'tax/tax.html', {
        'results': results,
        'salary': salary,
        'other_income': other_income,
        'occupation_type': occupation_type,
        'asset_breakdown': asset_breakdown
    })

@login_required
def tax_report(request):
    report_data = request.session.get('last_tax_report')
    if not report_data:
        return redirect('tax:calculator')
        
    return render(request, 'tax/report.html', {
        'results': report_data['results'],
        'asset_breakdown': report_data['asset_breakdown']
    })
