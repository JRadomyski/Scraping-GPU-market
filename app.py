from bs4 import BeautifulSoup
from requests import get



# first page
URL = "https://www.euro.com.pl/karty-graficzne.bhtml"
page = get(URL)
scrp = BeautifulSoup(page.content, 'html.parser')

def scraping():
    for offer in scrp.find_all('ems-euro-mobile-product-medium-box', class_='product-list__product-box'):
        gpuprice = offer.find(class_='price__value').get_text().strip()
        # gpusystem = offer.find('span', class_='attribute-value').get_text().strip()
        # gpubrand = offer.find('a', class_='js-save-keyword').get_text().strip()[0:5]
        # link = offer.find('a')
        # gpulink = f"https://www.euro.com.pl{link['href']}"
        print(gpuprice)

scraping()
        
#     # second page
    
#     URL2 = "https://www.euro.com.pl/karty-graficzne,strona-2.bhtml"
#     page2 = get(URL2)
#     scrp2 = BeautifulSoup(page2.content, 'html.parser')


#     for offer2 in scrp2.find_all('div', class_ = 'product-row'):
#         gpuprice2 = offer2.find(class_='price-normal selenium-price-normal').get_text().strip()
#         gpusystem2 = offer2.find('span', class_ = 'attribute-value').get_text().strip()
#         gpubrand2 = offer2.find('a', class_ = 'js-save-keyword').get_text().strip()[0:5]
#         link2 = offer2.find('a')
#         gpulink2 = f"https://www.euro.com.pl{link2['href']}"
#         print(gpuprice2, gpusystem2, gpubrand2, gpulink2)
        
        
#     #third page

#     URL3 = "https://www.euro.com.pl/karty-graficzne.bhtml"
#     page3 = get(URL3)
#     scrp3 = BeautifulSoup(page3.content, 'html.parser')


#     for offer3 in scrp3.find_all('div', class_ = 'product-row'):
#         gpuprice3 = offer3.find(class_='price-normal selenium-price-normal').get_text().strip()
#         gpusystem3 = offer3.find('span', class_ = 'attribute-value').get_text().strip()
#         gpubrand3 = offer3.find('a', class_ = 'js-save-keyword').get_text().strip()[0:5]
#         link3 = offer3.find('a')
#         gpulink3 = f"https://www.euro.com.pl{link3['href']}"
#         print(gpuprice3, gpusystem3, gpubrand3, gpulink3)

#     #fourth page

#     URL4 = "https://www.euro.com.pl/karty-graficzne.bhtml"
#     page4 = get(URL4)
#     scrp4 = BeautifulSoup(page4.content, 'html.parser')


#     for offer4 in scrp4.find_all('div', class_ = 'product-row'):
#         gpuprice4 = offer4.find(class_='price-normal selenium-price-normal').get_text().strip()
#         gpusystem4 = offer4.find('span', class_ = 'attribute-value').get_text().strip()
#         gpubrand4 = offer4.find('a', class_ = 'js-save-keyword').get_text().strip()[0:5]
#         link4 = offer4.find('a')
#         gpulink4 = f"https://www.euro.com.pl{link4['href']}"
#         print(gpuprice4, gpusystem4, gpubrand4, gpulink4)
        
# scraping()