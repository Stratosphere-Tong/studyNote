# SJTU EE208

import re
import sys
import urllib.request

from bs4 import BeautifulSoup


def parseURL(content):
    urlset = set()
    ########################
    soup = BeautifulSoup(content, 'html.parser')

    """
    方式一：
    a_label=soup.find_all('a',attrs={'href':True})
    """
    a_label=soup.select('a[href]')
    for a in a_label:
        urlset.add(a.get('href'))
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
    content = urllib.request.urlopen(url).read()
    urlSet = parseURL(content)
    write_outputs(urlSet,'res1.txt')


if __name__ == '__main__':
    main()
    
