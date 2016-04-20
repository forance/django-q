from decimal import Decimal
from django.db import models

# Create your models here.


class Orders(models.Model):
	order_id = models.CharField( max_length=200, blank=False, null=True, unique=True)
	ship_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
	customer = models.CharField("Company Name",max_length=200, blank=False, null=True)
	currency= models.CharField(max_length=200, blank=False, null=True)
	creater = models.CharField(max_length=200, blank=False, null=True)
	order_amount= models.DecimalField(max_digits=10, decimal_places=2)
	paid_amount= models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
	create_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
	pay_term = models.CharField("Payment Term",max_length=200, blank=False, null=True)
	updater = models.CharField(max_length=200, blank=False, null=True)
	
	def __unicode__(self):
		# return u'%s, %s' %(self.company.companyprofile_name, self.reference_id)
		#return u'%s' %(self.company.companyprofile_name)
		return u'%s, %s, %s $%s, %s' %(self.order_id, self.customer, self.currency, self.order_amount, self.creater)

