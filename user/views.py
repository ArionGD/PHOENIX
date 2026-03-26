from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from portfolio.models import Holding
from decimal import Decimal

@login_required
def dashboard(request):
    period = request.GET.get('period', 'yearly')
    holdings = Holding.objects.filter(user=request.user)
    
    total_market_value = sum(h.market_value() for h in holdings)
    total_cost = sum(h.total_cost() for h in holdings)
    total_profit_loss = sum(h.profit_loss() for h in holdings) # Correctly sums Long + Short P/L
    
    if total_cost > 0:
        total_profit_loss_pct = (total_profit_loss / total_cost) * 100
    else:
        total_profit_loss_pct = 0
        
    import random
    from datetime import datetime, timedelta

    if period == 'monthly':
        # Generate 30-day timeline
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=29)
        date_list = [start_date + timedelta(days=x) for x in range(30)]
        chart_labels = [d.strftime('%d') for d in date_list]
        
        stock_values = []
        etf_values = []
        crypto_values = []
        index_values = []
        
        for d in date_list:
            day_stock_total = 0
            day_etf_total = 0
            day_crypto_total = 0
            day_index_total = 0
            
            for h in holdings:
                # If the stock was already owned on this day
                if h.purchase_date and h.purchase_date <= d:
                    # Calculate progress from buy date to today (0.0 to 1.0)
                    total_days = (end_date - h.purchase_date).days or 1
                    days_passed = (d - h.purchase_date).days
                    progress = days_passed / total_days
                    
                    # Interpolate price: linearly move from purchase to current price
                    # Add a small random jitter (±1.5%) for a "real" chart look
                    price_diff = float(h.current_price - h.purchase_price)
                    base_price = float(h.purchase_price) + (price_diff * progress)
                    jitter = base_price * (random.uniform(-0.015, 0.015))
                    daily_price = max(0, base_price + jitter)
                    
                    if h.position_type == 'short':
                        # Profit = Cost - Market Value
                        # Value to show on chart = Cost + (Cost - Simulated_MV)
                        val = float(h.total_cost()) + (float(h.total_cost()) - (daily_price * float(h.quantity)))
                    else:
                        val = daily_price * float(h.quantity)
                        
                    if h.asset_type == 'stock':
                        day_stock_total += val
                    elif h.asset_type == 'etf':
                        day_etf_total += val
                    elif h.asset_type == 'crypto':
                        day_crypto_total += val
                    else:
                        day_index_total += val
            
            stock_values.append(round(day_stock_total, 2))
            etf_values.append(round(day_etf_total, 2))
            crypto_values.append(round(day_crypto_total, 2))
            index_values.append(round(day_index_total, 2))
    else:
        # Yearly Timeline: Last 12 Months (Accurate)
        end_date = datetime.now().date()
        date_list = []
        
        current_date = end_date.replace(day=1)
        for _ in range(12):
            date_list.append(current_date)
            # Move to the first day of the PREVIOUS month
            if current_date.month == 1:
                current_date = current_date.replace(year=current_date.year-1, month=12)
            else:
                current_date = current_date.replace(month=current_date.month-1)
        
        # Reverse to get chronological order (past to present)
        date_list.reverse()
        chart_labels = [d.strftime('%b') for d in date_list]
        
        stock_values = []
        etf_values = []
        crypto_values = []
        index_values = []
        
        for d in date_list:
            # Safely find the last day of the month
            if d.month == 12:
                next_month = d.replace(year=d.year+1, month=1)
            else:
                next_month = d.replace(month=d.month+1)
            last_day = next_month - timedelta(days=1)
            
            # Don't simulate future months
            check_date = min(last_day, end_date)
            
            month_stock_total = 0
            month_etf_total = 0
            month_crypto_total = 0
            month_index_total = 0
            
            for h in holdings:
                if h.purchase_date and h.purchase_date <= check_date:
                    total_days = (end_date - h.purchase_date).days or 1
                    days_passed = (check_date - h.purchase_date).days
                    progress = days_passed / total_days
                    
                    price_diff = float(h.current_price - h.purchase_price)
                    base_price = float(h.purchase_price) + (price_diff * progress)
                    # Use slightly higher jitter for monthly points (±3%)
                    jitter = base_price * (random.uniform(-0.03, 0.03)) 
                    daily_price = max(0, base_price + jitter)
                    
                    if h.position_type == 'short':
                        # Profit = Cost - Market Value
                        # Value to show on chart = Cost + (Cost - Simulated_MV)
                        val = float(h.total_cost()) + (float(h.total_cost()) - (daily_price * float(h.quantity)))
                    else:
                        val = daily_price * float(h.quantity)
                        
                    if h.asset_type == 'stock':
                        month_stock_total += val
                    elif h.asset_type == 'etf':
                        month_etf_total += val
                    elif h.asset_type == 'crypto':
                        month_crypto_total += val
                    else:
                        month_index_total += val
            
            stock_values.append(round(month_stock_total, 2))
            etf_values.append(round(month_etf_total, 2))
            crypto_values.append(round(month_crypto_total, 2))
            index_values.append(round(month_index_total, 2))

    # Allocation for Doughnut Chart
    stock_total = sum(float(h.market_value()) for h in holdings.filter(asset_type='stock'))
    etf_total = sum(float(h.market_value()) for h in holdings.filter(asset_type='etf'))
    crypto_total = sum(float(h.market_value()) for h in holdings.filter(asset_type='crypto'))
    index_total = sum(float(h.market_value()) for h in holdings.filter(asset_type='index'))
    total_val = stock_total + etf_total + crypto_total + index_total
    
    distribution_data = [
        round((stock_total / total_val * 100), 1) if total_val > 0 else 0,
        round((etf_total / total_val * 100), 1) if total_val > 0 else 0,
        round((crypto_total / total_val * 100), 1) if total_val > 0 else 0,
        round((index_total / total_val * 100), 1) if total_val > 0 else 0
    ]

    import urllib.request
    import json
    from django.core.cache import cache
    
    mmi_value = cache.get('tickertape_mmi')
    if not mmi_value:
        try:
            req = urllib.request.Request('https://api.tickertape.in/mmi/now', headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=3)
            data = json.loads(res.read().decode('utf-8'))
            mmi_value = round(data['data']['currentValue'], 2)
            cache.set('tickertape_mmi', mmi_value, 600)
        except Exception:
            mmi_value = 50.0

    context = {
        'total_market_value': total_market_value,
        'total_investment': total_cost,
        'total_profit_loss': total_profit_loss,
        'total_profit_loss_pct': total_profit_loss_pct,
        'holdings_count': holdings.count(),
        'top_holdings': holdings[:5],
        'chart_labels': chart_labels,
        'stock_values': stock_values,
        'etf_values': etf_values,
        'crypto_values': crypto_values,
        'index_values': index_values,
        'active_period': period,
        'distribution_data': distribution_data,
        'user_salary': request.user.salary_income,
        'user_extra': request.user.other_income,
        'user_savings': request.user.monthly_savings,
        'user_expenses': request.user.expenses_json,
        'mmi_value': mmi_value,
    }
    
    return render(request, 'user/user_db.html', context)

import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
@require_POST
def update_budget(request):
    try:
        data = json.loads(request.body)
        user = request.user
        user.salary_income = Decimal(str(data.get('salary', 0)))
        user.other_income = Decimal(str(data.get('extra', 0)))
        user.monthly_savings = Decimal(str(data.get('savings', 0)))
        user.expenses_json = json.dumps(data.get('expenses', []))
        user.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@login_required
def cagr_calculator(request):
    return render(request, 'user/cagr_calc.html')

@login_required
def cagr_target(request):
    return render(request, 'user/cagr_target.html')
