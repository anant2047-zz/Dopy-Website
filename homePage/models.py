from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	fullname = models.CharField(max_length=120, blank=True, null=True)
	#password =forms.CharField(widget=forms.PasswordInput())
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email