from django.core.mail import send_mail
from django.conf import settings 

def send_result(task):

    # sending email
    subject ='result update'
    from_email = settings.EMAIL_HOST_USER
    to_email = ['forance@gmail.com']
    contact_message = task.result

    send_mail(subject,
               contact_message,
               from_email,
               to_email, 
               fail_silently=False)