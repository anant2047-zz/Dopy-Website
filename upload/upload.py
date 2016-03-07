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
		#PENDING WORK: user might enter the same event_name so we need to keep a check.That work is not done, we need to keep a check here.
		except OSError:
			if not os.path.isdir(location):
				raise



	def rename(self,old_name,new_name):
		print("renaming: " + old_name + " to " + new_name)
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
		path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
		if dir1 == "img":
			path, dirs, files = next(os.walk(os.path.join(path_media ,"events",event_name,image_dir,dir2)))
			
			i = 0
			while(i < len(files)):
				self.move(os.path.join(path_media,"events",event_name,image_dir,dir2,files[i]),os.path.join(path_media ,"events",event_name,image_dir,"img",files[i]))
				i+=1
			self.remove_dir(os.path.join(path_media ,"events",event_name,image_dir,dir2))
		
		else :
			path, dirs, files = next(os.walk(os.path.join(path_media ,"events",event_name,image_dir,dir1)))
			
			i = 0
			while(i < len(files)):
				self.move(os.path.join(path_media ,"events",event_name,image_dir,dir1,files[i]),os.path.join(path_media,"events",event_name,image_dir,"img",files[i]))
				i+=1
			self.remove_dir(os.path.join(path_media ,"events",event_name,image_dir,dir1))



	# def del_files(self,event_name):
	# 	print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name))
	# 	shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name))
	# 	print(event_name+" Deleted Successfully")
	def del_files(self,f_event_name):
		path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
		#print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name))
		print f_event_name
		try:
			shutil.rmtree(os.path.join(path_media,"events",f_event_name))
			print(f_event_name+" Deleted Successfully")
			
		except "Exception":
			print("Error")

	def startScript(self,event_name,panelImage,thumbnails):
		path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
		panelImage = re.sub(' ', '_', panelImage)
		thumbnails = re.sub(' ', '_', thumbnails)
		# print thumbnails
		# print panelImage
		# print panelImage_without_space
		# print thumbnails_without_space
		# print os.path.join(path_media,"temporary","panelImages",panelImage)
		# print os.path.join(path_media,"temporary","thumbnails",thumbnails)
		# self.rename(os.path.join(path_media,"temporary","panelImages",panelImage),os.path.join(path_media,"temporary","panelImages",panelImage_without_space))
		# self.rename(os.path.join(path_media,"temporary","thumbnails",thumbnails),os.path.join(path_media,"temporary","panelImages",thumbnails_without_space))
		

		try:
		#making event_name directory
			self.make_directory(os.path.join(path_media ,"events",event_name ))

		
			#making event_name/panelImage directory
			self.make_directory(os.path.join(path_media ,"events",event_name,"panelImages" ))		
			#uncompressing file in temporary/panelImages/panelImage source directory -> event_name/panelImages
			self.uncompressFile(os.path.join(path_media,"temporary","panelImages",panelImage),os.path.join(path_media ,"events",event_name,"panelImages" ))
			#removing uncompressed in temporary/panelImages/panelImage
			self.remove_files(os.path.join(path_media,"temporary","panelImages",panelImage))


			#renaming files in event_name/panelImages/panelImage to "img"
			path, dirs, files = next(os.walk(os.path.join(path_media ,"events",event_name,"panelImages")))
			# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")):
			if len(dirs) == 2:
				self.merge(dirs[0],dirs[1],"panelImages",event_name)
			else:
				self.rename(os.path.join(path_media ,"events",event_name,"panelImages",dirs[0] ),os.path.join(path_media,"events",event_name,"panelImages","img" ))

			self.make_directory(os.path.join(path_media,"events",event_name,"thumbnails" ))
			#uncompressing file in temporary/thumbnails/thumbnails source directory -> event_name/thumbnails
			self.uncompressFile(os.path.join(path_media,"temporary","thumbnails",thumbnails),os.path.join(path_media ,"events",event_name,"thumbnails"))
			#removing uncompressed in temporary/thumbnail/thumbnail
			self.remove_files(os.path.join(path_media,"temporary","thumbnails",thumbnails))
			
			#renaming files in event_name/thumbnails/thumbnails to "img"
			path, dirs, files = next(os.walk(os.path.join(path_media ,"events",event_name,"thumbnails")))
			# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")):
			if len(dirs) == 2:
				self.merge(dirs[0],dirs[1],"thumbnails",event_name)
			else:
				self.rename(os.path.join(path_media,"events",event_name,"thumbnails",dirs[0] ),os.path.join(path_media ,"events",event_name,"thumbnails","img" ))
		except "Exception":
			print("Error")



#new script

# import zipfile,os,shutil
# from django.conf import settings
# #from pyunpack import Archive
# import patoolib


# class Upload():
# 	"Used to manage uploaded file"
# 	def make_directory(self,location):
# 		#making desired directory if not present
# 		try:
# 			os.makedirs(location)
# 			print("making" + location)
# 		#PENDING WORK: user might enter the same event_name so we need to keep a check.That work is not done, we need to keep a check here.
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

# 	def rename(self,image_dir,event_name,dir_name):
# 		path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",event_name,image_dir,dir_name)
# 		random.seed(time.time())
# 		for content in os.listdir(os.path.join(path)):
# 			if os.path.isfile(os.path.join(path,content)):
# 				name,extension = content.split(".")
# 				random_number = str(math.trunc(random.random()*10000000000))
# 				self.rename(os.path.join(path,content),os.path.join(path,random_number,".",extension))


# 	def merge(self,dir1,dir2,image_dir,event_name):
# 		if dir1 == "img":
# 			#renaming all file in image_dir to some random number
# 			self.rename(image_dir,event_name,dir2)
# 			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir2)))
			
# 			i = 0
# 			while(i < len(files)):
# 				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir2,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,"img",files[i]))
# 				i+=1
# 			self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir2))
		
# 		else :
# 			#renaming all file in image_dir to some random number
# 			self.rename(image_dir,event_name,dir1)
# 			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir1)))
			
# 			i = 0
# 			while(i < len(files)):
# 				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir1,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,"img",files[i]))
# 				i+=1
# 			self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,image_dir,dir1))



# 	# def del_files(self,event_name):
# 	# 	print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name))
# 	# 	shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name))
# 	# 	print(event_name+" Deleted Successfully")
# 	def del_files(self,f_event_name):
# 		#print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name))
# 		try:
# 			shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",f_event_name))
# 			print(f_event_name+" Deleted Successfully")
			
# 		except "Exception":
# 			print("Error")

# 	def startScript(self,event_name,panelImage,thumbnails):
# 		try:
# 			#making event_name directory
# 			path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"events",event_name )
# 			self.make_directory(path)

		
# 			#making event_name/panelImage directory
# 			self.make_directory(os.path.join(path,"panelImages" ))		
			
# 			#transfering panelImages folder in services/panelImages
# 			temporary_path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR))	 ,"static_in_env","media_root" ,"temporary" )
# 			self.copy(os.path.join(temporary_path,"panelImages"),os.path.join(path,"panelImages"))

# 			#renaming files in event_name/panelImages/panelImage to "img"
# 			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages")))
# 			# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")):
# 			if len(dirs) == 2:
# 				self.merge(dirs[0],dirs[1],"panelImages",event_name)
# 			else:
# 				self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"panelImages","img" ))



# 			#making event_name/thumbnails directory
# 			self.make_directory(os.path.join(path,"thumbnails" ))		
			
# 			#transfering panelImages folder in services/panelImages
# 			temporary_path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR))	 ,"static_in_env","media_root" ,"temporary" )
# 			self.copy(os.path.join(temporary_path,"thumbnails"),os.path.join(path,"thumbnails"))

# 			#renaming files in event_name/panelImages/panelImage to "img"
# 			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails")))
# 			# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"sliderImages")):
# 			if len(dirs) == 2:
# 				self.merge(dirs[0],dirs[1],"thumbnails",event_name)
# 			else:
# 				self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"events",event_name,"thumbnails","img" ))

# 		except "Exception":
# 			print("Error")