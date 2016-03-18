from django import forms

from .models import orders


class ContactForm(forms.ModelForm):
	class Meta:
		model = orders
		fields = "__all__"