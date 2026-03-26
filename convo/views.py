from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View
from .models import Notification, SupportTicket
from datetime import datetime

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'convo/notifications.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = datetime.now().year
        return context

class SupportTicketView(LoginRequiredMixin, View):
    def get(self, request):
        tickets = SupportTicket.objects.filter(user=request.user)
        return render(request, 'convo/support.html', {
            'tickets': tickets,
            'year': datetime.now().year
        })

    def post(self, request):
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if subject and message:
            SupportTicket.objects.create(
                user=request.user,
                subject=subject,
                message=message
            )
        return redirect('convo:support')
