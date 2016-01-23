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
from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
	# if request.user.is_authenticated():
	# 	title = title + ", %s" %(request.user)
	#add a form
	# if request.method == "POST":
	# 	print(request.POST)
	form = SignUpForm(request.POST or None)#makes sure method is POST

	context = {
	"form":form,
	}
	if form.is_valid():
		#print(request.POST['email']) Will fetch raw data and skip any validation even after putting it under is_valid function.So,its NOT Recommended
		#form.save() will save directly and will not allow us to use any filters
		instance = form.save(commit=False) #helps to filter data because its not saved and we can do whatever we want with data till we save it.
		if not instance.fullname:
			#fullname="whatever" can be done as well
			instance.fullname = "Yoman"
		instance.save()
		# print(instance)
		# print(instance.timestamp)

	# 	context = {
	# "title":"Thank You!",
	# }
	return render(request,"index.html",context)
	# return render(request, "index.html")

def about(request):
	return render(request,"about.html")

def contact(request):
	return render(request,"contact-us.html")

# def test(request):

# 	some_list = []
# 	for i in range(100):
# 		some_list.append(str(i))

	
# 	context = {
# 		"some_list" : some_list,
# 	}
# 	return render(request,"test.html",context)


def gallery(request):
	# event_name = request.get_full_path().replace("/gallery/","").lower()
	# slider_list = []
	# location = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name)

	# #slider image and thumbnail can have atmost 10 images
	# for f in os.listdir(os.path.join(location,"sliderImages","img")):
	# 	slider_list.append(str(i))

	# #slider image and thumbnail can have atmost 12 images
	# if not len(slider_list) <= 12:
	# 	slider_list = []
	# 	for i in range(1,13):
	# 		slider_list.append(str(i))

	# context = {
	# 	"title":event_name,
	# 	"thumbnail_list" : slider_list,
	# 	"slider_list":slider_list,
	# }
	return render(request,"GalleryScroll.html")



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

		#send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
		context = {

		}



	return render(request, "contact-us.html", context)