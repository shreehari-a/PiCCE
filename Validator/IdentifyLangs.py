from .files_list import ListFiles

class Identify(object):
	def __init__(self, foldername):
		self.extensions = {
			'python':'py',
			'dotnet':'cs',
		}
		self.foldername = foldername

	def language(self):
		files = ListFiles(self.foldername).recursive()
		ext = []
		for item in files:
			ext.append(item.split('.')[-1])
		language = 'No support'
		for key, value in self.extensions.items():
			for item in ext:
				if value == item:
					language = key
					break
		return language


