import zipfile,os,shutil
from django.conf import settings

class Upload():
	"Used to manage uploaded file"
	def make_directory(self,location):
		#making desired directory if not present
		try:
			print("asdafd")
			os.makedirs(location)
			print("making" + location)
		#PENDING WORK: user might enter the same event_name so we need to keep a check.That work is not done, we need to keep a check here.
		except OSError:
			if not os.path.isdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"events",event_name )):
				raise

	def uncompressFile(self,from_location,to_location):
		zfile = zipfile.ZipFile(from_location)
		zfile.extractall(to_location)
		print("uncompressing:" + from_location) 	

	def remove_files(self,location):
		os.remove(location)
		print("deleting:" + location)

	def rename(self,old_name,new_name):
		os.rename(old_name,new_name)
		print("renaming: " + old_name + " to " + new_name)

	def move(self,old,new):
		shutil.move(old,new)

	def startScript(self,event_name,sliderImage,panelImage,storage):
		
		print(event_name)
		print(settings.BASE_DIR)
		print(sliderImage)
		print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","events","sliderImages",sliderImage))
		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name ))
		
		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages" ))
		self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","events","sliderImages",sliderImage),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages"))
		self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","events","sliderImages",sliderImage))

		for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")):
			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages",f ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages","img" ))

		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages" ))		
		self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","events","panelImages",panelImage),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages" ))
		self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","events","panelImages",panelImage))
		
		for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages")):
			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages",f ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages","img" ))
		#self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages",panelImage ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages","img" ))

		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"storage" ))		
		# self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","events","storage",storage),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"storage" ))
		# self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","events","storage",storage))

		for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events","storage")):
			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events","storage",f ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"storage",event_name + ".zip" ))
		 	#self.move(os.path.join(os.path.dirname(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)))) , "static_in_env","media_root","events","storage",f),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"storage",event_name + ".zip"))