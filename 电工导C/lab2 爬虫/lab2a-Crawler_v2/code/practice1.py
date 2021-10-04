# SJTU EE208

import re
import urllib.parse
import urllib.request
from http import cookiejar

from bs4 import BeautifulSoup

# 1. 构建一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()
# 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
# 3. 通过build_opener()来构建opener
opener = urllib.request.build_opener(cookie_handler)
# 4. addheaders接受一个列表，里面每个元素都是一个headers信息的元组，opener附带headers信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, \
                       like Gecko) Chrome/58.0.3029.110Safari/537.36")]
# 5. 需要登陆的账号和密码, 此处需要使用你们自己注册的账号密码
data = {"username": "startosphere",
        "pwd": "hxt20020512",
        "formhash": "4A95C39D38",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"}

sign_in_url = "https://www.yaozh.com/login/"
info_url = "https://www.yaozh.com/member/basicinfo/"
# 6. 通过urlencode转码
postdata = urllib.parse.urlencode(data).encode("utf8")
# 7. 构建Request请求对象，包含需要发送的用户名和密码
request = urllib.request.Request(sign_in_url, data=postdata,headers = dict(Referer = sign_in_url))
# 8. 通过opener发送这个请求，并获取登陆后的Cookie值
opener.open(request)

# The rest is done by you:
req=opener.open(info_url).read()
soup=BeautifulSoup(req,features="html.parser")
# 访问子节点
my_info=soup.find_all(attrs={'class': 'U_myinfo clearfix'})[0].contents
for i in range(3,10,2):
        # 访问属性value
        print('{0} {1}'.format(my_info[i].dt.string,my_info[i].input.attrs['value']))
# 访问文本text
print('简介：%s'%my_info[11].textarea.text)

        
       
