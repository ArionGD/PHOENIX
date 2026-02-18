from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Holding
from django.db.models import Sum, F

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
    }
    
    return render(request, 'portfolio/portfolio.html', context)
