import fileinput

indexNazione = 2
indexImporto = 6
indexDate = 4
date2016 = 20160101

def convertDate(text):
	return text.split(" ")[0].replace("-","")

for line in fileinput.input():
	values = line.split(';')
	date = convertDate(values[indexDate])
	if (int(date) >= date2016):
		nazione = values[indexNazione]
		importo = values[indexImporto]
		print('{0}\t{1}'.format(nazione, importo))