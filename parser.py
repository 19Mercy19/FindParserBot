import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


url= 'https://www.list.am/category/56?pfreq=1&po=1&n=1&price1=&price2=&crc=-1&_a5=0&_a39=0&_a40=0&_a11_1=&_a11_2=&_a4=0&_a37=0&_a3_1=&_a3_2=&_a38=0&gl=2'
base_url = 'https://www.list.am/ru'


class Advertisement:
    def __init__(self, url, desc, price, place, image):
        self.url = url
        self.desc = desc
        self.price = price
        self.place = place
        self.image = image

    # @property
    # def url(self):
    #     return self.__url
    #
    # @url.setter
    # def url(self, new_url):
    #     self.__url = new_url
    #
    # @property
    # def desc(self):
    #     return self.__desc
    #
    # @desc.setter
    # def desc(self, all_desc):
    #     self.__desc = all_desc.select_one('h1').text
    #
    # @property
    # def price(self):
    #     return self.__price
    #
    # @price.setter
    # def price(self, bar):
    #     self.__price = bar.select_one('div.price').find('span', {'class': 'price x'}).text
    #
    # @property
    # def place(self):
    #     return self.__price
    #
    # @place.setter
    # def place(self, bar):
    #     self.__place = bar.select_one('div.loc').select_one('a').text
    #
    # @property
    # def image(self):
    #     return self.__image
    #
    # @image.setter
    # def image(self, info):
    #     self.__image = info.select_one('div.pv').select_one('img').get('src')
    #
    # def __getattribute__(self, item):
    #     if getattr(self, item) is None:
    #         return 'Данных нет'


def get_products():
    response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    products = soup.select_one('div.dl')
    return products


def get_products_urls() -> list:
    urls = []
    products = get_products()
    for product in products:
        try:
            url = base_url + product.get('href')
            urls.append(url)
        except AttributeError:
            continue
    return urls

print(get_products_urls())


# urls = get_products_urls()
#
#
# for url in urls:
#     response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
#     html = response.content
#     soup = BeautifulSoup(html, 'lxml')
#     info = soup.select_one('div.vit')
#     image = info.select_one('div.pv').select_one('img').get('src')
#     all_desc = info.select_one('div.vih')
#     bar = all_desc.select_one('div#abar')
#     price = bar.select_one('div.price').find('span', {'class': 'price x'}).text
#     place = bar.select_one('div.loc').select_one('a').text
#     desc = all_desc.select_one('h1').text
#
#     print(url, desc, price, place, image, sep='\n')


def get_list_advertisements() -> list:
    urls = get_products_urls()
    advertisements = []
    for url in urls:
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
        advertisements.append(Advertisement(url, desc, price, place, image))
    return advertisements

a  = get_list_advertisements()

for i in a:
    print(i.__dict__)

