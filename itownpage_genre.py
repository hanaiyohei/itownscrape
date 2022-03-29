# coding: エンコーディング名
import requests
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import codecs
from urllib.parse import urljoin
from time import sleep

html = BeautifulSoup(open('スポーツ施設.html'), 'html.parser')

#print(html)
detail_url_list = html.find_all("a", class_="m-article-card__header__title__link")

items = detail_url_list
#print(type(items))
#driver.close()
#sleep(5)

list_url = []
for n in items:
    for s in n:
        s_mod = s.replace('</a>, <a class="m-article-card__header__title__link" data-v-4839c9c6="" href="', '').replace('/" target="_blank">', '').replace('<a class="m-article-card__header__title__link" data-v-1d1f5f44="" href="', '').replace('\n', '-').replace(' ', "").replace("-</a>", "\n")
        list_url.append("スポーツ施設" + "-" + s_mod)
        print(list_url)
#cur_url = driver.current_url

#else:
    #print("over " + key + " " + pref + " " + str(resultnum))
    
    #sleep(5)
    

    #driver.close()
