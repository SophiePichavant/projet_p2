import requests
from bs4 import BeautifulSoup


def scrap_categories(url):
    response = requests.get(url)

    if response.ok:
        response.encoding = 'utf8'
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [item['href'].replace('../../../','https://books.toscrape.com/catalogue/') for item in soup.select('.row>li>article>div>a')]
        print(links)

scrap_categories('https://books.toscrape.com/catalogue/category/books/travel_2/')
