from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.conf import settings
import os


# Create your views here.
def services(request):

	return render(request,'services.html')

def photography(request):

	path_images = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","static_root" ,"services","gallery","photography","images")
	path_thumbnails = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","static_root" ,"services","gallery","photography","thumbnails")
	images=[]
	thumbnails = []
	for i in os.listdir(path_thumbnails):
		thumbnails.append(i)

	for f in os.listdir(path_images):
		images.append(f)
	
	context={
	"image_list":zip(images,thumbnails)
	}
	
	return render(request,'gallery.html',context)


def advertising(request):

	return render(request,'portfolio.html')


def weddings(request):

	return render(request,'weddings.html')


