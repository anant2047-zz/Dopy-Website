from django.db import models
from django.db.models.signals import pre_delete
from django.db.models import signals
from .upload import Upload
from dopy.settings.base import *
from django.conf import settings
from datetime import datetime
import os

class UploadFile(models.Model):
	event_name=models.CharField(max_length=120, blank=False, null=False)
	panelImages = models.FileField(upload_to=os.path.join(MEDIA_ROOT,"temporary","panelImages"), blank=False, null=False)
	thumbnails = models.FileField(upload_to=os.path.join(MEDIA_ROOT,"temporary","thumbnails"), blank=False, null=False)
	link_day_zero = models.CharField(max_length=240,blank=True,null=False,default="")
	link_day_one = models.CharField(max_length=240,blank=True,null=False,default="")#make blank=False for production
	link_day_two = models.CharField(max_length=240,blank=True,null=False,default="")
	link_day_three = models.CharField(max_length=240,blank=True,null=False,default="")
	description = models.CharField(max_length=200,blank=True)
	year = models.CharField(max_length=4,blank=False,null=True,default=datetime.now().year)

	FEST_NAME = (
        ('W', 'Waves'),
        ('Q', 'Quark'),
        ('S', 'Spree'),
        ('Z', 'Zephyr'),
        ('T', 'TEDx'),
        ('O', 'Others'),
    )
	fest_name = models.CharField(max_length=1, choices=FEST_NAME,null=True, default="O")
	

	
def delete_files(sender,instance, **kwargs):
	# for i in UploadFile.objects.all():
	try:
		up = Upload()
		event_name_variable = instance.event_name

		Lost = LostAndFound(event_name=event_name_variable.lower(),link=instance.link,year=instance.year)
		Lost.save()
		up.del_files(event_name_variable.lower())
	except Exception as e:
		print(e)
		pass
def upload_files(sender,instance,**kwargs):
	try:
		up = Upload()
		event_name= str(instance.event_name.lower())
		panelImages = str(instance.panelImages)
		thumbnails = str(instance.thumbnails)
		up.startScript(event_name,panelImages,thumbnails)
	except Exception as e:
		print(e)

signals.post_save.connect(upload_files,sender=UploadFile)

signals.pre_delete.connect(delete_files,sender=UploadFile)

class LostAndFound(models.Model):
	link = models.CharField(max_length=240,blank=True,null=False,default="notfound")
	year = models.CharField(max_length=4,blank=False,null=True)
	event_name=models.CharField(max_length=120, blank=False, null=True)


