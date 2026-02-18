from django.db import models
from django.conf import settings

class Holding(models.Model):
    ASSET_TYPES = (
        ('stock', 'Stock'),
        ('etf', 'ETF'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='holdings')
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES, default='stock')
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2)
    current_price = models.DecimalField(max_digits=15, decimal_places=2)
    purchase_date = models.DateField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def total_cost(self):
        return self.quantity * self.purchase_price

    def market_value(self):
        return self.quantity * self.current_price

    def profit_loss(self):
        return self.market_value() - self.total_cost()

    def profit_loss_pct(self):
        if self.purchase_price == 0:
            return 0
        return (self.current_price - self.purchase_price) / self.purchase_price * 100

    def __str__(self):
        return f"{self.symbol} - {self.user.username}"
