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
    writer.writerow(['Title', 'Price'])
    for page in PAGES:
        url = BASE_URL + page
        response = get(url)
        sp = BeautifulSoup(response.content, 'html.parser')
        products = sp.findAll('div', class_='cat-product')
        for product in products:
            title_tag = product.find('a', class_='productLink')
            if title_tag:
                title = title_tag.get('title')
            else:
                title = ''
            price_tag = product.find('div', class_='price-new')
            if price_tag:
                price = price_tag.get_text(strip=True)
            else:
                price = ''
            writer.writerow([title, price])
