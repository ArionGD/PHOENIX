from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_overview, name='overview'),
    path('add-asset/', views.add_asset, name='add_asset'),
    path('search-stocks/', views.search_stocks, name='search_stocks'),
]
