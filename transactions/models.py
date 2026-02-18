from django.db import models
from django.conf import settings


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('buy',         'Buy'),
        ('sell',        'Sell'),
        ('book_profit', 'Book Profit/Loss'),
    )

    ASSET_TYPES = (
        ('stock',  'Stock'),
        ('etf',    'ETF'),
        ('crypto', 'Cryptocurrency'),
        ('index',  'Index Fund'),
    )

    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    asset_type      = models.CharField(max_length=10, choices=ASSET_TYPES, default='stock')
    symbol          = models.CharField(max_length=20)
    name            = models.CharField(max_length=100, blank=True)
    quantity        = models.DecimalField(max_digits=15, decimal_places=4)
    price           = models.DecimalField(max_digits=15, decimal_places=2, help_text='Price per unit at time of transaction')
    total_value     = models.DecimalField(max_digits=15, decimal_places=2, help_text='quantity × price')
    realized_pl     = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, help_text='Realized P/L for sell/book transactions')
    notes           = models.TextField(blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_transaction_type_display()} {self.symbol} × {self.quantity} @ ₹{self.price} — {self.user.username}"
