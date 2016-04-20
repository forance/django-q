import datetime
from models import Orders
# import xlrd
from dateutil.relativedelta import relativedelta
from decimal import Decimal

from django.db.models import Q


def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.datetime.now()
    return from_date - relativedelta(years=years)


def name_list(seq):
	name_list=[]
	for i in seq:
		if i.customer not in name_list:
			name_list.append(i.customer)
	return name_list

def compare(seq1,seq2):
	for i in seq1:
		if i in seq2:
			seq1.remove(i)
	return seq1

def order_q(starting, end):
	orders_obj = Orders.objects.filter(ship_date__gte=starting, ship_date__lte=end)
	if orders_obj is None:
		orders_obj = 'No orders'
	return name_list(orders_obj)



def order(duration):
    # search order from one years ago
    end_date =yearsago(1).date()  # same date as today one years ago
    start_date = end_date - datetime.timedelta(days=duration) # starting date minus duration

    old_customer_list = order_q(start_date, end_date)
    # print old_customer_list
  
    # search order from this year
    today = datetime.datetime.now()
    past = today - datetime.timedelta(days=duration) # starting date minus duration

    new_customer_list = order_q(past, today)
    # print new_customer_list
   
    # finding the customer who does not place order this year in the given period
    no_orders = compare(old_customer_list, new_customer_list)

    # use list() , otherwise the result would be truncated
    no_orders_obj = list(Orders.objects.filter(ship_date__gte=start_date, 
    	                                    ship_date__lte=end_date).filter(customer__in=no_orders).order_by('creater','ship_date'))

    # print len(no_orders_obj)
    
    return (
        '{order} were placed during {start} to {end}'
        .format(order=no_orders_obj, start=start_date, end=end_date )
    )



def payment_reminder(duration):

    paymet_term = ['3070','5050','1585']

    today = datetime.datetime.now()
    start = today - datetime.timedelta(days=duration) # starting date minus duration
    end = today - datetime.timedelta(days=14 )

    unpaid = list(Orders.objects.filter(ship_date__gte=start, 
                    ship_date__lte=end).filter(paid_amount=Decimal('0')).filter(reduce(lambda x, y: x | y, [Q(pay_term__contains=term) for term in paymet_term])).order_by('creater','-order_amount'))

   

    return (
        '{order} are unpaid during {start} to {end}'
        .format(order=unpaid, start=start, end=end )
    )







def updb():
    # from os import getenv
    import pymssql
    # server = 'server2'
    host='192.168.2.113'
    user = 'nicktang'
    password = 'forance0708'
    timeout= '60'
    
    try:
        conn = pymssql.connect(host, user, password, "winQHs", timeout)
        cursor = conn.cursor()

    except Exception as e:
            return (
                     'Connection failed on {now} with Error {error}'
                     .format(now=datetime.datetime.today(), error=e.message)
            )

    cursor.execute("""
    select sc.DocNo, sc.CustID, sc.DDate, sc.Curncy, sc.OrdAmt, sc.RvdAmt, sc.Creater,sc.CDate,sc.Payment, sc.Updater
    from dbo.SC AS sc
    where CDate between '2015-01-01' and '2016-12-31'
    ORDER BY DDate DESC;
    """)

    # def data_gen(seq):
    #     for row in seq:
    #         yield row
    
    create = duplicate  = 0
    
    for index, item in enumerate(cursor, start=1):
        try:
              updated_values = { 'ship_date':item[2], 'currency':item[3], 'order_amount':item[4], 'paid_amount':item[5],'pay_term': item[8], 'updater':item[9]}
              obj, created = Orders.objects.update_or_create(order_id=item[0], customer=item[1],creater=item[6],
                      create_date=item[7],defaults=updated_values )
            
              if created:
                create += 1
              else:
                duplicate += 1
                pass
              

        except Exception as e:
            # print e.message, e.args
            conn.close()
            return (
                     'Failed on {now} with Error {error}'
                     .format(now=datetime.datetime.today(), error=e.message)
            )
 
      
    conn.close()

    return (
        'total {i} orders processed, {c} orders created and {d} orders updated sucessfully on {now}'
        .format(i=index, c=create, d=duplicate  ,now=datetime.datetime.today())
    )















