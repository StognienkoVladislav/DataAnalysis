# -*- coding: utf-8 -*-
import sqlite3
import itertools
from selenium import webdriver

search_engine = "https://allo.ua/"

search_lists = [['a'], ['b', 'c'], ['d', 'e', 'q']]

for combo_list in search_lists:
    list_for_pars = list(itertools.permutations(combo_list))

    for lst in list_for_pars:
        browser = webdriver.Chrome(r'C:/chromedriver_win32/chromedriver.exe')
        browser.get(search_engine)

        element = browser.find_element_by_id('search')
        word = [''.join(str(w) for w in lst)]

        conn = sqlite3.connect('allo_db.sqlite')
        c = conn.cursor()
        element.send_keys(word)

        browser.implicitly_wait(3)

        all_links = browser.find_elements_by_id("search-suggest-query")
        result = []

        for link in all_links:
            span = link.find_elements_by_tag_name('span')
            for li in span:
                result.append(li.text.encode('utf-8'))

        to_db = [word[0], '; '.join(str(res) for res in result)]

        c.execute("""INSERT INTO allo_parse (search_param, results) VALUES ("{}", "{}");""".format(to_db[0], to_db[1]))
        conn.commit()
        conn.close()
