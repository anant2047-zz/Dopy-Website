from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
	fullname = forms.CharField(required=False)
	email = forms.EmailField()
	contact_number = forms.CharField(required=False)
	message = forms.CharField(widget=forms.Textarea)
	captcha = ReCaptchaField()
	captcha = ReCaptchaField(
    public_key='6LenfBkTAAAAAGxCwZ06pQ0Q7P8g0tOgegJysQC1',
    private_key='6LenfBkTAAAAAPb4QNB2mwjYisPvxCuMZQb39LhG',
    use_ssl=True
	)
	
	widgets = {
	'message':forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
	def clean_contact_number(self):
		contact_number = self.cleaned_data.get('contact_number', None)
		try:
			int(contact_number)
		except Exception:
			raise forms.ValidationError("Please enter a valid contact number")
		return contact_number
 
 