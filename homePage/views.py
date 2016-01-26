from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
import os,random

# Create your views here.
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
	path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events")
	recent_dir = [(os.path.getctime(os.path.join(path,f)), f)for f in os.listdir(path)]
	recent_dir.sort(reverse = True)
	event_title = os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events"))
	random_display_image = []
	for i in range(3):
		random_display_image.append( random.choice(os.listdir(os.path.join(path,recent_dir[i][1],"sliderImages","img")) ))
	

	random_panel_image = []
	for i,p in recent_dir:
		k=0
		random_panel_image.append( random.choice(os.listdir(os.path.join(path,recent_dir[k][1],"panelImages","img")) ))
		k+=1

	# print(random_panel_image)
	# print(event_title)

	slider_name = []
	slider_title = []
	thumbnail_name = []
	thumbnail_title = []

	location = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root")

	i = 1
	for f in os.listdir(os.path.join(location,"home_slider","img")):
	#slider image can have atmost 12 images		
		if not i > 12:
			slider_name.append(f)
			slider_title.append(str(i))
		else :
			break 
		i+=1
	print(slider_name)

	i=1
	for f in os.listdir(os.path.join(location,"home_slider","thumbnails")):
		#thumbnails can have atmost 12 images		
		if not i > 12:
			thumbnail_name.append(f)
			thumbnail_title.append(str(i))
		else :
			break 
		i+=1


	context = {
		"event1" : recent_dir[0][1],
		"event1_image" : random_display_image[0],
		"event2" : recent_dir[1][1],
		"event2_image" : random_display_image[1],
		"event3" : recent_dir[2][1],
		"event3_image" : random_display_image[2],
		#slider
		"thumbnails_list" : zip(thumbnail_name,thumbnail_title),
		"slider_list":zip(slider_name,slider_title),
		# upper panel
		"title":event_title,
		"panel_list":zip(event_title,random_panel_image),
	}
	


	return render(request, "index.html",context)

def about(request):
	return render(request,"about.html")

def contact(request):
	return render(request,"contact-us.html")

def test(request):

	some_list = []
	for i in range(100):
		some_list.append(str(i))

	context = {
		"some_list" : some_list,
	}
	return render(request,"test.html",context)


def gallery(request):
	event_name = request.get_full_path().replace("/gallery/","").lower()
	slider_name = []
	slider_title = []
	thumbnail_name = []
	thumbnail_title = []
	panel_name = []

	location = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name)

	i = 1
	for f in os.listdir(os.path.join(location,"sliderImages","img")):
	#slider image can have atmost 12 images		
		if not i > 12:
			slider_name.append(f)
			slider_title.append(str(i))
		else :
			break 
		i+=1

	i=1
	for f in os.listdir(os.path.join(location,"thumbnails","img")):
		#thumbnails can have atmost 12 images		
		if not i > 12:
			thumbnail_name.append(f)
			thumbnail_title.append(str(i))
		else :
			break 
		i+=1

	for f in os.listdir(os.path.join(location,"panelImages","img")):
		#panelImages can have atmost 12 images		
		panel_name.append(f)



	context = {
		"title":event_name,
		"thumbnails_list" : zip(thumbnail_name,thumbnail_title),
		"slider_list":zip(slider_name,slider_title),
		"panel_list":panel_name,
	}

	return render(request,"GalleryScrollTemplate.html",context)



def contact(request):
	form = ContactForm(request.POST or None)
	context ={
		"form":form,
		"submit":True
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
		context = {

		}



	return render(request, "contact-us.html", context)