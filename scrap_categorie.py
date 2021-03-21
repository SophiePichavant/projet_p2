from bs4 import BeautifulSoup
import requests
import argparse


def scrap_categorie(url):
    """recupère les données d'une catégorie"""
    books_urls = []

    page = 'index'
    step = 1
    while True:
        if step > 1:
            page = f'page-{step}'
            url = f'https://books.toscrape.com/catalogue/category/books/mystery_3/{page}.html'
        response = requests.get(url).text
        if response.ok:
            response.encoding = 'utf8'
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [item['href'].replace('../../../', 'https://books.toscrape.com/catalogue/') for item in soup.select('.row>li>article>div>a')]
            books_urls += links
            step += 1

        else:
            break
    return books_urls


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('scrap_categorie', help='')
    args = parser.parse_args()
    print(scrap_categorie(args.scrap_categorie))
