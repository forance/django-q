import datetime
import xlrd



def order_fruit():

	# book = xlrd.open_workbook("orders.xlsx")
	# orders = book.sheet_by_index(0)
	# today = datetime.datetime.now().date()
	# target_date = today+datetime.timedelta(days=2)

	# for i in range(0,4):
	# 	xldate = orders.cell_value(rowx=i, colx=1)
	# 	order_time = datetime.datetime(*xlrd.xldate_as_tuple(xldate, book.datemode))
	# 	order_date = order_time.date()
	# 	if target_date == order_date:
	# 		target_order = orders.cell_value(rowx=i, colx=0) 
	# 		print "match", target_order
    
    target_order="success"
    return (
        '{order} is due in 2 days later'
        .format(order=target_order)
    )
