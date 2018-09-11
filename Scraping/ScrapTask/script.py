import json

from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_hrefs(mass_url):
    hrefs = []
    for url in mass_url:
        html = urlopen(url)

        bsObj = BeautifulSoup(html.read(), 'lxml')
        for sibling in bsObj.findAll("div", class_="featured-collection__info js-product-tile"):
            hrefs.append(sibling.find('a').get('href'))

    return hrefs


def get_info(hrefs, *args):
    info = {}
    columns = args[0]
    print(len(hrefs))
    for i, url in enumerate(hrefs):
        i += 1
        html = urlopen(base + url)

        bsObj = BeautifulSoup(html.read(), 'lxml')
        info[i] = {}

        for sibling in bsObj.findAll("div", class_="grid__item large-up--one-third product__selector-container"):
            sku = sibling.find("div", class_='product__sku').get_text()
            if 'SKU' in columns:
                info[i]['SKU'] = sku
            if 'title' in columns:
                info[i]['Title'] = sibling.h1.get_text()

            all_prices = []
            if 'price' in columns:
                for price in sibling.find("div", class_='product__price-wrapper').find_all('span'):
                    all_prices.append(price.string.strip())
                if len(all_prices) >1:
                    info[i]['price'] = all_prices[1]
                    info[i]['discount_price'] = all_prices[2]
                else:
                    info[i]['price'] = all_prices[0]
                    info[i]['discount_price'] = 'No discount'

            if 'color' in columns or 'size' in columns:
                for gg in sibling.findAll('div', {'itemprop': 'offers'}):
                    if 'color' in columns:
                        info[i]['color'] = []
                        for asd in gg.find_all('label', {'data-option': 'option1'}):
                            info[i]['color'].append(asd.get('data-value'))

                    if 'size' in columns:
                        info[i]['size'] = []
                        for asd in gg.find_all('label', {'data-option': 'option2'}):
                            info[i]['size'].append(asd.get('data-value'))

        if 'description' in columns or 'specs' in columns:
            for gg in bsObj.find_all('div', {'class': 'resp-tabs-container resp-element'}):
                if 'description' in columns:
                    for asd in gg.findAll('div', {'id': 'toggle-product__description'}):
                        info[i]['description'] = asd.get_text().strip()
                if 'specs' in columns:
                    for asd in gg.findAll('div', {'id': 'toggle-product__specs'}):
                        info[i]['specs'] = asd.get_text().strip()

    return info


pages = 2
base = 'https://suzyshier.com'
exclusives = 'https://suzyshier.com/collections/sz_trend_online-exclusives'

# Если больше 1 страницы
urls = []
for page in range(pages):
    urls.append('https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page={}'.format(page+1))

# Для exclusives
# hrefs = get_hrefs([exclusives])

# Для bottoms
hrefs = get_hrefs(urls)

all_params = ['SKU', 'title', 'price', 'color', 'size', 'description', 'specs']

# В массив добавляем нужные параметры или используем все (all_params)
# full_info = get_info(hrefs, ['title', 'price', 'description', 'size'])
full_info = get_info(hrefs, all_params)

# Изменяем имя файла, относительно нужных URLs
file_name = 'bottoms.json'
with open(file_name, 'w') as outfile:
    json.dump(full_info, outfile)
