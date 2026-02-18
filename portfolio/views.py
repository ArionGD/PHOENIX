from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Holding
import json
import requests
import re
from decimal import Decimal
from datetime import timedelta

# Curated list of specific assets with types
NSE_STOCKS = [
    {'symbol': 'RELIANCE', 'name': 'Reliance Industries Ltd.', 'type': 'stock'},
    {'symbol': 'SBIN', 'name': 'State Bank of India', 'type': 'stock'},
    {'symbol': 'MARUTI', 'name': 'Maruti Suzuki India Ltd.', 'type': 'stock'},
    {'symbol': 'GOLDBEES', 'name': 'Nippon India Gold BeES ETF', 'type': 'etf'},
    {'symbol': 'SILVERBEES', 'name': 'Nippon India Silver ETF', 'type': 'etf'},
]

CRYPTO_ASSETS = [
    {'symbol': 'BTC', 'name': 'Bitcoin', 'type': 'crypto', 'cg_id': 'bitcoin'},
    {'symbol': 'ETH', 'name': 'Ethereum', 'type': 'crypto', 'cg_id': 'ethereum'},
    {'symbol': 'DOGE', 'name': 'Dogecoin', 'type': 'crypto', 'cg_id': 'dogecoin'},
]

INDEX_FUNDS = [
    {'symbol': 'NIFTY_50', 'name': 'Nifty 50 Index', 'type': 'index'},
    {'symbol': 'NIFTY_NEXT_50', 'name': 'Nifty Next 50', 'type': 'index'},
    {'symbol': 'NIFTY_MIDCAP_150', 'name': 'Nifty Midcap 150', 'type': 'index'},
    {'symbol': 'NIFTY_SMALLCAP_250', 'name': 'Nifty Smallcap 250', 'type': 'index'},
]

MASTER_LIST = NSE_STOCKS + CRYPTO_ASSETS + INDEX_FUNDS

def get_live_price(symbol, asset_type='stock'):
    try:
        if asset_type == 'crypto':
            # Find the CoinGecko ID
            crypto = next((c for c in CRYPTO_ASSETS if c['symbol'] == symbol.upper()), None)
            cg_id = crypto['cg_id'] if crypto else symbol.lower()
            
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={cg_id}&vs_currencies=inr"
            r = requests.get(url, timeout=10)
            data = r.json()
            if cg_id in data:
                return Decimal(str(data[cg_id]['inr']))
            return None

        # Google Finance symbols for indices use INDEXNSE
        suffix = ":INDEXNSE" if asset_type == 'index' else ":NSE"
        url = f"https://www.google.com/finance/quote/{symbol}{suffix}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return None
            
        # Extract price using stable data-last-price attribute
        match = re.search(r'data-last-price="([\d\.]+)"', r.text)
        if match:
            return Decimal(str(match.group(1)))
            
        # Fallback to secondary price class if attribute not found
        fallback_match = re.search(r'class="YMlKec fxKbKc">₹?([\d,\.]+)<', r.text)
        if fallback_match:
            val = fallback_match.group(1).replace(',', '')
            return Decimal(val)
            
        return None
    except Exception as e:
        print(f"Scrape error for {symbol}: {e}")
        return None

@login_required
def portfolio_overview(request):
    holdings = Holding.objects.filter(user=request.user)
    
    # Auto-update prices ONLY if they are older than 5 minutes
    now = timezone.now()
    cooldown = timedelta(minutes=5)
    
    for holding in holdings:
        if not holding.current_price or (now - holding.last_updated) > cooldown:
            new_price = get_live_price(holding.symbol, holding.asset_type)
            if new_price:
                holding.current_price = new_price
                holding.save()

    # Separate holdings
    stock_holdings = holdings.filter(asset_type='stock')
    etf_holdings = holdings.filter(asset_type='etf')
    crypto_holdings = holdings.filter(asset_type='crypto')
    index_holdings = holdings.filter(asset_type='index')

    # Calculate totals
    total_market_value = sum(h.market_value() for h in holdings)
    total_cost = sum(h.total_cost() for h in holdings)
    total_profit_loss = total_market_value - total_cost
    
    if total_cost > 0:
        total_profit_loss_pct = (total_profit_loss / total_cost) * 100
    else:
        total_profit_loss_pct = 0
        
    context = {
        'stock_holdings': stock_holdings,
        'etf_holdings': etf_holdings,
        'crypto_holdings': crypto_holdings,
        'index_holdings': index_holdings,
        'total_market_value': total_market_value,
        'total_investment': total_cost,
        'total_profit_loss': total_profit_loss,
        'total_profit_loss_pct': total_profit_loss_pct,
        'master_list': MASTER_LIST,
        'master_list_json': json.dumps(MASTER_LIST),
    }
    
    return render(request, 'portfolio/portfolio.html', context)

@login_required
@require_POST
def add_asset(request):
    symbol = request.POST.get('symbol', '').upper().replace(".NS", "").replace(".BO", "")
    name = request.POST.get('name')
    quantity = request.POST.get('quantity')
    purchase_price = request.POST.get('purchase_price')
    purchase_date = request.POST.get('purchase_date')
    asset_type = request.POST.get('asset_type', 'stock')
    
    if not (symbol and quantity and purchase_price):
        return redirect('portfolio:overview')
        
    # Get direct live price
    curr_price = get_live_price(symbol, asset_type)
    if not curr_price:
        curr_price = Decimal(purchase_price) # Fallback to purchase price
    
    Holding.objects.create(
        user=request.user,
        symbol=symbol,
        name=name or symbol,
        quantity=quantity,
        purchase_price=purchase_price,
        current_price=curr_price,
        purchase_date=purchase_date if purchase_date else None,
        asset_type=asset_type
    )
    
    return redirect('portfolio:overview')

@login_required
@require_POST
def edit_asset(request, pk):
    holding = get_object_or_404(Holding, pk=pk, user=request.user)
    
    holding.symbol = request.POST.get('symbol', '').upper()
    holding.name = request.POST.get('name', holding.name)
    holding.quantity = request.POST.get('quantity')
    holding.purchase_price = request.POST.get('purchase_price')
    holding.purchase_date = request.POST.get('purchase_date') or None
    
    # Update current price as well since symbol might change
    curr_price = get_live_price(holding.symbol, holding.asset_type)
    if curr_price:
        holding.current_price = curr_price
        
    holding.save()
    return redirect('portfolio:overview')

@login_required
def delete_asset(request, pk):
    holding = get_object_or_404(Holding, pk=pk, user=request.user)
    holding.delete()
    return redirect('portfolio:overview')

@login_required
def manual_refresh(request):
    """Force refresh all prices regardless of cooldown."""
    holdings = Holding.objects.filter(user=request.user)
    for holding in holdings:
        new_price = get_live_price(holding.symbol, holding.asset_type)
        if new_price:
            holding.current_price = new_price
            holding.save()
    return redirect('portfolio:overview')

def search_stocks(request):
    q = request.GET.get('q', '').upper()
    results = [s for s in NSE_STOCKS if q in s['symbol'] or q in s['name'].upper()]
    return JsonResponse(results[:10], safe=False)
