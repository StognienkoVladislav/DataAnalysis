
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_hrefs(url):
    hrefs = []

    try:
        html = urlopen(url)

    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        for sibling in bsObj.findAll("div", class_="featured-collection__info js-product-tile"):
            hrefs.append(sibling.find('a').get('href'))

    except AttributeError as e:
        return None

    return hrefs


def get_info(hrefs):
    info = {}

    for i, url in enumerate(hrefs):

        html = urlopen(base + url)

        bsObj = BeautifulSoup(html.read(), 'lxml')
        info[i] = []
        for sibling in bsObj.findAll("div", class_="grid__item large-up--one-third product__selector-container"):
            sku = sibling.find("div", class_='product__sku').get_text()
            info[i] = []
            info[i].append(sibling.h1.get_text())
            for price in sibling.find("div", class_='product__price-wrapper').find_all('span'):
                info[i].append(price.get_text())
            for gg in sibling.findAll('div', {'itemprop': 'offers'}):
                for asd in gg.find_all('label')[:-1]:
                    info[i].append(asd.get('data-value'))

        for gg in bsObj.find_all('div', {'class': 'resp-tabs-container resp-element'}):

            for asd in gg.findAll('div'):
                info[i].append(asd.get_text())

    return info


html_url = 'https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms'
excluse = 'https://suzyshier.com/collections/sz_trend_online-exclusives'
base = 'https://suzyshier.com'
hrefs = get_hrefs(excluse)

print(get_info(hrefs))