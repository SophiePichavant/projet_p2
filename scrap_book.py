from bs4 import BeautifulSoup
import requests
import argparse


def scrap_book(url): 
    """recupère les données d'un bouquin et retourne dans un dictionnaire"""
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
   
    upc = soup.select_one('table > tr:nth-child(1) > td').text
    product_type = soup.select_one('table > tr:nth-child(2) > td').text
    price_excl = soup.select_one('table > tr:nth-child(3) > td').text
    price_incl = soup.select_one('table > tr:nth-child(4) > td').text
    availability = soup.select_one('table > tr:nth-child(6) > td').text
    title = soup.select_one('div.col-sm-6:nth-child(2) > h1:nth-child(1)').text
    image = soup.select_one('.item > img:nth-child(1)')['src']
    recent = soup.select_one('li.col-xs-6:nth-child(1)').text
    description = soup.select_one('.product_page > p:nth-child(3)').text
    

    return {'upc': upc , 'titre': title, 'incl': price_incl, 'excl': price_excl, 'disponible': availability,'description': description, 'type': product_type, 'image': image, 'recent': recent}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='')
    args = parser.parse_args()
    print(scrap_book(args.url))