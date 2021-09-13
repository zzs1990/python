# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import os


def download(url, pic_alt, name):
    path = f'D:\\美女图片\\{pic_alt}\\'
    # 判断系统是否存在该路径，不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    # 下载图片并保存在本地
    urllib.request.urlretrieve(url, f'{path}{name}.jpg')


agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
# 定义请求头
header = {
    "User-Agent": agent,
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}


# 网页分析
def run(target_url, begin_num, end_num):
    # 创建网络请求对象
    req = urllib.request.Request(url=target_url, headers=header)
    response = urllib.request.urlopen(req)  # 这里的req可看成一种更为高级的URL
    # 设置请求参数
    html = response.read().decode('gb2312', 'ignore')  # 解码 得到这个网页的html源代码：这个网站的编码使用的是GB2312格式，更常见的网站编码格式应该是UTF-8了吧
    soup = BeautifulSoup(html, 'html.parser')  # 将得到的HTML代码使用python自带的解析器（也可以使用lxml解析器，性能会更好，本代码从简
    # 获取图片div
    divs = soup.find_all('div', attrs={'id': 'big-pic'})
    # 当前页
    now_page = soup.find('span', attrs={'class': 'nowpage'}).get_text()
    # 所有页
    total_page = soup.find('span', attrs={'class': 'totalpage'}).get_text()
    if begin_num == end_num:  # 跳出条件
        return
    for div in divs:
        begin_num = begin_num + 1
        # 判断是否存在图片
        if div.find("a") is None:  # 如果这张图片没有下一张图片的链接
            print("没有图片")
            return
        # 有链接，但是是 空链接
        elif div.find("a")['href'] is None or div.find("a")['href'] == "":
            print("没有图片")
            return
        # 展示进度
        print("下载信息：总进度：", begin_num, "/", end_num, " ，正在下载组图：(", now_page, "/", total_page, ")")

        # 变换成下一页
        if int(now_page) < int(total_page):
            # 获取下一张图片链接
            next_page_link = "http://www.mmonly.cc/mmtp/xgmn/" + (div.find('a')['href'])
        elif int(now_page) == int(total_page):
            # 获取下一组图片链接
            next_page_link = (div.find('a')['href'])
        # 获取图片链接
        pic_link = (div.find('a').find('img')['src'])  # 本网站大图的SRC属性是下一张图片的链接
        pic_alt = (div.find('a').find('img'))['alt']  # 图片的名字alt属性
        print('下载的图片链接:', pic_link)
        print('组图名：[ ', pic_alt, ' ] ')
        print('开始下载...........')
        download(pic_link, pic_alt, now_page)
        print("下载成功！")
        print('下一页链接:', next_page_link)
        # 递归
        run(next_page_link, begin_num, end_num)
        return


# 主函数
if __name__ == '__main__':
    # http://www.mmonly.cc/mmtp/qcmn任意一个网址开始爬取，是爬取的起点（）
    targetUrl = "https://www.mmonly.cc/mmtp/xgmn/325125.html"
    run(targetUrl, begin_num=0, end_num=100)  # 设置下载图片数量：endNUM-beginNUM 数字相减为总数量
