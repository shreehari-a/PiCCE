import re

class Codebase(object):
	def __init__(self):
		pass

	def git(self, config_file):
		try:
			config_file = open(config_file, 'r')
		except:
			return("invalid", '')
		
		lines = config_file.readlines()

		for line in lines:
			match = re.match('\[remote', line)
			if match != None:
				ind = lines.index(line)
				# remote_origin_l = remote_origin.split('\n')
		url = lines[ind+1]
		url = re.split("=[' ']", url)[1]
		return ('valid',url.rstrip('\r\n'))

	def svn():
		pass

	def mercurial():
		pass

	def tfs():
		pass