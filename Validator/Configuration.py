from .files_list import ListFiles
import re

class Config(object):
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
		
		val = "Valid"

		for item in files:
			try:
				test = open(item, 'r')
				read_file = test.readlines()
			except:
				continue

			regex = '(username|secret|password|hmac|access.*key)\s*[:=>]\s*[\']'
			for line in read_file:
				result = re.match(regex, line)
				if result:
					val = "Invalid"
					break
		return val