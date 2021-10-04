# SJTU EE208

import re
import sys
import requests
from bs4 import BeautifulSoup


def parseIMG(content):
    urlset = set()
    ########################
    soup = BeautifulSoup(content, 'html.parser')
    """
    方式一：
    a_label=soup.find_all('img',attrs={'src':True})
    """
    a_label=soup.select('img[src]')
    for a in a_label:
        urlset.add(a.get('src'))
    ########################

    return urlset


def write_outputs(urls, filename):
    file = open(filename, 'w', encoding='utf-8')
    for i in urls:
        file.write(i)
        file.write('\n')
    file.close()


def main():
    url = "http://www.baidu.com"
    #设置最大超时时间为6秒
    content = requests.get(url,timeout=6).text
    urlSet = parseIMG(content)
    write_outputs(urlSet,'res2.txt')


if __name__ == '__main__':
    main()