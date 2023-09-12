import csv
from bs4 import BeautifulSoup
from requests import get

BASE_URL = "https://www.morele.net/kategoria/karty-graficzne-12"

PAGES = [
    "/", 
    "/,,,,,,,,0,,,,/2/", 
    "/,,,,,,,,0,,,,/3/", 
    "/,,,,,,,,0,,,,/4/",
    "/,,,,,,,,0,,,,/5/",
    "/,,,,,,,,0,,,,/6/",
    "/,,,,,,,,0,,,,/7/",
    "/,,,,,,,,0,,,,/8/",
    "/,,,,,,,,0,,,,/9/",
    "/,,,,,,,,0,,,,/10/",
    ]

with open('products.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Title'])
    for page in PAGES:
        url = BASE_URL + page
        page = get(url)
        sp = BeautifulSoup(page.content, 'html.parser')
        products = sp.findAll('div', class_='cat-list-products')
        for product in products:
            links = product.findAll('a', class_='productLink')
            for link in links:
                title = link.get('title')
                price = product.find('div', class_='price-new').get_text(strip=True)
                writer.writerow([title])