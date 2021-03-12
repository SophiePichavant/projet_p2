import requests
from bs4 import BeautifulSoup


def scrap_type(url):
    response = requests.get(url)

    if response.ok:
        response.encoding = 'utf8'
        soup = BeautifulSoup(response.text, 'html.parser')
        links = ['https://books.toscrape.com/' + item['href'] for item in soup.select('.nav-list>li>ul>li>a')]
        print(links)

scrap_type('https://books.toscrape.com/index.html')