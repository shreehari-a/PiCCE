from os import listdir
from os.path import isfile, join
import os

from .files_list import ListFiles
		

class Validator(object):
	def __init__(self, foldername):
		self.foldername = foldername

	def PythonApp(self):
		files = ListFiles(self.foldername).recursive()
		return "valid"
		pass

	def DotnetApp(self):
		onlyfiles = ListFiles(self.foldername).recursive()
		print(onlyfiles)
		file_ar = {}
		for file in onlyfiles:
			file_ar[file] = []
			f = open(file,'r',encoding="utf8")
			plist = []
			try:
				data = f.read()
			except:
				pass
			data_ar = data.split('\n')
			for line in data_ar:

				if 'new' in line and 'StreamWriter' in line:
					#print(str(file))
					if '(' in line:
						line = line.replace('(',' ')
						line = line.replace(')',' ')
					line_ar = line.split(' ')
					if('StreamWriter' in line_ar and 'log' in ''.join(line_ar)):
						#pos = line_ar.index("StreamWriter")
						
						pos = line_ar.index('StreamWriter')
						plist.append(line_ar[pos+1])
			#print(plist)
			for item in plist:
				search = [str(item)+'.WriteLine(', str(item)+'.Write(' , str(item)+'.write(', str(item)+'.writeline(' ]
				#print(search)
				if (k in data for k in search):
					file_ar[file].append("Invalid")
		flag = 0
		for key,value in file_ar.items():
		
			
			for item in value:
				if item != "Invalid":
					flag = 1
				else:
					pass
		if flag == 0:
			return "valid"
		else:
			return "invalid"

	# if 'StreamWriter' in data:
	# 	pos = data.find('StreamWriter')
	# 	print(pos)