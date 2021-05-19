
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.formula1-dictionary.net/driver_constructor_champ.html")
soup = BeautifulSoup(html, "html.parser")
table_rechold = soup.findAll("table", {"class":"slova_12"})[0]
rows = table_rechold.findAll("tr")

with open("C:/Users/artem/Desktop/Parcing/Team2/recordholders.csv", "wt+", newline="") as f: #change the file paths to your own
    writer = csv.writer(f)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)