# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

req_obj = requests.get('http://www.ha.stats.gov.cn/zjtj/')
req_obj.encoding = 'utf-8'
soup = BeautifulSoup(req_obj.text, 'lxml')

'''标签查找'''
print(soup.title)  # 只是查找出第一个
print(soup.meta)
print(soup.findall("name"))
