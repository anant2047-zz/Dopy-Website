from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.conf import settings
from .models import Service
# from django.contrib.auth.forms import AuthenticationForm
import os
import re
# from .forms import UserInformationForm
from PIL import Image
from .get_video_id import *


# Create your views here.
def services(request):
	return render(request,'services.html')

def photography(request):
	try:
		panel_name = []
		width = []
		height = []
		thumbnails = []
		location = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" ,"services","P")
		#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services","W")
		
		for f in os.listdir(os.path.join(location,"thumbnails","img")):
			thumbnails.append(f)
		

		for f in os.listdir(os.path.join(location,"panelImages","img")):	
			panel_name.append(f)
			
		thumbnails.sort()
		panel_name.sort()
		for f in panel_name:
			im = Image.open(os.path.join(location,"panelImages","img",f))
			width.append(im.size[0])
			height.append(im.size[1])



		context = {
			"title":"Photography",
			"location":"P",
			"data":zip(panel_name,thumbnails,width,height),
		}

		return render(request,"gallery_services.html",context)
	except Exception as e:
		print(e)
		return render(request,"coming-soon.html")

def advertising(request):
	links=[]
	
	for i in Service.objects.all():
		
		if i.service_name == 'A':
			links.append(get_yt_video_id(i.link))

	

	print(links)

	context = {
		"title":"Advertisements",
		"location":"A",
		"link":links,
	}

	return render(request,"advertisements.html",context)


	# return render(request,'portfolio.html')


def weddings(request):
	try:
		panel_name = []
		width = []
		height = []
		thumbnails = []
		location = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" ,"services","W")
		#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services","W")
		
		for f in os.listdir(os.path.join(location,"thumbnails","img")):
			thumbnails.append(f)
		

		for f in os.listdir(os.path.join(location,"panelImages","img")):	
			panel_name.append(f)
			
		thumbnails.sort()
		panel_name.sort()
		for f in panel_name:
			im = Image.open(os.path.join(location,"panelImages","img",f))
			width.append(im.size[0])
			height.append(im.size[1])



		context = {
			"title":"Weddings",
			"location":"W",
			"data":zip(panel_name,thumbnails,width,height),
		}

		return render(request,"gallery_services.html",context)
	except Exception as e:
		print(e)
		return render(request,"coming-soon.html")

# def userProf(request):
		
# 	form = UserInformationForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		if not instance.contact_number:
# 			instance.contact_number = ""
# 		if not instance.address:
# 			instance.address = ""
# 		if not instance.full_name:
# 			instance.full_name = request.user
# 		if not instance.email:
# 			instance.email = request.user.email
# 		instance.save()
	
# 	form1 = AuthenticationForm(data=request.POST)
	
# 	context={
# 	"form":form,
# 	"form1":form1,
# 	}
# 	return render(request,"user_prof.html",context)
