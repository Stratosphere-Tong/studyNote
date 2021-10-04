# SJTU EE208
import time
import os
import re
import string
import sys
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import threading
import queue

from HashTable import HashTable
import Bitarray

def valid_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)+'.html' # 修改文件后缀为.html 方便直接查看
    return s


def get_page(page):
    req=urllib.request.Request(page)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36')
    try:
        response=urllib.request.urlopen(req,timeout=3)
        content=response.read()
        if response.getcode() == 200:
            return content
    # except urllib.error.URLError:
        return None
    except:
        return None

def get_all_links(content, page):
    links = []
    soup=BeautifulSoup(content,features='html.parser')
    a_labels=soup.findAll('a',{'href' : re.compile('^http|^/')})
    for a in a_labels:
        link=a['href']
        if link[0]!='h':link=urllib.parse.urljoin(page,link)
        links.append(link)
    return links


def union_dfs(a, b):
    for e in b:
        if e not in a:
            a.append(e)


def union_bfs(a, b):
    a[0:0]=list(set(b))


def add_page_to_folder(page, content):  # 将网页存到文件夹里，将网址和对应的文件名写入index.txt中
    index_filename = 'index.txt'  # index.txt中每行是'网址 对应的文件名'
    folder = 'html'  # 存放网页的文件夹
    filename = valid_filename(page)  # 将网址变成合法的文件名
    index = open(index_filename, 'ab')
    index.write(page.encode('utf8', 'ignore')+ b'\t' + filename.encode('utf8','ignore') + b'\n') # write() argument must be bytes, not str
    index.close()
    if not os.path.exists(folder):  # 如果文件夹不存在则新建
        os.mkdir(folder)
    f = open(os.path.join(folder, filename), 'wb')
    f.write(content)  # 将网页存入文件
    f.close()



false_cnt=0
def crawl_BloomFliters(seed,method,max_page):
    global false_cnt
    tocrawl = [seed]
    crawled = Bitarray.BloomFilters(size=20*max_page)# 令k=10
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if not crawled.lookup(page):
            content = get_page(page)
            if content==None:continue # 对于打不开的网页忽略
            outlinks = get_all_links(content,page)
            if outlinks!=[]:graph[page]=outlinks
            globals()['union_%s' % method](tocrawl, outlinks)
            crawled.add(page)
            
            max_page-=1
            if max_page==0:break # 达到最大深度

    return graph, crawled

def add_to_queue(outlinks):
    for i in outlinks:
        q.put(i)

def working(max_page):
    while True:
        
        page=q.get()
        
        if not crawled.lookup(page):
            print(page,max_page,q.qsize())
            content=get_page(page)
            if content==None:continue
            outlinks=get_all_links(content,page)
            if outlinks!=[]:graph[page]=outlinks
            for link in outlinks:
                q.put(link)

            if varLock.acquire():
                graph[page] = outlinks
                crawled.add(page)
                varLock.release()
            max_page-=1
            if max_page==0:break # 达到需要爬取的任务数，停止程序
            
        # q.task_done() 此操作无意义，因为队列中爬取的网址总是无限的
        
            

            


if __name__ == '__main__':
    """
    seed = sys.argv[1]
    method = sys.argv[2]
    max_page = sys.argv[3]
    """
    start = time.time()
    seed,method,max_page='http://www.sjtu.edu.cn','bfs',20
    graph={}
    q=queue.Queue()
    q.put(seed)
    NUM=4 # 4个线程
    varLock=threading.Lock()
    crawled=Bitarray.BloomFilters(size=20*max_page)

    ts=[threading.Thread(target=working, args=(max_page//NUM,))for i in range(NUM)]    

    for t in ts:
        t.setDaemon(True)
        t.start()
    
    # 当所有线程爬到指定个数的page时线程结束
    # 当所有线程结束时，主程序继续运行，否则阻塞等待
    for t in ts:
        t.join()

    end=time.time()
    print(end-start)