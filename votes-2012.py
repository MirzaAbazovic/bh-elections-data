from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import xlsxwriter
import json
import http.client
def checkUrl(url):
    conn = http.client.HTTPConnection("www.izbori.ba")
    conn.request("GET", url)
    r1 = conn.getresponse()
    #print(r1.status)
    return r1.status < 400 #and r1.status != 302
chrome_path = r"chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
#driver.implicitly_wait(2)
data = []
for i in range(1,201):
    locationNumber = str(i).zfill(3)
    page = "http://izbori.ba/Rezultati/RezultatiPotvrdjeni/files/Glavni_report_trka_9_opstina_"+ str(i).zfill(3)+".html"
    url ="/Rezultati/RezultatiPotvrdjeni/files/Glavni_report_trka_9_opstina_"+ locationNumber
    print(page)
    ret = checkUrl(url)
    #print(ret)
    if ret:
        driver.get(page)
        #opcina = driver.find_element_by_xpath("""//*[@id="ctl00_navigationContentPlaceHolder_tdNavigation"]/span[3]""")
        try:
            opcina = driver.find_element_by_xpath("""//*[contains(text(), 'Kod opštine')]""")
            print(driver.current_url)
            if opcina:
                print(opcina.text)
                for j in range(1,50,1):
                    #print("j="+str(j))
                    try:
                        #//*[@id="ctl00_rightContentPlaceHolder_tabChartTable_tabTable"]/div/table/tbody/tr[8]
                        xpath ="""//*[@id="ctl00_rightContentPlaceHolder_tabChartTable_tabTable"]/div/table/tbody/tr["""+str(j)+"""]"""
                        #print(xpath)
                        stranka = driver.find_element_by_xpath(xpath)
                        if(stranka):
                            #print(stranka.text)
                            ns_arr = stranka.text.splitlines()
                            results = ns_arr[2].split()                       
                            row = []
                            row.append(opcina.text.replace("Kod opštine: ",""))
                            row.append(ns_arr[1])
                            row.append(results[0])
                            row.append(results[6])
                            #print(row)
                            data.append(row)
                    except:
                        #print("BREAK j="+str(j))
                        next
        except:
            next
#print(data)
workbook = xlsxwriter.Workbook('2012.xlsx')
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

#with open('data2008.json', 'wb') as outfile:
#    json.dumps(data, outfile)
