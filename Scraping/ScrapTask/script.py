import json

from urllib.request import urlopen
from bs4 import BeautifulSoup


# Парсим из html страницы, ссылки на товары
def get_hrefs(mass_url):
    hrefs = []
    for url in mass_url:
        html = urlopen(url)
        # Считываем html
        bsObj = BeautifulSoup(html.read(), 'lxml')
        for sibling in bsObj.findAll("div", class_="featured-collection__info js-product-tile"):
            # После нахождения контейнера, вытягиваем ссылки на товары
            hrefs.append(sibling.find('a').get('href'))

    return hrefs


# Обрабатываем ссылки и относительно параметров (args) формируем JSON
def get_info(hrefs, *args):
    info = {}
    columns = args[0]
    print(len(hrefs))
    # В цикле проходимся по всем товарам
    for i, url in enumerate(hrefs):
        i += 1
        # формируем url относительно базовой ссылки и уникальной части
        html = urlopen(base + url)

        bsObj = BeautifulSoup(html.read(), 'lxml')
        info[i] = {}
        # находим div с нужной нам информацией и парсим ее относительно (args)
        for sibling in bsObj.findAll("div", class_="grid__item large-up--one-third product__selector-container"):
            sku = sibling.find("div", class_='product__sku').get_text()
            if 'SKU' in columns:
                info[i]['SKU'] = sku
            if 'title' in columns:
                info[i]['Title'] = sibling.h1.get_text()

            if 'price' in columns:
                all_prices = []
                for price in sibling.find("div", class_='product__price-wrapper').find_all('span'):
                    all_prices.append(price.string.strip())
                if len(all_prices) >1:
                    info[i]['price'] = all_prices[1]
                    info[i]['discount_price'] = all_prices[2]
                else:
                    info[i]['price'] = all_prices[0]
                    info[i]['discount_price'] = 'No discount'

            if 'color' in columns or 'size' in columns:
                for items_prop in sibling.findAll('div', {'itemprop': 'offers'}):
                    if 'color' in columns:
                        info[i]['color'] = []
                        for color in items_prop.find_all('label', {'data-option': 'option1'}):
                            info[i]['color'].append(color.get('data-value'))

                    if 'size' in columns:
                        info[i]['size'] = []
                        for size in items_prop.find_all('label', {'data-option': 'option2'}):
                            info[i]['size'].append(size.get('data-value'))

        if 'description' in columns or 'specs' in columns:
            for desc_and_specs in bsObj.find_all('div', {'class': 'resp-tabs-container resp-element'}):
                if 'description' in columns:
                    for description in desc_and_specs.findAll('div', {'id': 'toggle-product__description'}):
                        info[i]['description'] = description.get_text().strip()
                if 'specs' in columns:
                    for spec in desc_and_specs.findAll('div', {'id': 'toggle-product__specs'}):
                        info[i]['specs'] = spec.get_text().strip()

    return info


# Входные данные
########################################################################################
base = 'https://suzyshier.com'
exclusives = 'https://suzyshier.com/collections/sz_trend_online-exclusives'
all_params = ['SKU', 'title', 'price', 'color', 'size', 'description', 'specs']

# Если больше 1 страницы
pages = 2
urls = []
for page in range(pages):
    urls.append('https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?page={}'.format(page+1))
########################################################################################
# Для exclusives
# hrefs = get_hrefs([exclusives])

# Для bottoms
hrefs = get_hrefs(urls)

# В массив добавляем нужные параметры или используем все (all_params)
# full_info = get_info(hrefs, ['title', 'price', 'description', 'size'])
full_info = get_info(hrefs, all_params)

# Изменяем имя файла, относительно нужных URLs
file_name = 'bottoms.json'
with open(file_name, 'w') as outfile:
    json.dump(full_info, outfile)
