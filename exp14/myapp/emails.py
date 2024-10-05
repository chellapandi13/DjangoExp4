# myapp/emails.py

from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        '22uit072@kamarajengg.edu.in',  # From email address
        recipient_list,
        fail_silently=False,
    )
