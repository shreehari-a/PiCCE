from .files_list import ListFiles
class BTR(object):

	def __init__(self, foldername):
		self.config_name = {
		'travis':'.travis.yml',
		'Jenkins':'',
		'circleci':'circle.yml',
		'appveyor':'',
		'teamcity':'',
		'bamboo':'',
		'gitlab':'',
		'codeship':'',
		}
		self.foldername = foldername

	def check_ci_cd(self):
		files = ListFiles(self.foldername).current_dir()
		ci_cd = 'invalid'
		l = ''
		for key,value in self.config_name.items():
			for item in files:
				if item == value:
					ci_cd = 'valid'
					l = key
					break
		return (ci_cd, key)

	