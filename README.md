# Web scraping with Python and Selenium

Web scraping of local municipality elections data from official site of Central Election Commision of Bosnia and Herzegovina  http://izbori.ba 

Data is scraped using python and selenium web driver for chrome and saved in excel format for 2008 and 2012 year.

Website is analysed with chrome dev tools in order to understand navigation and find elements that contain data.

Python is using selenium to navigate to pages and collect data (and to handle exceptions). 

Collected data is saved in excel files 2008.xls and 2012.xls with columns: party name, municipality name, number of votes, number of mandates for every party in every municipality.