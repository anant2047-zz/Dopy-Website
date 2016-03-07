from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models import signals
from dopy.settings.base import *
from .upload_home import *

# Create your models here.
class HomePage(models.Model):
	sliderImages = models.FileField(upload_to=os.path.join(MEDIA_ROOT,"temporary","sliderImages"),blank=True,null=True)
	thumbnails = models.FileField(upload_to=os.path.join(MEDIA_ROOT,"temporary","thumbnails"),blank=True,null=True)

def upload_files(sender,instance, **kwargs):
	# for i in UploadFile.objects.all():
	up = Upload()
	up.startScript(str(instance.sliderImages),str(instance.thumbnails))
	

signals.post_save.connect(upload_files,sender=HomePage)

def del_files(sender,instance, **kwargs):
	# for i in UploadFile.objects.all():
	up = Upload()
	up.del_files("homeslider")
	

signals.pre_delete.connect(del_files,sender=HomePage)