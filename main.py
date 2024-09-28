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
    writer.writerow(['Title', 'Price', 'Długość karty', 'Ilość pamięci RAM', 'Rodzaj chipsetu', 'Taktowanie rdzenia w trybie boost'])
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

            # Inicjalizacja zmiennych cech produktu
            dlugosc_karty = ''
            ilosc_pamieci_ram = ''
            rodzaj_chipsetu = ''
            taktowanie_rdzenia = ''

            # Wyszukiwanie cech produktu
            features_div = product.find('div', class_='cat-product-features')
            if features_div:
                feature_items = features_div.find_all('div', class_='cat-product-feature')
                for feature in feature_items:
                    feature_text = feature.get_text(strip=True)
                    if 'Długość karty:' in feature_text:
                        dlugosc_karty = feature.find('b').get_text(strip=True)
                    elif 'Ilość pamięci RAM:' in feature_text:
                        ilosc_pamieci_ram = feature.find('b').get_text(strip=True)
                    elif 'Rodzaj chipsetu:' in feature_text:
                        rodzaj_chipsetu = feature.find('b').get_text(strip=True)
                    elif 'Taktowanie rdzenia w trybie boost:' in feature_text:
                        taktowanie_rdzenia = feature.find('b').get_text(strip=True)
            # Zapis danych do pliku CSV
            writer.writerow([title, price, dlugosc_karty, ilosc_pamieci_ram, rodzaj_chipsetu, taktowanie_rdzenia])
