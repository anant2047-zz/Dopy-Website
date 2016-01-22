from django.contrib import admin
from .models import *
from .upload import Upload
from .forms import SignUpForm, UploadFileForm

# from .upload import upload
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["email", "timestamp", "updated"]
	# class Meta:
	# 	model = SignUp
	form = SignUpForm



admin.site.register(SignUp, SignUpAdmin)

# Register your models here.
class UploadFileAdmin(admin.ModelAdmin):
	# object = UploadImage.uploadname()
	# a,b = UploadImage.__str__()
	# a,b = "__str__".split("======================>")
	# list_display = ['Event','Filename'] 
	list_display = ["__str__","event_name"]
	form = UploadFileForm
	
	# class Meta:
	# 	#model = SignUp
	# form1 = UploadImageForm#can be skipped as well if forms.py is empty but use pass then
	# class Meta:
	# 	model = UploadImage
	# dictionary = ["__str__"]
	# a = dictionary['event_name']
	# b = dictionary['image'].split("/")
	# def Event(a):
	# 	return a
	# def event_name(self,request):
	#  	return request.FILES['image'].name
	# def uploaded_by(self,request):
	# 	return request.user.get_username()

	
	def save_model(self, request, obj, form, change=False):
       # do any pre-save stuff here
		print("hello before saving")
		obj.save()
		print("Hello")
		# global filename
		# filename = request.FILES['storage'].name
		# filesize = request.FILES['storage'].size
		# upload.main()
		event_name = request.POST.get('event_name')
		print(event_name)
		sliderImages = request.FILES['sliderImages'].name
		print(request.FILES['sliderImages'].name)
		panelImages = request.FILES['panelImages'].name
		storage = request.FILES['storage'].name
		print(request)
		# storage = filename = request.FILES['storage'].name
		Up = Upload()
		Up.startScript(event_name,sliderImages,panelImages,storage)
		#list_display = ["__str__","filename"]
		#list_display = ["__str__","filename"]
		# list_display.extend(filename)
		# list_display = ["a","b"]
		# list_display.extend(["__str__",filename])

		# filename = UploadImage
		# for f in files:
			# if object.endswith('.zip'):
			# 	obj.extractall()
			# 	print("Extracted File Successfully!")

admin.site.register(UploadFile, UploadFileAdmin)

# class EventNameAdmin(admin.ModelAdmin):
# 		form2 = EventNameForm
# 		list_display = ["__str__"]
# admin.site.register(EventName, EventNameAdmin)