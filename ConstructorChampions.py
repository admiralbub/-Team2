
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.formula1-dictionary.net/driver_constructor_champ.html")
soup = BeautifulSoup(html, "html.parser")
table_construct = soup.findAll("table", {"width":"620"})[0]
rows = table_construct.findAll("tr")

with open("C:/Users/artem/Desktop/Parcing/Team2/driver_construct.csv", "wt+", newline="") as f: #change the file paths to your own
    writer = csv.writer(f)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)