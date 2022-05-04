from bs4 import BeautifulSoup
import requests
import pandas as pd

startURL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(startURL)
print(page)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table')

tempList = []
rows = table.find_all('tr')
for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)


Star_Name = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(tempList)):
    Star_Name.append(tempList[i][1])
    Distance.append(tempList[i][3])
    Mass.append(tempList[i][5])
    Radius.append(tempList[i][6])

df = pd.DataFrame(list(zip(Star_Name, Distance, Mass, Radius)), columns=[
    'Star_Name', 'Distance', 'Mass', 'Radius'])
print(df)

df.to_csv('data.csv')
