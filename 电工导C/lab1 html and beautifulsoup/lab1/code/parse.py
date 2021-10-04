# SJTU EE208

import re
import sys
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup


def parseZhihuDaily(content, url):
    zhihulist = list()
    ########################
    soup=BeautifulSoup(content,features="html.parser")
    boxes=soup.findAll('div',{'class':'box'})
    for box in boxes:
        linkpage=urllib.parse.urljoin(url,box.a['href'])
        img=box.img['src']
        text=box.get_text()
        zhihulist.append([img,text,linkpage])        
    ########################
    return zhihulist


def write_outputs(zhihus, filename):
    file = open(filename, "w", encoding='utf-8')
    for zhihu in zhihus:
        for element in zhihu:
            file.write(element)
            file.write('\t')
        file.write('\n')
    file.close()


def main():
    url = "http://daily.zhihu.com/"
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36')
    content = urllib.request.urlopen(req).read()
    zhihus = parseZhihuDaily(content, url)
    write_outputs(zhihus, 'res3.txt')


if __name__ == '__main__':
    main()
