import requests
import csv
from bs4 import BeautifulSoup


def scrap_homepage(url):
    """recupère la liste de la page d'acceuil"""
    response = requests.get(url)

    if response.ok:
        response.encoding = 'utf8'
        soup = BeautifulSoup(response.text, 'html.parser')
        links = ['https://books.toscrape.com/' + item['href'] for item in soup.select('.nav-list>li>ul>li>a')]
        print(links)


scrap_homepage('https://books.toscrape.com/index.html')
with open('fichier_product.csv', mode='w', newline='') as csv_file:
    fieldnames = ['upc', 'titre', 'incl', 'excl', 'disponible', 'description', 'type', 'image', 'recent']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'upc': 'upc', 'titre': 'title', 'incl': 'price_incl', 'excl': 'price_excl', 'disponible': 'availability', 'description': 'description', 'type': 'product_type', 'image': 'image', 'recent': 'recent'})
