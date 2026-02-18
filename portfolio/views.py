from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Holding
import json

# Simple mock list of NSE Stocks
NSE_STOCKS = [
    {'symbol': 'RELIANCE', 'name': 'Reliance Industries Ltd.'},
    {'symbol': 'TCS', 'name': 'Tata Consultancy Services Ltd.'},
    {'symbol': 'HDFCBANK', 'name': 'HDFC Bank Ltd.'},
    {'symbol': 'ICICIBANK', 'name': 'ICICI Bank Ltd.'},
    {'symbol': 'INFY', 'name': 'Infosys Ltd.'},
    {'symbol': 'SBIN', 'name': 'State Bank of India'},
    {'symbol': 'BHARTIARTL', 'name': 'Bharti Airtel Ltd.'},
    {'symbol': 'LICI', 'name': 'Life Insurance Corporation of India'},
    {'symbol': 'ITC', 'name': 'ITC Ltd.'},
    {'symbol': 'HINDUNILVR', 'name': 'Hindustan Unilever Ltd.'},
    {'symbol': 'LT', 'name': 'Larsen & Toubro Ltd.'},
    {'symbol': 'BAJFINANCE', 'name': 'Bajaj Finance Ltd.'},
    {'symbol': 'HCLTECH', 'name': 'HCL Technologies Ltd.'},
    {'symbol': 'MARUTI', 'name': 'Maruti Suzuki India Ltd.'},
    {'symbol': 'SUNPHARMA', 'name': 'Sun Pharmaceutical Industries Ltd.'},
    {'symbol': 'ADANIENT', 'name': 'Adani Enterprises Ltd.'},
    {'symbol': 'KOTAKBANK', 'name': 'Kotak Mahindra Bank Ltd.'},
    {'symbol': 'TITAN', 'name': 'Titan Company Ltd.'},
    {'symbol': 'ONGC', 'name': 'Oil & Natural Gas Corporation Ltd.'},
    {'symbol': 'TATASTEEL', 'name': 'Tata Steel Ltd.'},
]

@login_required
def portfolio_overview(request):
    holdings = Holding.objects.filter(user=request.user)
    
    # Calculate totals
    total_market_value = sum(h.market_value() for h in holdings)
    total_cost = sum(h.total_cost() for h in holdings)
    total_profit_loss = total_market_value - total_cost
    
    if total_cost > 0:
        total_profit_loss_pct = (total_profit_loss / total_cost) * 100
    else:
        total_profit_loss_pct = 0
        
    context = {
        'holdings': holdings,
        'total_market_value': total_market_value,
        'total_profit_loss': total_profit_loss,
        'total_profit_loss_pct': total_profit_loss_pct,
        'stocks': NSE_STOCKS, # For the dropdown/search
    }
    
    return render(request, 'portfolio/portfolio.html', context)

@login_required
@require_POST
def add_asset(request):
    symbol = request.POST.get('symbol')
    name = request.POST.get('name')
    quantity = request.POST.get('quantity')
    purchase_price = request.POST.get('purchase_price')
    purchase_date = request.POST.get('purchase_date')
    
    # Basic validation
    if not (symbol and quantity and purchase_price):
        return redirect('portfolio:overview')
        
    # In a real app, we'd fetch the actual name and current price from an API
    # For now, we'll use a default current price same as purchase or +5%
    curr_price = float(purchase_price) * 1.05 
    
    Holding.objects.create(
        user=request.user,
        symbol=symbol,
        name=name or symbol,
        quantity=quantity,
        purchase_price=purchase_price,
        current_price=curr_price,
        purchase_date=purchase_date if purchase_date else None,
        asset_type='stock' # Default to stock as requested
    )
    
    return redirect('portfolio:overview')

def search_stocks(request):
    q = request.GET.get('q', '').upper()
    results = [s for s in NSE_STOCKS if q in s['symbol'] or q in s['name'].upper()]
    return JsonResponse(results[:10], safe=False)
