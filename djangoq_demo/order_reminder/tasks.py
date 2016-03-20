import datetime
from models import Orders
# import xlrd
from dateutil.relativedelta import relativedelta

def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.datetime.now()
    return from_date - relativedelta(years=years)



def order(duration):
    # all_orders = Orders.objects.all()
    end_date =yearsago(1).date()  # same date as today one years ago
    start_date = end_date - datetime.timedelta(days=duration) # starting date minus duration
  
    # print target_year
    match_orders = Orders.objects.filter(ship_date__gt=start_date,
    	                                 ship_date__lt=end_date)
    

    return (
        '{order} were placed during {start} to {end}'
        .format(order=match_orders, start=start_date, end=end_date )
    )
