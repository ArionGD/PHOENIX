from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Transaction
from decimal import Decimal


@login_required
def transaction_list(request):
    """Show all transactions for the logged-in user."""
    txns = Transaction.objects.filter(user=request.user)

    # --- Summary stats ---
    total_invested = sum(t.total_value for t in txns if t.transaction_type == 'buy')
    total_sold     = sum(t.total_value for t in txns if t.transaction_type in ('sell', 'book_profit'))
    total_realized = sum(t.realized_pl for t in txns if t.realized_pl is not None)
    txn_count      = txns.count()

    # --- Filter by type ---
    filter_type = request.GET.get('type', 'all')
    if filter_type != 'all':
        txns = txns.filter(transaction_type=filter_type)

    context = {
        'transactions':    txns,
        'filter_type':     filter_type,
        'total_invested':  total_invested,
        'total_sold':      total_sold,
        'total_realized':  total_realized,
        'txn_count':       txn_count,
    }
    return render(request, 'transactions/transactions.html', context)
