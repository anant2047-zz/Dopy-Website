from django import forms
# from django.contrib.auth.models import User
from .models import *

class ServiceForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
 		model = Service
 		widgets = {
 		'description':forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
 		fields = ['service_name','panelImages','thumbnails','link','description',]

# class UserInformationForm(forms.ModelForm):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	contact_number = forms.IntegerField()
# 	address = forms.CharField(widget=forms.Textarea)
# 	class Meta:
# 		model = UserInformation
# 		widgets = {
#  		'address':forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
# 		fields = ['full_name','user_email','contact_number','address']

