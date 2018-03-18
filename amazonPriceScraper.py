# Amazon Price Scraper

import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

# noinspection PyBroadException
def search(url):
    # Mando richiesta http al server interessato
    r = requests.get(url)

    # Parso l'html
    soup = BeautifulSoup(r.text, "html.parser")

    # print(soup.prettify())

    # Trovo prezzo e nome
    try:
        price = soup.find("span", {"id": "priceblock_ourprice"})
        price_text = price.text
    except:
        try:
            price = soup.find("span", {"class": "a-color-price"})
            price_text = price.text
        except:
            print(url, "non disponibile")
            return
    name = soup.find("span", {"id": "productTitle"})
    # Stampo prezzo e nome
    name_text = " ".join(name.text.split())
    print(name_text)
    print("Costo: ", price_text)
    print()
    print_excel(name_text, price_text, url)

def print_excel(name, price, url):
    wb = load_workbook('risultati.xlsx')
    ws = wb.active
    ws.append([name, price, url])
    wb.save('risultati.xlsx')

# Apro il file
f = open("input2.txt", "r")
# Leggo righe nel file
urls = f.readlines()
# Stampo a terminale gli url che visiterò
print(urls)

for url in urls:
    search(url)
