import requests
from bs4 import BeautifulSoup
from pandas as pd
import csv
url = 'http://gaosan.com/gaokao/265440.html'
response = requests.get(url)
content = requests.get(url).content
##print ("response headers:", response.headers)
##print ("content:", content)

soup = BeautifulSoup(content, 'html.parser', from_encoding = 'utf-8')
result = soup('table')
tables = soup.select('table')
print(tables)

df_list = []
for table in tables:
     df_list.append(pd.concat(pd.read_html(table.prettify)))
df = pd.concat(df_list)
df.to_csv
