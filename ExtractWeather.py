import requests
import json
import datetime
import csv

key='c898f935e9e5c4ddc8c930f62fe499bc'
d = datetime.date(2014, 1, 1)
delta = datetime.timedelta(days=1)

with open("output3.csv",'wb') as f:
	writer = csv.writer(f, dialect='excel')
	writer.writerow(['Date', 'Max', 'Min'])
	while d<=datetime.date(2016, 1, 1):
		sdate=d.strftime('%Y-%m-%d')
		r = requests.get('https://api.darksky.net/forecast/'+key+'/43.0481,-76.1474,'+sdate+'T00:00:00')

		d2 = r.json()
		d3 = d2['daily']
		d4 = d3['data']
		d5 = d4[0]
		d6 = d5['temperatureMax']
		d7 = d5['temperatureMin']
		writer.writerow([sdate, d6, d7])
		
		d+=delta



