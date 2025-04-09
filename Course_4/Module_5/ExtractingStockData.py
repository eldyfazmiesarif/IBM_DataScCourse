import pandas as pd
import requests
from bs4 import BeautifulSoup

# First Example



url1 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

htmldata1 = requests.get(url1).text
parsed_htmldata1 = BeautifulSoup(htmldata1,'html.parser')


print(parsed_htmldata1.title.text)
"""
print(parsed_htmldata1.find("tbody").find('tr'))
print()
print(parsed_htmldata1.find("tbody").find('tr').find("td"))
print()
print(parsed_htmldata1.find("tbody").find('tr').find_all("td"))
"""

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
netflixHTML_tr = parsed_htmldata1.find("tbody").find_all('tr')

for row in netflixHTML_tr:
    col_data = row.find_all("td")
    Date = col_data[0].text
    Open = col_data[1].text
    High = col_data[2].text
    Low = col_data[3].text
    Close =col_data[4].text
    adjClose = col_data[5].text
    Volume = col_data[6].text
    
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[Date], "Open":[Open], "High":[High], "Low":[Low], "Close":[Close], "Adj Close":[adjClose], "Volume":[Volume]})], ignore_index=True)    
    
print(netflix_data.head())
print(netflix_data.tail())


# Second Example

url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data2 = requests.get(url2).text
parsedHTML_data2 = BeautifulSoup(html_data2,'html.parser')

title = parsedHTML_data2.title
print()
print()
print(title.text)

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in parsedHTML_data2.find("tbody").find_all("tr"):
    col = row.find_all("td")
    Date = col[0].text
    Open = col[1].text
    High = col[2].text
    Low = col[3].text
    Close =col[4].text
    adjClose = col[5].text
    Volume = col[6].text
    
    amazon_data = pd.concat([amazon_data,pd.DataFrame({"Date":[Date], "Open":[Open], "High":[High], "Low":[Low], "Close":[Close], "Adj Close":[adjClose], "Volume":[Volume]})], ignore_index=True)    

print(amazon_data.head())
print(amazon_data.tail())