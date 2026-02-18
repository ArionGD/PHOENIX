from django.contrib import admin
from .models import Holding

@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'user', 'asset_type', 'quantity', 'current_price', 'market_value')
    list_filter = ('asset_type', 'user')
    search_fields = ('symbol', 'name')
