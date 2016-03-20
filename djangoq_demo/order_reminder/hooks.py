from django.core.mail import send_mail
from django.conf import settings 
from django.template.loader import get_template
# from django.core.mail import EmailMessage
import re


email_list = ['nick.tang@shugie.com.tw', 'sg-5@shugie.com.tw']
# email_list = ['forance@gmail.com']

def send_result(task):
    result = task.result
    split_result = re.findall(r"<.*?>", result)
    print split_result

    match=re.findall(r'(\d+-\d+-\d+)',result)
    if match:
       start_date, end_date = match
    else:
      print "no date found"


    ctx = {
        'start_date':start_date,
        'end_date': end_date, 
        'context': split_result,
       
    }

    message = get_template('email.html').render(ctx)


    # sending email
    subject ='Orders One Year Ago'
    from_email = settings.EMAIL_HOST_USER
    to_email = email_list
    # contact_message = task.result
   

    send_mail(subject,
               message,
               from_email,
               to_email, 
               fail_silently=False,
               html_message=message)