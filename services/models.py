from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models import signals
from .upload_services import Upload
from django.contrib.auth.models import User
from dopy.settings.base import *
import os

class Service(models.Model):
	
	panelImages = models.FileField(upload_to=os.path.join(MEDIA_ROOT,"temporary","panelImages"), blank=True, null=True)
	thumbnails = models.FileField(upload_to=os.path.join(MEDIA_ROOT,"temporary","thumbnails"), blank=True, null=True)
	link = models.CharField(max_length=200,blank=True,null=True)
	description = models.CharField(max_length=500,blank=True)
	

	SERVICE_NAME = (
        ('P', 'Photography'),
        ('A', 'Advertisements'),
        ('W', 'Weddings'),
        
    )
	service_name = models.CharField(max_length=1, choices=SERVICE_NAME,null=True, default="P")

def upload_files(sender,instance, **kwargs):
	# for i in UploadFile.objects.all():
	try:
		up = Upload()
		up.startScript(str(instance.service_name),str(instance.panelImages),str(instance.thumbnails))
	except Exception as e:
		print(e)
		pass

signals.post_save.connect(upload_files,sender=Service)

def del_files(sender,instance, **kwargs):
	# for i in UploadFile.objects.all():
	up = Upload()
	up.del_files(instance.service_name)
	

signals.pre_delete.connect(del_files,sender=Service)
	
class UserInformation(models.Model):
	full_name= models.CharField(max_length=100,null=True)
	user_email = models.EmailField()
	contact_number = models.IntegerField(null=True)
	address = models.CharField(max_length=100,blank=True,null=True,default="fsf")

	
		


