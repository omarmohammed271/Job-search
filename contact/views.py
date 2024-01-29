from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    return render(request,'contact/contact.html')
