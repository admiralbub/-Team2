import requests
import csv
from bs4 import BeautifulSoup

url = 'http://www.formula1-dictionary.net/drivers_all_time_list.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name = soup.find_all('td', class_='excel6')
country = soup.find_all('td', {"width":"99"})
championships = soup.find_all('td', {"width":"125"})

entries = soup.find_all('td', {"width":"74"})
points = soup.find_all('td', {"width":"110"})


def csv_read(data):
    with open("C:/Users/artem/Desktop/Parcing/driver.csv",  "wt+", newline="",encoding='utf-8') as file: #change to your file path drivers.csv
        writer = csv.writer(file)
        writer.writerow((data['ID'], data['Name'], data['Country'], data['Championships'], data['Entries'], data['Points']))

for i in range(0, len(name)):
    
    data = {'ID': str(i+1),
            'Name': name[i].text,
            'Country':country[i].text,
            'Championships':championships[i].text,
            'Entries':entries[i].text,
            'Points':points[i].text}
    csv_read(data)
   
print("Parsing was successful \n Result is found driver.csv")
    