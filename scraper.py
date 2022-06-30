import requests
import bs4
import pandas as pd


result = requests.get('https://www.worldometers.info/coronavirus/#countries')

soup = bs4.BeautifulSoup(result.text,'lxml')

cases = soup.find_all('div' ,class_= 'maincounter-number')

data = []
 
for i in cases:
    span = i.find('span')
    data.append(span.string)
 

print(data)

df = pd.DataFrame({"CoronaData": data})
 
df.index = ['Total Cases', ' Deaths', 'Recovered']

df.to_csv('data.csv')