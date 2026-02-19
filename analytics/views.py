from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from portfolio.models import Holding
from decimal import Decimal
import json
import requests
import re

def get_nifty_50_price():
    """Fetch current Nifty 50 price for benchmarking."""
    url = "https://www.google.com/search?q=NSE:NIFTY+50"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        match = re.search(r'data-last-price="([\d\.]+)"', r.text)
        if match:
            return Decimal(str(match.group(1)).replace(',', ''))
    except:
        pass
    return Decimal('25819.35') # Fallback

@login_required
def analytics_overview(request):
    holdings = Holding.objects.filter(user=request.user)
    
    # 1. Asset Type Distribution
    type_data = {}
    for h in holdings:
        a_type = h.get_asset_type_display()
        mv = float(h.market_value())
        type_data[a_type] = type_data.get(a_type, 0) + mv
        
    # 2. Fund Amount Wise (Top Holdings)
    fund_data = {h.symbol: float(h.market_value()) for h in holdings}
    fund_data = dict(sorted(fund_data.items(), key=lambda x: x[1], reverse=True)[:6])
    
    # 3. Sector Distribution (Mapping)
    SECTOR_MAP = {
        'RELIANCE': 'Energy', 'TCS': 'IT', 'INFY': 'IT', 'HDFCBANK': 'Banking',
        'ICICIBANK': 'Banking', 'SBIN': 'Banking', 'MARUTI': 'Auto', 'TATAMOTORS': 'Auto',
        'GOLDBEES': 'Commodities', 'SILVERBEES': 'Commodities', 'BTC': 'Crypto',
        'ETH': 'Crypto', 'NIFTY_50': 'Index'
    }
    sector_data = {}
    for h in holdings:
        sector = SECTOR_MAP.get(h.symbol, 'Others')
        mv = float(h.market_value())
        sector_data[sector] = sector_data.get(sector, 0) + mv

    # 4. Benchmarking (Portfolio P/L % vs Nifty 50)
    total_cost = sum(h.total_cost() for h in holdings)
    total_mv = sum(h.market_value() for h in holdings)
    portfolio_pl_pct = float((total_mv - total_cost) / total_cost * 100) if total_cost > 0 else 0
    
    # Nifty Benchmark (Assume a baseline for comparison, e.g., 5% return for context)
    nifty_return = 4.2  # Hardcoded or derived from real price delta if we had historical start
    
    context = {
        'type_labels': list(type_data.keys()),
        'type_values': list(type_data.values()),
        'fund_labels': list(fund_data.keys()),
        'fund_values': list(fund_data.values()),
        'sector_labels': list(sector_data.keys()),
        'sector_values': list(sector_data.values()),
        'portfolio_pl_pct': portfolio_pl_pct,
        'nifty_return': nifty_return,
        'total_mv': total_mv,
        'total_pl': total_mv - total_cost,
    }
    
    return render(request, 'analytics/detailed_analytics.html', context)
