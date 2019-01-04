from selenium import webdriver
import xlsxwriter
import json
import http.client
def checkUrl(url):
    conn = http.client.HTTPConnection("www.izbori.ba")
    conn.request("GET", url)
    r1 = conn.getresponse()
    return r1.status < 400
chrome_path = r"chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
data = []

for i in range(1,201):
    locationNumber = str(i).zfill(3)
    page = "http://www.izbori.ba/Mandati27102008/ShowMunicipality.asp?MunicipalityCode="+ locationNumber
    url ="/Mandati27102008/ShowMunicipality.asp?MunicipalityCode="+ locationNumber
    print(page)
    ret = checkUrl(url)
    if ret:
        driver.get(page)
        opcina = driver.find_element_by_xpath("""/html/body/table[2]/tbody/tr[1]/td/table[1]/tbody/tr/td[1]/span/strong""")
        if opcina:
            print(opcina.text)
            for j in range(6,600,3):
                #print(j)
                try:
                    stranka = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[3]/table[1]/tbody/tr["+str(j)+"]")
                    if(stranka):
                        #print(stranka.text)
                        ns_arr = stranka.text.splitlines()
                        #print (ns_arr)
                        row = []
                        row.append(opcina.text)
                        row.append(ns_arr[2])
                        row.append(ns_arr[3])
                        row.append(ns_arr[5])
                        data.append(row)
                except:
                    break
#print(data)
workbook = xlsxwriter.Workbook('2008.xlsx')
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
for opcina,stranka,glas,manda in (data):
    worksheet.write(row, col,opcina)
    worksheet.write(row, col + 1, stranka)
    worksheet.write(row, col + 2, int(glas.replace(",","")))
    worksheet.write(row, col + 3, int(manda.replace(",","")))
    row += 1

workbook.close()

with open('data2008.json', 'wb') as outfile:
    json.dumps(data, outfile)
