from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('update-budget/', views.update_budget, name='update_budget'),
    path('cagr-calculator/', views.cagr_calculator, name='cagr_calculator'),
    path('cagr-target/', views.cagr_target, name='cagr_target'),
]
