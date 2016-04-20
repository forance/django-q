from django import forms

from .models import Orders


class OrderForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = "__all__"