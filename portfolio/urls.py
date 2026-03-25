from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_overview, name='overview'),
    path('add-asset/', views.add_asset, name='add_asset'),
    path('edit-asset/<int:pk>/', views.edit_asset, name='edit_asset'),
    path('delete-asset/<int:pk>/', views.delete_asset, name='delete_asset'),
    path('price-update/<int:pk>/', views.get_live_price_json, name='get_live_price_json'),
    path('value-update/<int:pk>/', views.get_market_value_json, name='get_market_value_json'),
    path('book-profit/<int:pk>/', views.book_profit, name='book_profit'),
    path('refresh/', views.manual_refresh, name='refresh'),
    path('search-stocks/', views.search_stocks, name='search_stocks'),
]
