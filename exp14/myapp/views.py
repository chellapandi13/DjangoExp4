# myapp/views.py

from django.http import HttpResponse
from .emails import send_email

def send_email_view(request):
    subject = "Test Email"
    message = "This is a test email from Django."
    recipient_list = ['22uit019@kamarajengg.edu.in']  # Recipient email address
    send_email(subject, message, recipient_list)
    return HttpResponse("Email sent successfully!")
