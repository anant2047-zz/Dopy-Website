from django import forms


class ContactForm(forms.Form):#use model to save the data in database just as SignUpForm
	fullname = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

