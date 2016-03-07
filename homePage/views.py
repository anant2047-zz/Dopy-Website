from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from upload.models import *
from django.core.context_processors import csrf
import os,random

# Create your views here.
from django.shortcuts import render
from .forms import ContactForm
from PIL import Image
import re
# Create your views here.
def home(request):
	try:
		path = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" ,"events")
		recent_dir = [(os.path.getctime(os.path.join(path,f)), f)for f in os.listdir(path)]
		recent_dir.sort(reverse = True)
		event_title = []
		random_panel_image = []
		random_display_image = []

		try:
		
			for i in range(3):
				random_display_image.append( random.choice(os.listdir(os.path.join(path,recent_dir[i][1],"thumbnails","img")) ))
		except Exception:
			print("Images Not Found")
		
		
		k = 0
		for i,p in recent_dir:
			random_panel_image.append( random.choice(os.listdir(os.path.join(path,recent_dir[k][1],"thumbnails","img")) ))
			event_title.append(recent_dir[k][1])
			k+=1
			if k > 11:#ONLY 12 PANEL IMAGES ALLOWED TO AVOID CLUTTER
				break

		slider_name = []
		slider_title = []
		thumbnail_name = []
		thumbnail_title = []

		location = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))),"dopy_media")

		first_image = ""
		i = 1
		for f in os.listdir(os.path.join(location,"homepage","sliderImages","img")):
		#slider image can have atmost 12 images	
			if i == 1:
				first_image = f
				i+=1
				continue	
			if not i > 12:
				slider_name.append(f)
				slider_title.append(str(i))
			else :
				break 
			i+=1
		print(request.flavour)
		first_thumbnail = ""
		i=1
		for f in os.listdir(os.path.join(location,"homepage","thumbnails","img")):
			#thumbnails can have atmost 12 images	
			if i == 1:
				first_thumbnail = f
				i+=1
				continue
			if not i > 12:
				thumbnail_name.append(f)
				thumbnail_title.append(str(i))
			else :
				break 
			i+=1


		context = {
			"thumbnails_list" : zip(thumbnail_name,thumbnail_title),
			"slider_list":zip(slider_name,slider_title),
			# upper panel
			"title":event_title,
			"panel_list":zip(event_title,random_panel_image),
			"first_thumbnail":first_thumbnail,
			"first_image":first_image,
		}
		


		return render(request, "index.html",context)
	except Exception as e:
		print(e)
		return render(request,"500.html")



# def about(request):
# 	return render(request,"about.html")

# def portfolio(request):
# 	return render(request,"portfolio.html")

# def contact(request):
# 	return render(request,"contact-us.html")

# def test(request):

# 	some_list = []
# 	for i in range(100):
# 		some_list.append(str(i))

# 	context = {
# 		"some_list" : some_list,
# 	}
# 	return render(request,"test.html",context)


def events(request):
	
	event_name = request.get_full_path().replace("/events/","")
	print event_name
	event_name = re.sub('%20', ' ', event_name)
	print event_name
	try:
		UploadFile.objects.all().filter(event_name__icontains=event_name)


		event_name = request.get_full_path().replace("/events/","").lower()
		event_name = re.sub('%20', ' ', event_name)
		panel_name = []
		dl_link = []
		width = []
		height = []
		thumbnails = []
		link_present = ['True']*4
		day = []
		os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" ,"events")
		location = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" ,"events",event_name)
		#os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))) ,"dopy_media","events",event_name)
		
		for i in UploadFile.objects.all():
			if i.event_name.lower() == event_name.lower():
				if i.link_day_zero != "" :
					dl_link.append(i.link_day_zero)
					day.append("Day Zero")
				else:
					link_present[0] = 'False'
				if i.link_day_one != "" :
					dl_link.append(i.link_day_one)
					day.append("Day One")
				else:
					link_present[1] = 'False'
				if i.link_day_two != "" :
					dl_link.append(i.link_day_two)
					day.append("Day Two")
				else:
					link_present[2] = 'False'
				if i.link_day_three != "" :
					dl_link.append(i.link_day_three)
					day.append("Day Three")
				else:
					link_present[3] = 'False'

		download_button = 'False'
		for i in link_present:
			print i
			if i == 'True':
				download_button = 'True'
				print i
				break
		# for i in link_present:
		# 	print i
		print download_button

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
		facebook = thumbnails[0]
		print(facebook)

	



		context = {
			"title":event_name,
			"link":zip(link_present,dl_link,day),
			"data":zip(panel_name,thumbnails,width,height),
			"facebook":facebook,
			"download_button":download_button,
		}

		return render(request,"gallery_final.html",context)
	except Exception:
		 return render(request,"404.html")

def event_list(request):
	print("1")
	waves_list = []
	quark_list = []
	spree_list = []
	zephyr_list = []
	tedx_list = []
	other_list = []
	for i in UploadFile.objects.all():
		if i.fest_name == "W":
			waves_list.append(i.event_name)
			waves_list.sort()
		elif i.fest_name == "Q":
			quark_list.append(i.event_name)
			quark_list.sort()
		elif i.fest_name == "S":
			spree_list.append(i.event_name)
			spree_list.sort()
		elif i.fest_name == "Z":
			zephyr_list.append(i.event_name)
			zephyr_list.sort()
		elif i.fest_name == "T":
			tedx_list.append(i.event_name)
			tedx_list.sort()
		elif i.fest_name == "O":
			other_list.append(i.event_name)
			other_list.sort()
	print waves_list
	print other_list


	context = {
		"waves_list":waves_list,
		"quark_list":quark_list,
		"spree_list":spree_list,
		"zephyr_list":zephyr_list,
		"tedx_list":tedx_list,
		"other_list":other_list,
	}

	return render(request,"gallery_list.html",context)

def contact(request):
	form = ContactForm(request.POST or None)
	submit = True
	if form.is_valid():
		human = True
		print(human)

		for key in form.cleaned_data:
			print(form.cleaned_data.get(key))
			print(form.cleaned_data)
			
		form_email = form.cleaned_data.get("email")
		form_fullname = form.cleaned_data.get("fullname")
		form_message = form.cleaned_data.get("message")
		form_contact = form.cleaned_data.get("contact_number")

		subject = 'Site Email Message'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'otheremail@email.com']

		contact_message ="%s : \n %s via \n %s \tcontact:%s"%(
			form_fullname, 
			form_message, 
			form_email,
			str(form_contact),)
		form = ContactForm()
		

		# send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
		msg = EmailMessage(subject,contact_message,to=[from_email])
		msg.send()

			
	else:
		form = ContactForm(request.POST or None)
		human = False

	return render(request,"contact_new.html", locals())

def archive(request):
	links = LostAndFound.objects.all()
	# object = LostAndFound.objects.filter(year=2015)
	# object.delete()
	Context={
	"links":links
	}

	return render(request,"lostandfound.html",Context)


def search_titles(request):
	# print(request.POST['search_text'])
	# if request.method == 'POST':
	# 	search_text == request.POST['search_text']
	# else:
	# 	search_text = ''
	articles = UploadFile.objects.all.afilter(event_name__contains=request.POST['search_text'])
	
	return render_to_response('ajax_search.html',{'articles': articles})