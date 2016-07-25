import fileinput

indexNazione = 0
indexImporto = 1
mr = {}

for line in fileinput.input():
	if(line.strip()):
		values = line.split('\t')
		nazione = str(values[indexNazione])
		importo = float(values[indexImporto])
		temp = {str(nazione) : importo}
		if nazione in mr.keys():
			mr[nazione] = mr[nazione] + importo
		else:
			mr.update(temp)

print(mr)