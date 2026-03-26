from django.urls import path
from . import views

app_name = 'convo'

urlpatterns = [
    path('notifications/', views.NotificationListView.as_view(), name='notifications'),
    path('support/', views.SupportTicketView.as_view(), name='support'),
]
