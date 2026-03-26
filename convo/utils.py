from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from datetime import datetime

def send_notification_email(notification, dashboard_url):
    """
    Sends a premium formatted HTML email for a given notification.
    """
    subject = f"PHOENIX ALERT: {notification.title}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = notification.user.email
    
    context = {
        'notification': notification,
        'dashboard_url': dashboard_url,
        'year': datetime.now().year
    }
    
    html_content = render_to_string('convo/emails/notification_email.html', context)
    text_content = strip_tags(html_content)
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
