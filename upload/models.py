from django.db import models
from django.db.models.signals import pre_delete
from django.db.models import signals #for connect (Method 2)
# from django.dispatch import receiver #for receiver decorator(Method 1)
from .upload import Upload
import os

class UploadFile(models.Model):
	event_name=models.CharField(max_length=120, blank=False, null=False)
	sliderImages = models.FileField(upload_to='temporary/sliderImages/', blank=False, null=False)
	panelImages = models.FileField(upload_to='temporary/panelImages/', blank=False, null=False)
	storage = models.FileField(upload_to='temporary/storage/', blank=False, null=False)
	thumbnails = models.FileField(upload_to='temporary/thumbnails',blank=True,null=False)
	home_slider = models.FileField(upload_to='home_slider',blank=True,null=False)
	description = models.CharField(max_length=200,blank=True)
	

	def __str__(self):
		return os.path.basename(self.storage.name)
		

def delete_files(sender,instance, **kwargs):
	# for i in UploadFile.objects.all():
	up = Upload()
	up.del_files(instance.event_name)

signals.pre_delete.connect(delete_files,sender=UploadFile)


