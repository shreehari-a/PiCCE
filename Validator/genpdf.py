import pdfkit
dict_12 = {"__cb":"valid","__dp":"valid","__co":"valid","__bs":"invalid","__brr":"valid","__pr":"valid","__pb":"valid","__co":"valid","__di":"valid","__dev":"valid","__log":"valid","__ap":"valid"}
# file_html = open('pdf.html','w')

# str_html = file_html.read()
# #print(str_html)
# for key, value in dict_12.items():
# 	str_html = str_html.replace(key,value)
#print(str_html)

pdfkit.from_string(dict_12,'report.pdf')