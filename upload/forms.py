from django import forms
from .models import *

class UploadFileForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
 		model = UploadFile
 		widgets = {
 		'description':forms.Textarea(attrs={'cols': 150, 'rows': 20}),}
 		fields = ['fest_name','event_name','year','panelImages','thumbnails','link_day_zero','link_day_one','link_day_two','link_day_three','description',]
		