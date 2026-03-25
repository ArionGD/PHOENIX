from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('support/', core_views.support, name='support'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboard/', include('user.urls', namespace='user')),
    path('manager/', include('admin.urls', namespace='dashboard_admin')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('transactions/', include('transactions.urls', namespace='transactions')),
    path('analysis/', include('analysis.urls', namespace='analysis')),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('tax/', include('tax.urls', namespace='tax')),
]
