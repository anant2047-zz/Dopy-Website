from django.contrib import admin
from .models import *
from .upload import Upload
from .forms import UploadFileForm

# Register your models here.
class UploadFileAdmin(admin.ModelAdmin):
	list_display = ["event_name","link_day_zero","link_day_one","link_day_two","link_day_three","fest_name","year","description"]
	list_filter = ["year","fest_name"]
	list_editable = ["link_day_zero","link_day_one","link_day_two","link_day_three"]
	search_fields = ["event_name","fest_name"]
	form = UploadFileForm


	
	# def save_model(self, request, obj, form, change=False):
	# 	print("hello before saving")
	# 	obj.save()
	# 	print("Hello")
	# 	event_name = request.POST.get('event_name')
		
	# 	panelImages = request.FILES['panelImages'].name
	# 	thumbnails = request.FILES['thumbnails'].name
	# 	Up = Upload()
	# 	Up.startScript(event_name.lower(),panelImages,thumbnails)



admin.site.register(UploadFile, UploadFileAdmin)
