import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def pars_texnomart(category):
    texnomart_data = []
    load_dotenv()
    URL = os.getenv("URL")
    HOST = os.getenv("HOST")
    HEADERS = {
        'User-Agent': 'Mozilla/5.0  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }

    html = requests.get(URL+category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')
    blocks =soup.find_all('div',class_="col-3")

    for block in blocks[:5]:
        images = block.find('img').get('data-src')
        content = block.find('h2').get_text()
        prices = block.find('div',class_='product-price__current').get_text(strip=True)
        installment_price =block.find('div',class_="installment-price").get_text(strip=True)
        link = HOST + block.find('a').get('href')
        print(link)

        texnomart_data.append({
            'images': images,
            'content': content,
            'prices': prices,
            'installment_price': installment_price,
            'link': link


        })

    return texnomart_data



pars_texnomart('katalog/obogrevateli/')