# SJTU EE208

import time
from HashTable import HashTable

def get_page(page):
    print('downloading page %s' % page)
    time.sleep(0.5)
    return g.get(page, [])


def get_all_links(content):
    return content


def union_dfs(a, b):
    for e in b:
        if e not in a:
            a.append(e)


def union_bfs(a, b):
    pass


def crawl(seed, method):
    tocrawl = [seed]
    crawled = HashTable()
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if not crawled.hashtable_lookup(page):
            content = get_page(page)
            outlinks = get_all_links(content)

            globals()['union_%s' % method](tocrawl, outlinks)
            crawled.hashtable_add(page)
    return graph, crawled


g = {'A': ['B', 'C', 'D'],
     'B': ['E', 'F'],
     'D': ['G', 'H'],
     'E': ['I', 'J'],
     'G': ['K', 'L']}

start = time.time()
graph_dfs, crawled_dfs = crawl('A', 'dfs')
end = time.time()
print(end - start)
