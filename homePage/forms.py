from django import forms
from .models import SignUp


class ContactForm(forms.Form):#use model to save the data in database just as SignUpForm
	fullname = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = SignUp
		widgets = {'password': forms.PasswordInput(),}
		fields = ['fullname', 'email','password']

	def clean_email(self):
		print("working!")
		email = self.cleaned_data.get('email')
		base_email, provider = email.split("@")
		domain, extension = provider.split(".")
		# if not domain == "gmail":
		# 	raise forms.ValidationError("Please enter a valid gmail email")
		if not extension == "edu":
			raise forms.ValidationError("Please enter a valid edu email")
		return email
