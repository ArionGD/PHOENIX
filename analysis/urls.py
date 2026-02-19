from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('explain/', views.explain_market, name='explain'),
]
