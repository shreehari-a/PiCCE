import os

class ListFiles(object):

	def __init__(self, foldername):
		self.foldername = foldername

	def recursive(self):
		file_list = []
		
		for root, dirs, files in os.walk(self.foldername, topdown=False):
			for name in files:
				item = os.path.join(root, name)
				file_list.append(item)
				
		return file_list

	def current_dir(self):
		file_list = [f for f in os.listdir(self.foldername) ]
		return file_list