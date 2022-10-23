import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


url= 'https://www.list.am/category/56?pfreq=1&po=1&n=1&price1=&price2=&crc=-1&_a5=0&_a39=0&_a40=0&_a11_1=&_a11_2=&_a4=0&_a37=0&_a3_1=&_a3_2=&_a38=0&gl=2'
base_url = 'https://www.list.am/ru'


response = requests.get(url, headers={'User-Agent': UserAgent().chrome})

html = response.content

soup = BeautifulSoup(html, 'lxml')

products = soup.select_one('div.dl')



urls = []
for product in products:
    url = base_url + product.get('href')
    urls.append(url)

for url in urls:
    response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    description = None
    price = None
    city = None
    info = None




