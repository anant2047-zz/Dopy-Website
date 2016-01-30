import zipfile,os,shutil
from django.conf import settings
#from pyunpack import Archive
import patoolib


class Upload():
	"Used to manage uploaded file"
	def make_directory(self,location):
		#making desired directory if not present
		try:
			os.makedirs(location)
			print("making" + location)
		#PENDING WORK: user might enter the same event_name so we need to keep a check.That work is not done, we need to keep a check here.
		except OSError:
			if not os.path.isdir(location):
				raise

	def rename(self,old_name,new_name):
		os.rename(old_name,new_name)
		print("renaming: " + old_name + " to " + new_name)

	def uncompressFile(self,from_location,to_location):
		if from_location.endswith(".zip"):
			zfile = zipfile.ZipFile(from_location)
			zfile.extractall(to_location)
			print("uncompressing:" + from_location) 	

		elif from_location.endswith(".rar"):
			patoolib.extract_archive(from_location, outdir=to_location) 

	def remove_files(self,location):
		os.remove(location)
		print("deleting:" + location)

	def remove_dir(self,location):
		os.rmdir(location)
		print("deleting:" + location)
	
	def move(self,old,new):
		shutil.move(old,new)

	def merge(self,dir1,dir2,image_dir,event_name):
		if dir1 == "img":
			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir2)))
			
			i = 0
			while(i < len(files)):
				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir2,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,"img",files[i]))
				i+=1
			self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir2))
		
		else :
			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir1)))
			
			i = 0
			while(i < len(files)):
				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir1,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,"img",files[i]))
				i+=1
			self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir1))



	# def indexImages(self,location):
	# 	i = 1
	# 	for f in os.listdir(location):
	# 		list = f.split(".")
	# 		print(f)
	# 		self.rename(os.path.join(location , f),os.path.join(location , str(i) + "." + list[ len(list) - 1 ]))
	# 		i+=1

	def startScript(self,event_name,sliderImage,panelImage,storage,thumbnails):
		#making event_name directory
		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name ))
		
		#making event_name/sliderImage directory
		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages" ))
		#uncompressing file in temporary/sliderImages/sliderImage source directory -> event_name/sliderImages
		self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","sliderImages",sliderImage),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages"))
		#removing uncompressed in temporary/sliderImages/sliderImage
		self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","sliderImages",sliderImage))
		
		#renaming files in event_name/sliderImages/sliderImage to "img"
		path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")))
		if len(dirs) == 2:
			self.merge(dirs[0],dirs[1],"sliderImages",event_name)
		else:
			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages","img" ))


	
		#making event_name/panelImage directory
		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages" ))		
		#uncompressing file in temporary/panelImages/panelImage source directory -> event_name/panelImages
		self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages" ))
		#removing uncompressed in temporary/panelImages/panelImage
		self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage))


		#renaming files in event_name/panelImages/panelImage to "img"
		path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages")))
		# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")):
		if len(dirs) == 2:
			self.merge(dirs[0],dirs[1],"panelImages",event_name)
		else:
			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages","img" ))

		#making event_name/storage directory
		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"storage" ))		


		#making event_name/thumbnails directory
		self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails" ))
		#uncompressing file in temporary/thumbnails/thumbnails source directory -> event_name/thumbnails
		self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails"))
		#removing uncompressed in temporary/thumbnail/thumbnail
		self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails))
		
		#renaming files in event_name/thumbnails/thumbnails to "img"
		path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails")))
		# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")):
		if len(dirs) == 2:
			self.merge(dirs[0],dirs[1],"thumbnails",event_name)
		else:
			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails","img" ))


		#renaming compressed file in event_name/storage/storage
		for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"temporary","storage")):
			if f.endswith(".zip"):
				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"temporary","storage",f ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"storage",event_name + ".zip" ))
			elif f.endswith(".rar"):
				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"temporary","storage",f ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"storage",event_name + ".rar" ))		 		
		

		# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"temporary","home_slider")):
		# 	if f.endswith(".zip"):
		# 		self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"temporary","home_slider",f ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"home_slider","home_slider" + ".zip" ))
		# 	elif f.endswith(".rar"):
		# 		self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"temporary","home_slider",f ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"home_slider","home_slider" + ".rar" ))

		# self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","home_slider",home_slider),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"home_slider" ))		 		
		# self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","home_slider",home_slider))
