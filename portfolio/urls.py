from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_overview, name='overview'),
    path('add-asset/', views.add_asset, name='add_asset'),
    path('edit-asset/<int:pk>/', views.edit_asset, name='edit_asset'),
    path('delete-asset/<int:pk>/', views.delete_asset, name='delete_asset'),
    path('refresh/', views.manual_refresh, name='refresh'),
    path('search-stocks/', views.search_stocks, name='search_stocks'),
]
