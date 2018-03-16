
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Дочерние элементы
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

# for child in bsObj.find("table", {"id": "giftList"}).children:
#    print(child)

# Одноуровневые элементы

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# Работа с родительскими элементами

print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"
                         }).parent.previous_sibling.get_text())
