import re,time
from django.core.mail import send_mail
from django.conf import settings 
from django.template.loader import get_template
# from django.core.mail import EmailMessage



email_list = { 'NICK':['nick.tang@shugie.com.tw','Nick'], 'ADISON':['sg-5@shugie.com.tw', 'Adison'],'VITA':['sg-2@shugie.com.tw','Vita'],
                'SHERRY':['shugie@shugie.com.tw', 'Sherry'],'ANGELA':['sg-3@shugie.com.tw', 'VIVI'],'JUDY':['@shugie.com.tw', 'ADA']}
# email_list= ['forance@gmail.com']




def custom_mail(result, start_date, end_date, template, title ):

  for key, value in email_list.iteritems():
    matches = [x for x in result if key in x]

    ctx = {
        'start_date':start_date,
        'end_date': end_date, 
        'context': matches,
       
    }

    message = get_template(template).render(ctx)

    # sending email
    subject = title +value[1]+' '+time.strftime("%Y/%m/%d") 
    from_email = settings.EMAIL_HOST_USER
    to_email = [value[0],'nick.tang@shugie.com.tw']
    # to_email = ['forance@gmail.com']
    # contact_message = task.result

    send_mail(subject,
               message,
               from_email,
               to_email, 
               fail_silently=False,
               html_message=message)





def order_reminder_result(task):
    result = task.result
    split_result = re.findall(r"<.*?>", result)
    title = 'Customers follow up list -'

    match=re.findall(r'(\d+-\d+-\d+)',result)
    if match:
       start_date, end_date = match
    else:
      print "no date found"
    
    custom_mail(split_result,start_date,end_date,"order_email.html", title )
    

def payment_reminder_result(task):
    result = task.result
    split_result = re.findall(r"<.*?>", result)
    title = 'Customers payment follow up  -'


    match=re.findall(r'(\d+-\d+-\d+)',result)
    if match:
       start_date, end_date = match
    else:
      print "no date found"
    
    custom_mail(split_result,start_date,end_date,"payment_email.html", title )
    
    # ctx = {
    #     'start_date':start_date,
    #     'end_date': end_date, 
    #     'context': split_result,
       
    # }

    # message = get_template('email.html').render(ctx)


    # # sending email
    # subject ='Orders One Year Ago'
    # from_email = settings.EMAIL_HOST_USER
    # to_email = email_list
    # # contact_message = task.result
   

    # send_mail(subject,
    #            message,
    #            from_email,
    #            to_email, 
    #            fail_silently=False,
    #            html_message=message)