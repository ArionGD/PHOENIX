from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboard/', include('user_dashboard.urls', namespace='user_dashboard')),
    path('manager/', include('manager_dashboard.urls', namespace='manager_dashboard')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('transactions/', include('transactions.urls', namespace='transactions')),
]
