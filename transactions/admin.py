from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display  = ('user', 'transaction_type', 'asset_type', 'symbol', 'quantity', 'price', 'total_value', 'realized_pl', 'created_at')
    list_filter   = ('transaction_type', 'asset_type')
    search_fields = ('symbol', 'name', 'user__username')
    ordering      = ('-created_at',)
