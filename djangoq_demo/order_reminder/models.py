from django.db import models

# Create your models here.


class orders(models.Model):
	order_id = models.PositiveIntegerField()
	order_amount= models.DecimalField(max_digits=8, decimal_places=2)
	customer = models.CharField("Company Name",max_length=200, blank=False, null=True, unique=True)
	ship_date = models.DateField(auto_now_add=False, auto_now=False, null=True,\
		           help_text="Please use the following format: YYYY/MM/DD.", )

	def __unicode__(self):
		# return u'%s, %s' %(self.company.companyprofile_name, self.reference_id)
		#return u'%s' %(self.company.companyprofile_name)
		return u'%s' %(self.order_id)

