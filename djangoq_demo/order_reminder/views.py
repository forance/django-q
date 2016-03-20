import logging, datetime
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django_q.humanhash import humanize
from django_q.models import OrmQ
from django_q.tasks import async, Task


logger = logging.getLogger(__name__)



# from django_q.tasks import schedule

# schedule('order_reminder.tasks.order_fruit',
#          2, -2,
#          # hook='order_reminder.hooks.send_result',
#          schedule_type='I')



def home(request):
    if request.method == 'POST':
        #Parse the form params
        try:
            # fruit = request.POST.get('fruit_type', '')
            duration = int(request.POST.get('duration', '0'))
        except ValueError:
            return HttpResponseBadRequest('Invalid request!')
        #Create async task
        if duration != 0:
            task_id = async(
                'order_reminder.tasks.order',
                 duration,
                 # hook='order_reminder.hooks.send_result'
            )
            messages.info(
                request,
                ' trace order from past {duration:d} days (task: {task})'
                .format(duration=duration, task=humanize(task_id))
            )
     
    today = datetime.datetime.now()
    # Select orders in queue
    queue_orders = OrmQ.objects.all().order_by('lock')

    # Select finished orders
    complete_orders = Task.objects.all().filter(
        func__exact='order_reminder.tasks.order',
    )
    return render(request, 'index.html', {
            'today':today,
            'queue_orders': queue_orders,
            'complete_orders': complete_orders
    })





















