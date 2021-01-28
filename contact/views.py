from django.conf import settings
from django.core.mail import send_mail

from .models import Info
from django.shortcuts import render


# Create your views here.
def send_message(request):
    # here not use ModelForm  because not any data save in DB
    myinfo = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,  # from
            [settings.EMAIL_HOST_USER]  # to

        )

    return render(request, 'contact/contact.html', {'myinfo': myinfo})
