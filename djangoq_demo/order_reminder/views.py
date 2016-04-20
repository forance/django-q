import logging, datetime
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django_q.humanhash import humanize
from django_q.models import OrmQ
from django_q.tasks import async, Task


logger = logging.getLogger(__name__)



def  reminder(duration, request):
    if duration != 0:
            task_id = async(
                'order_reminder.tasks.order',
                 duration,
                 # hook='order_reminder.hooks.order_reminder_result'
            )
            messages.info(
                request,
                ' trace order from past {duration:d} days (task: {task})'
                .format(duration=duration, task=humanize(task_id))
            )
    else:
        print "no reminder set!"

def update_db(update, request):
    if update:
        task_id = async(
                'order_reminder.tasks.updb',
                 # hook='order_reminder.hooks.send_result'
            )
        messages.info(
            request,
                ' updating database (task: {task})'
                .format(task=humanize(task_id))
            )

    else:
        print "no update"

def  payment(payment, request):
    if payment != 0:
            task_id = async(
                'order_reminder.tasks.payment_reminder',
                 payment,
                 hook='order_reminder.hooks.payment_reminder_result'
            )
            messages.info(
                request,
                ' trace payment from past {duration:d} days (task: {task})'
                .format(duration=payment, task=humanize(task_id))
            )
    else:
        print "no payment checking"




def home(request):
    if request.method == 'POST':
        # print request.POST
        #Parse the form params
        try:
            # fruit = request.POST.get('fruit_type', '')
            duration = int(request.POST.get('duration', '0'))
            update = request.POST.get('update')
            pay = int(request.POST.get('payment', '0'))

        except ValueError:
            return HttpResponseBadRequest('Invalid request!')

        #Create async task
        reminder(duration, request)
        update_db(update,  request)
        payment(pay, request)
        
     
    today = datetime.datetime.now()
    # Select orders in queue
    queue_orders = OrmQ.objects.all().order_by('lock')

    # Select finished orders
    complete_orders = Task.objects.all().filter(
        func__exact='order_reminder.tasks.order',
    )

    complete_update = Task.objects.all().filter(
        func__exact='order_reminder.tasks.updb',
    )

    complete_payment = Task.objects.all().filter(
        func__exact='order_reminder.tasks.payment_reminder',
    )

    

    return render(request, 'index.html', {
            'today':today,
            'queue_orders': queue_orders,
            'complete_orders': complete_orders,
            'complete_update': complete_update,
            'complete_payment': complete_payment
    })





















