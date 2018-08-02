import pdfkit
from PiCCE.settings import BASE_DIR
#dict_12 = {"__CBName":"Supply Chain Tracker v5","__CBFramework":"DotNet","__cb":["invalid","https://github.com/myRepo","Please push into a Github Repo"],"__dp":["valid","Requirements stored in separate files.","Please specify dependencies in separate files."],"__co":["valid","No sensitive information found in code.","Please remove configurations from codebase & include them as environment variables."],"__bs":["invalid","Coming Soon","Coming Soon"],"__brr":["valid","CI/CD configuration found","Please specify CI/CD pipeline configuration"],"__pr":["valid","Coming Soon","Coming Soon"],"__pb":["valid","Coming Soon","Coming Soon"],"__ccc":["valid","Coming Soon","Coming Soon"],"__dis":["valid","Coming Soon","Coming Soon"],"__dev":["valid","Coming Soon","Coming Soon"],"__log":["valid","Logs are displayed on STDOUT and are not written into files","Please stream logs on STDOUT or route to log engines"],"__ap":["valid","Coming Soon","Coming Soon"]}
path = BASE_DIR+'/static/template2.html'

def generate_pdf(dict_12,outfile):
	html_file = open(path,'r')
	html = html_file.read()

	for key,value in dict_12.items():
		if(key == "__CBName" or key == "__CBFramework"):
			html = html.replace(key,value)
		elif (value == "__csoon"):
			html = html.replace(key+'_',"Coming Soon.")
			html = html.replace(str(key+"i"),'')
			html = html.replace(str("__desc"+key),"Coming Soon.")
		else :
			if value[0] == "valid":
				html = html.replace(key+'_',"Validated.")
				html = html.replace(str(key+"i"),"")
				html = html.replace(str("__desc"+key),value[1])
				print(str("__desc"+key))
				print(str(key+"i"))
			else:
				html = html.replace(str(key+"i"),"Not Compliant.")
				html = html.replace(key+'_',"")
				html = html.replace(str("__desc"+key),value[2])
				print(str(key+"i"))
				print(str("__desc"+key))
	pdfkit.from_string(html,outfile+"report.pdf")