import zipfile,os
from django.conf import settings

class Upload():
	"Used to manage uploaded file"
	def make_directory(self,event_name):
		#making desired directory if not present
		try:
			os.makedirs(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"events",event_name ))
			print("making " + event_name + " directory")
		#PENDING WORK: user might enter the same event_name so we need to keep a check.That work is not done, we need to keep a check here.
		except OSError:
			if not os.path.isdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"events",event_name )):
				raise
	def uncompressFile(self,storage,event_name):
		zfile = zipfile.ZipFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","Storage",storage))
		zfile.extractall(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name ))	

	def startScript(self,event_name,storage):
		print(event_name)
		print(settings.BASE_DIR)
		self.make_directory(event_name)
		self.uncompressFile(storage,event_name)
		
		



