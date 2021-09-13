# -*- coding: utf-8 -*-
import json
import requests
from lxml import etree

key_code = "河南省考"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
response = requests.get(f'https://www.baidu.com/s?wd={key_code}&lm=1', headers=headers)

r = response.text
html = etree.HTML(r, etree.HTMLParser())
r1 = html.xpath('//h3')
r2 = html.xpath('//*[@class="c-abstract"]')
r3 = html.xpath('//*[@class="t"]/a/@href')

print(f"r1[{len(r1)}] = [{r1}]")
print(f"r2[{len(r2)}] = [{r2}]")
print(f"r3[{len(r3)}] = [{r3}]")

min_len = min(len(r1), len(r2), len(r3))
for i in range(min_len):
    r11 = r1[i].xpath('string(.)')
    r22 = r2[i].xpath('string(.)')
    r33 = r3[i]
    with open(f'{key_code}_ok.txt', 'a', encoding='utf-8') as c:
        c.write(json.dumps(r11, ensure_ascii=False) + '\n')
        c.write(json.dumps(r22, ensure_ascii=False) + '\n')
        c.write(json.dumps(r33, ensure_ascii=False) + '\n')
    print(r11, end='\n')
    print('------------------------')
    print(r22, end='\n')
    print(r33)
