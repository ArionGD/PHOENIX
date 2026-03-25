from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.cache import cache
from django.utils import timezone
from .models import Holding
from transactions.models import Transaction
import json
import requests
import re
from decimal import Decimal
from datetime import timedelta

# Curated list of specific assets with types
SHORTABLE_STOCKS = [
    {'symbol': 'NYKAA', 'name': 'FSN E-Commerce Ventures (Nykaa)', 'type': 'stock'},
    {'symbol': 'PAYTM', 'name': 'One 97 Communications (Paytm)', 'type': 'stock'},
    {'symbol': 'ETERNAL', 'name': 'Zomato Limited (Eternal)', 'type': 'stock'},
]

NSE_STOCKS = [
    {'symbol': 'RELIANCE', 'name': 'Reliance Industries Ltd.', 'type': 'stock'},
    {'symbol': 'SBIN', 'name': 'State Bank of India', 'type': 'stock'},
    {'symbol': 'MARUTI', 'name': 'Maruti Suzuki India Ltd.', 'type': 'stock'},
]

CRYPTO_ASSETS = [
    {'symbol': 'BTC', 'name': 'Bitcoin', 'type': 'crypto', 'cg_id': 'bitcoin'},
    {'symbol': 'ETH', 'name': 'Ethereum', 'type': 'crypto', 'cg_id': 'ethereum'},
    {'symbol': 'DOGE', 'name': 'Dogecoin', 'type': 'crypto', 'cg_id': 'dogecoin'},
]

ETF_ASSETS = [
    {'symbol': 'NIFTYBEES', 'name': 'Nippon India Nifty 50 ETF', 'type': 'etf'},
    {'symbol': 'GOLDBEES', 'name': 'Nippon India Gold ETF', 'type': 'etf'},
    {'symbol': 'MON100', 'name': 'Motilal Oswal NASDAQ 100 ETF', 'type': 'etf'},
    {'symbol': 'SILVERBEES', 'name': 'Nippon India Silver ETF', 'type': 'etf'},
]

INDEX_FUNDS = [
    {'symbol': 'NIFTY_50', 'name': 'Nifty 50 Index', 'type': 'index'},
    {'symbol': 'NIFTY_NEXT_50', 'name': 'Nifty Next 50', 'type': 'index'},
]

MASTER_LIST = NSE_STOCKS + CRYPTO_ASSETS + INDEX_FUNDS + ETF_ASSETS

def get_live_price(symbol, asset_type='stock'):
    try:
        # Special handling for shortable stocks in test
        if symbol.upper() in [s['symbol'] for s in SHORTABLE_STOCKS]:
            asset_type = 'stock' # Ensure they are treated as stocks

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
        
        # Zomato rebranded to Eternal, add fallback
        search_symbol = symbol.upper()
        if search_symbol == 'ZOMATO': search_symbol = 'ETERNAL'
        
        url = f"https://www.google.com/finance/quote/{search_symbol}{suffix}"
        
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
    # Try to get data from cache first for speed
    cache_key = f'portfolio_data_{request.user.id}'
    cached_data = cache.get(cache_key)
    
    if cached_data and 'refresh' not in request.GET:
        context = cached_data
    else:
        holdings = Holding.objects.filter(user=request.user)
        # Sort holdings
        stock_holdings = holdings.filter(asset_type='stock', position_type='long')
        short_holdings = holdings.filter(position_type='short')
        etf_holdings = holdings.filter(asset_type='etf')
        crypto_holdings = holdings.filter(asset_type='crypto')
        index_holdings = holdings.filter(asset_type='index')

        total_market_value = sum(h.market_value() for h in holdings)
        total_cost = sum(h.total_cost() for h in holdings)
        total_profit_loss = sum(h.profit_loss() for h in holdings)
        
        total_profit_loss_pct = (total_profit_loss / total_cost * 100) if total_cost > 0 else 0
            
        context = {
            'stock_holdings': stock_holdings,
            'short_holdings': short_holdings,
            'etf_holdings': etf_holdings,
            'crypto_holdings': crypto_holdings,
            'index_holdings': index_holdings,
            'total_market_value': total_market_value,
            'total_investment': total_cost,
            'total_profit_loss': total_profit_loss,
            'total_profit_loss_pct': total_profit_loss_pct,
            'master_list': MASTER_LIST,
            'shortable_stocks': SHORTABLE_STOCKS,
            'master_list_json': json.dumps(MASTER_LIST),
        }
        # Cache results for 5 minutes
        cache.set(cache_key, context, 300)
    
    return render(request, 'portfolio/portfolio.html', context)

@login_required
def get_live_price_json(request, pk):
    holding = get_object_or_404(Holding, pk=pk, user=request.user)
    new_price = get_live_price(holding.symbol, holding.asset_type)
    if new_price:
        holding.current_price = new_price
        holding.save()
        # Clear cache since data changed
        cache.delete(f'portfolio_data_{request.user.id}')
    
    # Render price with icon for HTMX
    return render(request, 'portfolio/partials/price_update.html', {'price': holding.current_price})

@login_required
def get_market_value_json(request, pk):
    holding = get_object_or_404(Holding, pk=pk, user=request.user)
    return render(request, 'portfolio/partials/market_value_update.html', {'value': holding.market_value()})

@login_required
@require_POST
def add_asset(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol', '').upper().replace(".NS", "").replace(".BO", "")
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        purchase_price = request.POST.get('purchase_price')
        purchase_date = request.POST.get('purchase_date')
        asset_type = request.POST.get('asset_type', 'stock')
        position_type = request.POST.get('position_type', 'long')
        use_market_price = request.POST.get('use_market_price') == 'true'
        
        if not (symbol and quantity):
            return redirect('portfolio:overview')
            
        curr_price = get_live_price(symbol, asset_type)
        if use_market_price or not purchase_price or purchase_price == '0':
            price = curr_price if curr_price else Decimal(str(purchase_price or 0))
        else:
            price = Decimal(str(purchase_price))
        
        if not curr_price: curr_price = price
        
        qty = Decimal(str(quantity))

        holding = Holding.objects.create(
            user=request.user, symbol=symbol, name=name or symbol,
            quantity=qty, purchase_price=price, current_price=curr_price,
            purchase_date=purchase_date if purchase_date else None,
            asset_type=asset_type, position_type=position_type
        )

        Transaction.objects.create(
            user=request.user, transaction_type='sell' if position_type == 'short' else 'buy',
            asset_type=asset_type, symbol=symbol, name=name or symbol,
            quantity=qty, price=price, total_value=qty * price,
        )

        # Clear cache
        cache.delete(f'portfolio_data_{request.user.id}')

        if request.headers.get('HX-Request'):
            # Fetch updated holdings
            holdings = Holding.objects.filter(user=request.user)
            
            if position_type == 'short':
                return render(request, 'portfolio/partials/short_rows.html', {'short_holdings': holdings.filter(position_type='short')})
                
            if asset_type == 'stock':
                return render(request, 'portfolio/partials/stock_rows.html', {'stock_holdings': holdings.filter(asset_type='stock', position_type='long')})
            
            # For ETFs, Crypto, Index - since they might not have specific partials in the user's current logic, 
            # I will ensure the page refreshes or we provide a more generic response.
            # Actually, looking at the template, there are loops for etf_holdings, etc.
            # I'll return a Trigger for a full page refresh if it's not a Stock/Short or 
            # I can just redirect which HTMX handles via HX-Redirect
            from django.http import HttpResponse
            response = HttpResponse("")
            response['HX-Redirect'] = request.build_absolute_uri()
            return response

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

@login_required
def book_profit(request, pk):
    """Render the Book Profit / Loss page for a specific holding."""
    holding = get_object_or_404(Holding, pk=pk, user=request.user)

    if request.method == 'POST':
        sell_price = Decimal(str(request.POST.get('sell_price', '0')))
        sell_qty   = Decimal(str(request.POST.get('sell_quantity', '0')))

        if sell_price > 0 and sell_qty > 0:
            realized = (sell_price - holding.purchase_price) * sell_qty

            # Log the Book Profit transaction
            Transaction.objects.create(
                user=request.user,
                transaction_type='book_profit',
                asset_type=holding.asset_type,
                symbol=holding.symbol,
                name=holding.name,
                quantity=sell_qty,
                price=sell_price,
                total_value=sell_qty * sell_price,
                realized_pl=realized,
                notes=f"Booked from holding #{holding.pk}",
            )

            # Reduce or delete the holding
            if sell_qty >= holding.quantity:
                holding.delete()
            else:
                holding.quantity -= sell_qty
                holding.save()

        return redirect('portfolio:overview')

    context = {'holding': holding}
    return render(request, 'portfolio/book_profit.html', context)
