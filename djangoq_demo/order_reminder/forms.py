from django import forms

from .models import Orders


class ContactForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = "__all__"