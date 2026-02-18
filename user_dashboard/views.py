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
    total_profit_loss = total_market_value - total_cost
    
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
        # Yearly Timeline: Last 12 Months
        end_date = datetime.now().date()
        date_list = []
        for i in range(11, -1, -1):
            # First day of the month i months ago
            d = (end_date.replace(day=1) - timedelta(days=i*30)).replace(day=1)
            date_list.append(d)
        
        chart_labels = [d.strftime('%b') for d in date_list]
        
        stock_values = []
        etf_values = []
        crypto_values = []
        index_values = []
        
        for d in date_list:
            # Get the last day of that month for "closing" price
            if d.month == 12:
                last_day = d.replace(day=31)
            else:
                last_day = (d.replace(month=d.month+1, day=1) - timedelta(days=1))
            
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
    }
    
    return render(request, 'user_dashboard/user_db.html', context)
