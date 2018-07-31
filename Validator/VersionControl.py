import re

class Codebase(object):
	def __init__(self, config_file):
		self.config_file = config_file+'/.git/config'
	
	def Validate_git(self):
		try:
			config_file = open(self.config_file, 'r')
		except:
			return("NoVersionControl")
		
		lines = config_file.readlines()

		for line in lines:
			match = re.match('\[remote', line)
			if match != None:
				ind = lines.index(line)
				# remote_origin_l = remote_origin.split('\n')
		url = lines[ind+1]
		url = re.split("=[' ']", url)[1]
		return url
