try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import xlsxwriter
data = []
opcineArr = []
opcineUrl = "https://www.izbori.ba/cik_web_api/race9_electoralunit/%22WebResult_2016MUNI_2016_9_23_16_38_25%22/1"
vjece = "https://www.izbori.ba/cik_web_api/race9_electoralunitpartyresult/%22WebResult_2016MUNI_2016_9_23_16_38_25%22/"
responseOpcine = urlopen(opcineUrl)
opcine = responseOpcine.read().decode("utf-8")
opcineData = json.loads(opcine)
#print(opcineData)
for op in opcineData:
    #print(op)
    code = op['code']
    opcinaName = op['name']
    url = vjece + code+"/1"
    response = urlopen(url)
    data1 = response.read().decode("utf-8")
    d = json.loads(data1)
    #print(d)
    d.append({'municipality':opcinaName})
    print(d)
    data.append(d)

#for i in range(1,3):
#    url = vjece + str(i)+"/1"
#    response = urlopen(url)
#    data1 = response.read().decode("utf-8")
#    d = json.loads(data1)
#    print(d)
#    data.append(d)
print(data)
workbook = xlsxwriter.Workbook('2016.xlsx')
worksheet = workbook.add_worksheet()

# Write some data headers.
bold = workbook.add_format({'bold': 1})
worksheet.write('A1', 'OPCINA', bold)
worksheet.write('B1', 'STRANKA', bold)
worksheet.write('C1', 'GLASOVI', bold)
worksheet.write('D1', 'MANDATI', bold)

# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for item in (data):
    #print(item)
    #print(item[0]['name'])
    for stranka in item:
        print(stranka)
        worksheet.write(row, col,stranka['municipality'])
        worksheet.write(row, col + 1, stranka['name'])
        worksheet.write(row, col + 2, stranka['totalVotes'])
        worksheet.write(row, col + 3, stranka['mandates'])
        row += 1

workbook.close()

#with open('data2008.json', 'wb') as outfile:
#    json.dumps(data, outfile)
