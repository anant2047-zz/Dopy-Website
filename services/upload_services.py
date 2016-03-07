import zipfile,os,shutil
from django.conf import settings
#from pyunpack import Archive
import patoolib
import re

class Upload():
	"Used to manage uploaded file"
	def make_directory(self,location):
		#making desired directory if not present
		try:
			os.makedirs(location)
			print("making" + location)
		#PENDING WORK: user might enter the same service_name so we need to keep a check.That work is not done, we need to keep a check here.
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

	def merge(self,dir1,dir2,image_dir,service_name):
		path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
		if dir1 == "img":
			path, dirs, files = next(os.walk(os.path.join(path_media ,"services",service_name,image_dir,dir2)))
			
			i = 0
			while(i < len(files)):
				self.move(os.path.join(path_media,"services",service_name,image_dir,dir2,files[i]),os.path.join(path_media ,"services",service_name,image_dir,"img",files[i]))
				i+=1
			self.remove_dir(os.path.join(path_media ,"services",service_name,image_dir,dir2))
		
		else :
			path, dirs, files = next(os.walk(os.path.join(path_media,"services",service_name,image_dir,dir1)))
			
			i = 0
			while(i < len(files)):
				self.move(os.path.join(path_media,"services",service_name,image_dir,dir1,files[i]),os.path.join(path_media ,"services",service_name,image_dir,"img",files[i]))
				i+=1
			self.remove_dir(os.path.join(path_media ,"services",service_name,image_dir,dir1))



	# def del_files(self,service_name):
	# 	print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
	# 	shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
	# 	print(service_name+" Deleted Successfully")
	def del_files(self,f_service_name):
		path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
		#print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
		try:
			shutil.rmtree(os.path.join(path_media,"services",f_service_name))
			print(f_service_name+" Deleted Successfully")
			
		except Exception:
			print("Error")

	def startScript(self,service_name,panelImage,thumbnails):
		#making service_name directory
		path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
		panelImage = panelImage.split('/')[-1]
		thumbnails = thumbnails.split('/')[-1]
		panelImage = re.sub(' ', '_', panelImage)
		thumbnails = re.sub(' ', '_', thumbnails)
		self.make_directory(os.path.join(path_media ,"services",service_name ))
			#os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name ))

	
		#making service_name/panelImage directory
		self.make_directory(os.path.join(path_media,"services",service_name,"panelImages" ))
			#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages" ))		
		#uncompressing file in temporary/panelImages/panelImage source directory -> service_name/panelImages
		self.uncompressFile(os.path.join(path_media,"temporary","panelImages",panelImage),os.path.join(path_media,"services",service_name,"panelImages" ))
			#os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages" ))
		#removing uncompressed in temporary/panelImages/panelImage
		self.remove_files(os.path.join(path_media,"temporary","panelImages",panelImage))
			#os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage))


		#renaming files in service_name/panelImages/panelImage to "img"
		path, dirs, files = next(os.walk(os.path.join(path_media,"services",service_name,"panelImages")))
			#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages")))
		# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
		if len(dirs) == 2:
			self.merge(dirs[0],dirs[1],"panelImages",service_name)
		else:
			self.rename(os.path.join(path_media,"services",service_name,"panelImages",dirs[0] ),os.path.join(path_media ,"services",service_name,"panelImages","img" ))
				#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages","img" ))

		
		self.make_directory(os.path.join(path_media,"services",service_name,"thumbnails" ))
		#self.make_directory(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"thumbnails" ))
		#uncompressing file in temporary/thumbnails/thumbnails source directory -> service_name/thumbnails
		self.uncompressFile(os.path.join(path_media,"temporary","thumbnails",thumbnails),os.path.join(path_media,"services",service_name,"thumbnails" ))
		#self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"thumbnails"))
		#removing uncompressed in temporary/thumbnail/thumbnail
		self.remove_files(os.path.join(path_media,"temporary","thumbnails",thumbnails))
		#self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails))
		
		#renaming files in service_name/thumbnails/thumbnails to "img"
		path, dirs, files = next(os.walk(os.path.join(path_media,"services",service_name,"thumbnails")))
		#path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"thumbnails")))
		# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
		if len(dirs) == 2:
			self.merge(dirs[0],dirs[1],"thumbnails",service_name)
		else:
			self.rename(os.path.join(path_media,"services",service_name,"thumbnails",dirs[0] ),os.path.join(path_media ,"services",service_name,"thumbnails","img" ))
			#self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"thumbnails",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"thumbnails","img" ))





#new script

# import zipfile,os,shutil
# from django.conf import settings
# #from pyunpack import Archive
# import patoolib
# import random,time



# class Upload():
# 	"Used to manage uploaded file"
# 	def make_directory(self,location):
# 		#making desired directory if not present
# 		try:
# 			os.makedirs(location)
# 			print("making" + location)
# 		#PENDING WORK: user might enter the same service_name so we need to keep a check.That work is not done, we need to keep a check here.
# 		except OSError:
# 			if not os.path.isdir(location):
# 				raise



# 	def rename(self,old_name,new_name):
# 		os.rename(old_name,new_name)
# 		print("renaming: " + old_name + " to " + new_name)

# 	def uncompressFile(self,from_location,to_location):
# 		if from_location.endswith(".zip"):
# 			zfile = zipfile.ZipFile(from_location)
# 			zfile.extractall(to_location)
# 			print("uncompressing:" + from_location) 	

# 		elif from_location.endswith(".rar"):
# 			patoolib.extract_archive(from_location, outdir=to_location) 

# 	def remove_files(self,location):
# 		os.remove(location)
# 		print("deleting:" + location)

# 	def remove_dir(self,location):
# 		os.rmdir(location)
# 		print("deleting:" + location)
	
# 	def move(self,old,new):
# 		shutil.move(old,new)

# 	def copy(self,old,new):
# 		shutil.move(old,new)

# 	def rename(self,image_dir,service_name,dir_name):
# 		path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir_name)
# 		random.seed(time.time())
# 		for content in os.listdir(os.path.join(path)):
# 			if os.path.isfile(os.path.join(path,content)):
# 				name,extension = content.split(".")
# 				random_number = str(math.trunc(random.random()*10000000000))
# 				self.rename(os.path.join(path,content),os.path.join(path,random_number,".",extension))

# 	def merge(self,dir1,dir2,image_dir,service_name):

# 		if dir1 == "img":
# 			#renaming all file in image_dir to some random number
# 			self.rename(image_dir,service_name,dir2)
# 			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2)))
			
# 			i = 0
# 			while(i < len(files)):
# 				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,"img",files[i]))
# 				i+=1
# 			self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2))
		
# 		else :
# 			#renaming all file in image_dir to some random number
# 			self.rename(image_dir,service_name,dir1)
# 			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir1)))
			
# 			i = 0
# 			while(i < len(files)):
# 				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir1,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,"img",files[i]))
# 				i+=1
# 			self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir1))



# 	# def del_files(self,service_name):
# 	# 	print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
# 	# 	shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
# 	# 	print(service_name+" Deleted Successfully")
# 	def del_files(self,f_service_name):
# 		#print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
# 		try:
# 			shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",f_service_name))
# 			print(f_service_name+" Deleted Successfully")
			
# 		except Exception:
# 			print("Error")

# 	# 	def startScript(self,service_name):
# 	def startScript(self,service_name,panelImage,thumbnails):
# 		#making service_name directory
# 		a,b,panelImage = panelImage.split('/')
# 		c,e,thumbnails = thumbnails.split('/')
# 		print(panelImage)

# 		path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name )
# 		self.make_directory(path)

	
# 		#making service_name/panelImage directory
# 		self.make_directory(os.path.join(os.path.dirname(path,"panelImages" )))
		

# 		#transfering panelImages folder in services/panelImages
# 		temporary_path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR))	 ,"static_in_env","media_root" ,"temporary" )
# 		self.copy(os.path.join(temporary_path,"panelImages"),os.path.join(path,"panelImages"))

		
# 		path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages")))
# 		# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
# 		if len(dirs) == 2:
# 			self.merge(dirs[0],dirs[1],"panelImages",service_name)
# 		else:
# 		#renaming files in service_name/panelImages/panelImages to "img"
# 			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages","img" ))

		

# 		#making service_name/thumbnails directory
# 		self.make_directory(os.path.join(os.path.dirname(path,"thumbnails" )))
		

# 		#transfering thumbnails folder in services/thumbnails
# 		temporary_path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"temporary" )
# 		self.copy(os.path.join(temporary_path,"thumbnails"),os.path.join(path,"thumbnails"))

		
# 		path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages")))
# 		# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
# 		if len(dirs) == 2:
# 			self.merge(dirs[0],dirs[1],"thumbnails",service_name)
# 		else:
# 		#renaming files in service_name/thumbnails/thumbnails to "img"
# 			self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"panelImages","img" ))

# 		