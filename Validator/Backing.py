from .files_list import ListFiles
import re
from . import api_key_detect
class Back(object):
	def __init__(self, foldername):
		self.foldername = foldername 

	def check(self):
		files = ListFiles(self.foldername).recursive()
		req_files = []
		for item in files:
			# print(item.split('.')[-1])
			if item.split('.')[-1] == 'py':
				req_files.append(item)
			if item.split('.')[-1] == 'cs':
				req_files.append(item)
		
		val = "invalid"

		#url detection in py files
		for item in req_files:
			try:
				test = open(item, 'r')
				read_file = test.readlines()
			except:
				continue
			
			regex = '^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$'
	
			for line in read_file:
				result = re.match(regex, line)
				if result:
					val = "valid"
					break

		# api keys
		# res = api_key_detect.scan_dir(self.foldername)
		# if res[0] == True:
		# 	val = 'valid'
		# else:
		# 	val = 'invalid'
		return val

