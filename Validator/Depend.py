from .files_list import ListFiles


class Dependency(object):
	def __init__(self, folder_path):	
		self.folder_path = folder_path

# 	def Check_Presenece():

	def PythonApp(self):
		files = ListFiles(self.folder_path).current_dir()
		val = 'invalid'
		for item in files:
			if item == 'requirements.txt' or 'requirements.txt':
				val = 'valid'
		return val

	def DotnetApp(self):
		files = ListFiles(self.folder_path).recursive()
		val = 'invalid'
		for item in files:
			if item == 'packages.config' or 'packages.json' or 'package.config' or 'package.json' :
				val = 'valid'
		return val
