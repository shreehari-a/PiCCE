from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PiCCE.settings import BASE_DIR
from django.core.files.storage import default_storage
import zipfile
from .VersionControl import Codebase
# import pyping
from .LogValidation import Validator
from .IdentifyLangs import Identify
from .Depend import Dependency
from .Configuration import Config
from .BuildTestRelease import BTR
from .Backing import Back
from .genpdfv2 import generate_pdf
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
		folder_path = folder_name
		#unzipped folder
		folder_name = folder_name + '/' +filename.split('.')[0]

		#Language check
		Language = Identify(folder_name).language()

		print(Language)
		
		report_for_pdf = {}
		
		
		report_for_pdf['__CBFramework'] = report['Language'] = Language


		#version control functions
		ver = Codebase().git(folder_name+'/.git/config')
		
		report_for_pdf['__cb'] = report['Codebase'] = [ver[0],"Using remote repository "+ver[1], 'Please use some version control tool like git']
		
		#dependency function
		if Language == 'python':
			Dep = Dependency(folder_name).PythonApp()
			Dep = [Dep,'The repository has dependency file.', 'Please write the dependencies into requirements.txt']
		elif Language == 'dotnet':
			Dep = Dependency(folder_name).DotnetApp()
			Dep = [Dep,'The repository has dependency file.', 'Please write the dependencies into packages.json/packages.config']
		else:
			Dep = ["NoSupport", "NoSupport", 'NoSupport']

		print(Dep)

		report_for_pdf['__dp'] = report['Dependency'] = Dep
		#config functions
		config = Config(folder_name).check()
		config = [config, "The configurations are not stored in repository", "Please don't keep the configs in code repository. Try to keep it in environment."]
		report_for_pdf['__co'] = report['Configuration'] = config

		#build, test, release
		btr = BTR(folder_name).check_ci_cd()
		
		btr = [btr[0],"Using CI service "+btr[1], 'Please use some a CI tool like jenkins/gitlab/travisci/circleci']
		
		report_for_pdf['__brr'] = report['BuildTestRelease'] = btr
		

		#backing serverice

		res = Back(folder_name).check()

		report_for_pdf['__bs'] = report['BackingServices'] = [res, 'Backing serverice are acting as local system', 'Backing services are not acting as local services, please do modify your configurations']

		#logging functions
		if Language == 'python':
			Log = Validator(folder_name).PythonApp()
		elif Language == 'dotnet':
			Log = Validator(folder_name).DotnetApp()
		else:
			Log = "No Support"
		Log = [Log, "Logs are being written to STDOUT and are not written into files.","Logs are being written into file. Please redirect Logs to "]
		report_for_pdf['__log'] = report['Logging'] = Log
		#dependency function
		# report_to	] = ''
		print('\n')
		print(folder_path)
		print('\n')
		folder_path = folder_path.split('static')[-1]

		project_name = folder_path.split('/')[-1]
		report_for_pdf['__CBName'] = project_name
		
		print(project_name)
		folder_path = BASE_DIR + '/static'+folder_path+'/'
		print(folder_path)
		report_for_pdf['__pr'] = "__csoon" 
		report_for_pdf['__pb'] = "__csoon" 
		report_for_pdf['__ccc'] = "__csoon" 
		report_for_pdf['__dis'] = "__csoon" 
		report_for_pdf['__dev'] = "__csoon" 
		report_for_pdf['__ap'] = "__csoon" 
		
		#create a pdf file in folder_path. report is the dictionary
		generate_pdf(report_for_pdf, folder_path)



		
		return render(request, 'report.html', {'report':report, 'folder_name':'/static/ZIP/'+project_name}, )
	else:
		return render(request, 'index.html')

def Dell_Enthusiast(request):
	return render(request, 'Dell-Enthusiast.html')

def Report(request):
	return render(request, 'report.html')