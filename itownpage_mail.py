# coding: エンコーディング名
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
from time import sleep
import re
import csv


myfile = open("itown.txt")
urls = myfile.readlines()
myfile.close()
urls_list = []
for number in urls:
    url = number.strip()
    res = requests.get(url)

    html = BeautifulSoup(res.text, 'html.parser')
    
    #print(html)
    if len(html.find_all("dl")) > 0:
        detail = html.find_all("dl")
        detail = str(detail)
        detail = re.split('[,<>"]', detail)
        #print(detail)

        list_hp = [s for s in detail if 'null' not in s and '://' in s]
        list_hpage = []
        #print(list_hp)
        for item in list_hp:
            item_mod = item.replace('mailto:', '').replace('\n', "").replace('\\n', "").replace('"', '').replace('{', '').replace('\t', '').replace(' ', '').replace("'", '').replace("title=", '')
            list_hpage.append(item_mod)

        list_tell = [s for s in detail if 'null' not in s and re.match('[\(]{0,1}[0-9]{2,4}[\)\-\(]{0,1}[0-9]{2,4}[\)\-]{0,1}[0-9]{3,4}', s)]
        list_telln = []
        
        for item in list_tell:
            item_mod = item.replace('mailto:', '').replace('\n', "").replace('\\n', "").replace('"', '').replace('{', '').replace('\t', '').replace(' ', '').replace("'", '').replace("title=", '')
            list_telln.append(item_mod)

        list_mail = [s for s in detail if 'null' not in s and 'mailto' in s]
        list_email = []
        #print(list_mail)
        for item in list_mail:
            item_mod = item.replace('mailto:', '').replace('\n', "").replace('\\n', "").replace('"', '').replace('{', '').replace('\t', '').replace(' ', '').replace("'", '').replace("title=", '')
            list_email.append(item_mod)
        #print(list_email)

        list_address = [s for s in detail if "https" not in s and '県' in s or '都' in s or '北海道' in s or '府' in s]
        #print(list_address)
        print(url + str(list_email) + str(list_hpage) + str(list_address[0]) + str(list_telln))
        sleep(1)
    else:
        url = url.replace("/shop", "")
        res = requests.get(url)
        
        html = BeautifulSoup(res.text, 'html.parser')
        title = html.find_all(class_="o-detail-header__info")
        detail = list(html.find_all("dl"))
        detail = str(detail)
        detail = re.split('[,<>"]', detail)
        #print(detail)

        list_hp = [s for s in detail if 'null' not in s and '://' in s]
        list_hpage = []
        
        for item in list_hp:
            item_mod = item.replace('mailto:', '').replace('\n', "").replace('\\n', "").replace('"', '').replace('{', '').replace('\t', '').replace(' ', '').replace("'", '').replace("title=", '')
            list_hpage.append(item_mod)
        
        list_tell = [s for s in detail if 'null' not in s and re.match('[\(]{0,1}[0-9]{2,4}[\)\-\(]{0,1}[0-9]{2,4}[\)\-]{0,1}[0-9]{3,4}', s)]
        list_telln = []
        
        for item in list_tell:
            item_mod = item.replace('mailto:', '').replace('\n', "").replace('\\n', "").replace('"', '').replace('{', '').replace('\t', '').replace(' ', '').replace("'", '').replace("title=", '')
            list_telln.append(item_mod)
        

        list_mail = [s for s in detail if 'null' not in s and 'mailto' in s]
        list_email = []
        #print(list_mail)
        for item in list_mail:
            item_mod = item.replace('mailto:', '').replace('\n', "").replace('\\n', "").replace('"', '').replace('{', '').replace('\t', '').replace(' ', '').replace("'", '').replace("title=", '')
            list_email.append(item_mod)
        #print(list_email)

        list_address = [s for s in detail if "http" not in s and '県' in s or '都' in s or '北海道' in s or '府' in s]
        #print(list_address)
        if len(list_address) > 0:
            print(url + str(list_email) + str(list_hpage) + str(list_address[0]) + str(list_telln))
            sleep(1)
        else:
            pass
            sleep(1)
    """
    begin = 'E-mailアドレス'
    end = '<dt>業種</dt>'
    r = re.compile( '(%s.*%s)' % (begin,end), flags=re.DOTALL)
    m = r.search(html)
    script = ''
    if m is not None:
        script = m.group(0)
    script_list = script.split(',')
    print(script_list)
    print(type(script_list))
    """

    """
    var_img_list = [s for s in script_list if 'https://' in s]
    img_list = []
    for item in var_img_list:
        item_mod = item.replace('_50x50.jpg', '').replace('"summImagePathList":', '').replace('{', '')
        img_list.append(item_mod)
    """
