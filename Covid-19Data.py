import ssl
import csv
import bs4
import urllib
from urllib.request import  urlopen as uReq
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

#For sites that can't be opened due to Urllib blocker, use a Mozilla User agent to get access
ssl._create_default_https_context = ssl._create_unverified_context
pageRequest = Request('https://covidtracking.com/data/us-daily', headers = {'User-Agent': 'Firefox/5.0'})
htmlPage = urlopen(pageRequest).read()
page_soup = soup(htmlPage, 'html.parser')

#overarching Tbody section with list of dates and case numbers

Table = page_soup.find('table',{'class': 'bP_ff b7_ff'})#Class Id in html changes every day
dateIterator = 0

dateList = [] #List of dates
caseList = [] #List of cases
for i in range(0,236): #Iterating along the list of trs which contain the data in the overarching table
    dateList.append(Table.tbody.contents[dateIterator].contents[0].contents[1].text) #Extracts the dates
    caseList.append(Table.tbody.contents[dateIterator].contents[3].contents[1].text) #Extracts the cases
    dateIterator = dateIterator+1


#Add Dates to CSV
#Add number of cases to CSV
with open('CovidDataFile.csv','a',newline= '' ) as file:
    theWriter = csv.writer(file)
    for i in range(0,len(dateList)):
        theWriter.writerow([dateList[i]])
        theWriter.writerow([caseList[i]])



