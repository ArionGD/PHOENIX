from django.urls import path
from . import views

app_name = 'tax'

urlpatterns = [
    path('', views.tax_calculator, name='calculator'),
    path('report/', views.tax_report, name='report'),
]
