from django.contrib import admin

# Register your models here.
from .models import Orders



class OrdersAdmin(admin.ModelAdmin):
	date_hierarchy = 'create_date'
	list_display = ('order_id', 'customer', 'creater', 'ship_date','pay_term','create_date','updater')
	ordering = ['-create_date']
	# fields = ('order_id', 'customer', 'creater', 'create_date')


admin.site.register(Orders,OrdersAdmin)
