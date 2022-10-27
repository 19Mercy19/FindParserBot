import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


url= 'https://www.list.am/category/56?pfreq=1&po=1&n=1&price1=&price2=&crc=-1&_a5=0&_a39=0&_a40=0&_a11_1=&_a11_2=&_a4=0&_a37=0&_a3_1=&_a3_2=&_a38=0&gl=2'
base_url = 'https://www.list.am/ru'




# def get_products():
response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
html = response.content
soup = BeautifulSoup(html, 'lxml')
products = soup.select_one('div.dl')
# return products


urls = []

for product in products:
    try:
        url = base_url + product.get('href')
        urls.append(url)
    except AttributeError:
        continue
print(len(urls))


# for url in urls:
url = urls[0]
response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
html = response.content
soup = BeautifulSoup(html, 'lxml')
info = soup.select_one('div.vit')
image = info.select_one('div.pv').select_one('img').get('src')
all_desc = info.select_one('div.vih')
bar = all_desc.select_one('div#abar')
price = bar.select_one('div.price').find('span', {'class': 'price x'}).text
place = bar.select_one('div.loc').select_one('a').text
desc = all_desc.select_one('h1').text

print(url, desc, price, place, image, sep='\n')



