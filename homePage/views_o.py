from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
	return render(request, "index.html")

def about(request):
	return render(request,"about.html")

def contact(request):
	return render(request,"contact-us.html")

def gallery(request):
	
	return render(request,"GalleryScroll.html")



def contact(request):
	form = ContactForm(request.POST or None)
	context ={
		"form":form,
		"submit":True,
	}
	if form.is_valid():
		for key in form.cleaned_data:#.iteritems():
		# 	print(key)
			print(form.cleaned_data.get(key))
			print(form.cleaned_data)
			
		form_email = form.cleaned_data.get("email")
		form_fullname = form.cleaned_data.get("fullname")
		form_message = form.cleaned_data.get("message")

		subject = 'Site Email Message'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'otheremail@email.com']

		contact_message ="%s %s via %s"%(
			form_fullname, 
			form_message, 
			form_email)

		send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
		context={
		
		}



	return render(request, "contact-us.html", context)