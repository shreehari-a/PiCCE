from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PiCCE.settings import BASE_DIR
from django.core.files.storage import default_storage
import zipfile
from .VersionControl import Codebase
# import pyping
from .LogValidation import Validator
# Create your views here.
ZIP_SAVE_PATH = BASE_DIR + '/static/ZIP/'
def index(request):
	return render(request, 'index.html')

def MasterControl(request):
	return render(request, 'MasterControl.html')


@csrf_exempt 
def Upload(request):
	if request.method == 'POST':
		print('hello')
		report = {}
		repo = request.FILES['fileToUpload']
		# filename = repo.filename
		filename = repo.name
		filepath = ZIP_SAVE_PATH + filename
		temp = repo.read()

		with open(filepath,'wb') as f:
			f.write(temp)
		
		#unzip function
		zip_ref = zipfile.ZipFile(filepath, 'r')
		folder_name = filepath.split('.')[0]
		zip_ref.extractall(folder_name)
		zip_ref.close()
		
		#git_version control functions
		folder_name = folder_name + '/' +filename.split('.')[0]
		print(folder_name)
	
		ver = Codebase(folder_name)
		
		ver_res = ver.Validate_git()
		report['Codebase'] = ver_res.rstrip('\r\n')
		print(ver_res)
		
		#goes to LogValidation.py
		Log = Validator(folder_name)
		test = Log.Dotnet_Log()
		
		report['Logging'] = test
		#dependency function
		
		return render(request, 'report.html', {'report':report})

	else:
		return render(request, 'index.html')

def Dell_Enthusiast(request):
	return render(request, 'Dell-Enthusiast.html')

def Report(request):
	return render(request, 'report.html')