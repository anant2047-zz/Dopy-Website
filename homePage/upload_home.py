try:
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
			shutil.rmtree(location)
			print("deleting:" + location)
		
		def move(self,old,new):
			shutil.move(old,new)

		def merge(self,dir1,dir2,image_dir,service_name):
			path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )

			if dir1 == "img":
				path, dirs, files = next(os.walk(os.path.join(path_media,service_name,image_dir,dir2)))
					#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2)))
				
				i = 0
				while(i < len(files)):
					self.move(os.path.join(path_media,service_name,image_dir,dir2,files[i]),os.path.join(path_media,service_name,image_dir,"img",files[i]))
						#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,"img",files[i]))
					i+=1
				self.remove_dir(os.path.join(path_media,service_name,image_dir,dir2))
					#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2))
			
			else :
				path, dirs, files = next(os.walk(os.path.join(path_media,service_name,image_dir,dir1)))			
				#path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir1)))
				
				i = 0
				while(i < len(files)):
					self.move(os.path.join(path_media,service_name,image_dir,dir1,files[i]),os.path.join(path_media,service_name,image_dir,"img",files[i]))				
					#self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir1,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,"img",files[i]))
					i+=1
				self.remove_dir(os.path.join(path_media,service_name,image_dir,dir1))
				# self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir1))



		# def del_files(self,service_name):
		# 	print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
		# 	shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
		# 	print(service_name+" Deleted Successfully")
		def del_files(self,f_service_name):
			path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
			#print(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,"services",service_name))
			try:
				shutil.rmtree(os.path.join(path_media,"homepage","sliderImages","img"))
				shutil.rmtree(os.path.join(path_media,"homepage","thumbnails","img"))
				self.make_directory(os.path.join(path_media,"homepage","thumbnails","img"))
				self.make_directory(os.path.join(path_media,"homepage","sliderImages","img"))
					#os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,f_service_name))
				print(f_service_name+" Deleted Successfully")
				
			except "Exception":
				print("Error")

		def startScript(self,sliderImage,thumbnails):
			#making service_name directory
			sliderImage = sliderImage.split('/')[-1]
			thumbnails = thumbnails.split('/')[-1]
			sliderImage = re.sub(' ', '_', sliderImage)
			thumbnails = re.sub(' ', '_', thumbnails)
			#print(panelImage)
			path_media = os.path.join(os.path.dirname(os.path.dirname(os.path.join(settings.BASE_DIR))), "dopy_media" )
			
			#deleting homepage/image folder
			self.remove_dir(os.path.join(path_media,"homepage","sliderImages","img"))
			print os.path.join(path_media,"homepage","sliderImages","img")
			self.remove_dir(os.path.join(path_media,"homepage","thumbnails","img"))

			#making service_name/sliderImage directory
			
			#uncompressing file in temporary/sliderImages/sliderImage source directory -> service_name/sliderImages
			self.uncompressFile(os.path.join(path_media,"temporary","sliderImages",sliderImage),os.path.join(path_media,"homepage","sliderImages"))
				#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage),
				#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages" ))
			#removing uncompressed in temporary/sliderImages/sliderImage
			self.remove_files(os.path.join(path_media,"temporary","sliderImages",sliderImage))
				#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage))


			#renaming files in service_name/sliderImages/sliderImage to "img"
			# path, dirs, files = next(os.walk(os.path.join(path_media,"homepage","sliderImages")))
				#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages")))
			# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
			# if len(dirs) == 2:

			# 	self.merge(dirs[0],dirs[1],"sliderImages","homepage")
			# else:
			
			path, dirs, files = next(os.walk(os.path.join(path_media,"homepage","sliderImages")))
			#self.rename(os.path.join(path_media,"homepage","thumbnails",dirs[0] ),os.path.join(path_media,"homepage","thumbnails","img" ))
			self.rename(os.path.join(path_media,"homepage","sliderImages",dirs[0] ),os.path.join(path_media,"homepage","sliderImages","img" ))
					#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages","img" ))


			# #uncompressing file in temporary/panelImages/panelImage source directory -> service_name/panelImages
			# self.uncompressFile(os.path.join(path_media,"temporary","thumbnails",thumbnails),os.path.join(path_media,"homepage","thumbnails"))
			# #self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails" ))
			# #removing uncompressed in temporary/panelImages/panelImage
			# self.remove_files(os.path.join(path_media,"temporary","thumbnails",thumbnails))
			# #self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails))


			# #renaming files in service_name/panelImages/panelImage to "img"
			# #path, dirs, files = next(os.walk(os.path.join(path_media,"homepage","thumbnails")))
			# #path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails")))
			# # for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
			# # if len(dirs) == 2:
			# # 	self.merge(dirs[0],dirs[1],"thumbnails","homepage")
			# # else:
			# thumbnails,extension = thumbnails.split(".")
			# self.rename(os.path.join(path_media,"homepage","thumbnails",thumbnails ),os.path.join(path_media,"homepage","thumbnails","img" ))			
			# 	#self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails","img" ))

			#uncompressing file in temporary/sliderImages/sliderImage source directory -> service_name/sliderImages
			self.uncompressFile(os.path.join(path_media,"temporary","thumbnails",thumbnails),os.path.join(path_media,"homepage","thumbnails"))
				#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage),
				#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages" ))
			#removing uncompressed in temporary/sliderImages/sliderImage
			self.remove_files(os.path.join(path_media,"temporary","thumbnails",thumbnails))
				#os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage))


			#renaming files in service_name/sliderImages/sliderImage to "img"
			# path, dirs, files = next(os.walk(os.path.join(path_media,"homepage","sliderImages")))
				#os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages")))
			# for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
			# if len(dirs) == 2:

			# 	self.merge(dirs[0],dirs[1],"sliderImages","homepage")
			# else:
		
			path, dirs, files = next(os.walk(os.path.join(path_media,"homepage","thumbnails")))
			self.rename(os.path.join(path_media,"homepage","thumbnails",dirs[0] ),os.path.join(path_media,"homepage","thumbnails","img" ))

	# 		




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

	# 	def merge(self,dir1,dir2,image_dir,service_name):
	# 		if dir1 == "img":
	# 			path, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2)))
				
	# 			i = 0
	# 			while(i < len(files)):
	# 				self.move(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2,files[i]),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,"img",files[i]))
	# 				i+=1
	# 			self.remove_dir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,image_dir,dir2))
			
	# 		else :
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
	# 			shutil.rmtree(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) ,"static_in_env","media_root" ,f_service_name))
	# 			print(f_service_name+" Deleted Successfully")
				
	# 		except "Exception":
	# 			print("Error")

	# 	def transfer(str,path_temporary,path):
	# 		for content in os.listdir(os.path.join(path_temporary,str)):
	# 			if os.path.isfile(os.path.join(path_temporary,str, content)):
	# 					self.move(os.path.join(path_temporary,str, content),os.path.join(path,str,img))


	# 	# will be called as ---->
	# 	# def startSript(self)
	# 	def startScript(self,sliderImage,thumbnails):
	# 		#making service_name directory
	# 		a,b,sliderImage = sliderImage.split('/')
	# 		c,e,thumbnails = thumbnails.split('/')		
	# 		random.seed(time.time())
			
	# 		path = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage")
			
	# 		#deleting everything in sliderimages and thumbnails
	# 		for content in os.listdir(os.path.join(path,"sliderImages")):		
	# 			self.del_files(os.path.join(path,"sliderImages",content))
			
	# 		for content in os.listdir(os.path.join(path,"thumbnails")):		
	# 			self.del_files(os.path.join(path,"thumbnails",content))

	# 		#creating img folder in sliderimage and thumbnails
	# 		self.make_directory(os.path.join(path,"sliderImages",img))
	# 		self.make_directory(os.path.join(path,"thumbnails",img))


	# 		#transfering images from temporary folder to desired folders
	# 		path_temporary = os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"temporary")
	# 		self.transfer("sliderImages",path_temporary,path)
	# 		self.transfer("thumbnails",path_temporary,path)      



			#random_folder =  random.random()
		
			#making service_name/panelImage directory
					
			#uncompressing file in temporary/panelImages/panelImage source directory -> service_name/panelImages
			#self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages" ))
			#removing uncompressed in temporary/panelImages/panelImage
			#self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","panelImages",panelImage))



			# #renaming files in service_name/panelImages/panelImage to "img"
			# path1, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages")))
			# # for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
			# if len(dirs) == 2:
			# 	self.merge(dirs[0],dirs[1],"sliderImages",homepage)
			# else:
			# 	self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","sliderImages","img" ))


			#uncompressing file in temporary/panelImages/panelImage source directory -> service_name/panelImages
			# self.uncompressFile(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails" ))
			# #removing uncompressed in temporary/panelImages/panelImage
			# self.remove_files(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)) , "static_in_env","media_root","temporary","thumbnails",thumbnails))


			# #renaming files in service_name/panelImages/panelImage to "img"
			# path2, dirs, files = next(os.walk(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails")))
			# # for f in os.listdir(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"services",service_name,"sliderImages")):
			# if len(dirs) == 2:
			# 	self.merge(dirs[0],dirs[1],"thumbnails",homepage)
			# else:
			# 	self.rename(os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails",dirs[0] ),os.path.join(os.path.dirname(os.path.join(settings.BASE_DIR)), "static_in_env","media_root" ,"homepage","thumbnails","img" ))
except Exception as e:
		print("Error in upload_home.py")
		print(e)

