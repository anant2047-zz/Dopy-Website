from django.db import models
import os


class UploadFile(models.Model):
	event_name=models.CharField(max_length=120, blank=False, null=False)
	sliderImages = models.FileField(upload_to='events/sliderImages/', blank=False, null=False)
	panelImages = models.FileField(upload_to='events/panelImages/', blank=False, null=False)
	storage = models.FileField(upload_to='events/storage/', blank=False, null=False)
	# timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	# updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	# def __init__(self):
	# 	pass

	# def uploadfilename(self):
	# # 	filename = request.FILES['image'].name
	# # 	#print(filename)
	# # 	print("sdfsfsdf")
	# # 	return filename
	# 	return os.path.basename(self.image.name)

	# def __str__(self):
	# 	return '%s' %(self.event_name)
	def __str__(self):
		return os.path.basename(self.storage.name)
class SignUp(models.Model):
	email = models.EmailField()
	fullname = models.CharField(max_length=120, blank=True, null=True)
	#password =forms.CharField(widget=forms.PasswordInput())
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email


		#return self.event_name
		# global temp
		# temp = self.__dict__.copy()
		# self.__dict__.clear()
		# # list_display = []
		# # for key in self.__dict__:
		# # 	list_display.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
		# # return ', '.join(list_display)
		# temp['event_name']=self.__dict__['event_name']
		# temp['image']=self.__dict__['image']

