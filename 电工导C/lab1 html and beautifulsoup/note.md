# 爬取网页
## 读取
建议使用requests包而不是urllib包，requests包是urllib的进一步封装。
前期读取
```Python
import requests
import BeautifulSoup
#设置最大请求时间为6秒
reqs=requests.get(url,timeout=6)
#判断返回状态码是否为200
reqs.raise_for_status()
#根据网页内容分析可能的编码方式，防止出现中文乱码
reqs.encoding = reqs.apparent_encoding 
#reqs.content()返回的是二进制 处理图片、文件常用
#reqs.text()返回的是Unicode型数据 处理文字
demo=reqs.text
#注意不能有括号！！
```
## 读取
![1]
```html
访问<p class='textarea', vlaue='sss'>aaa</p>
访问对应的value：
soup.p.attrs['value']
访问value下的值：
soup.p.attrs['value'].string
访问文本内容
soup.p.text
访问p的子结点
soup.p.contents
soup.p.children
访问父节点
soup.p.parents

```

## 爬取所有超链接
```Python
soup=BeautifulSoup(demo)
"""
方法一：
soup.find_all('a',attrs={'href'=True})
"""
a_label=soup.select('a[href]')
urlset=set()
for a in a_label:
    urlset.add(a.get('href'))
```
## 传递URL参数
如果你希望为URL的查询字符串传递某种数据
如：
{'wd':'上海','key':'data'}
URL：www.baidu.com
+ 若手工构建：www.baidu.com?wd=上海&key=data
+ request库：
  ```Python
  import requests
  payload={'wd':'上海','key':'data'}
  req=requests.get(url,params=payload)
  # get函数会自动构建好查询字符串
  # print(req.url)
  ```

## 定制请求头
```Python
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

## 生成HTML表单头
+ 何时使用 GET？
  您能够使用 GET（默认方法）：

  如果表单提交是被动的（比如搜索引擎查询），并且没有敏感信息。

  当您使用 GET 时，表单数据在页面地址栏中是可见的：

  action_page.php?firstname=Mickey&lastname=Mouse
> GET 最适合少量数据的提交。浏览器会设定容量限制。

+ 何时使用 POST？
  如果表单正在更新数据，或者包含敏感信息（例如密码）。

  POST 的安全性更好，因为在页面地址栏中被提交的数据是不可见的。

+ 实现
  ```Python
  >>> payload = {'key1': 'value1', 'key2': 'value2'}
  >>> r = requests.post("http://httpbin.org/post", data=payload)
  >>> print(r.text)

  {
    ...
    "form": {
      "key2": "value2",
      "key1": "value1"
    },
    ...
  }
  ```

## Cookie
如果某个响应中包含一些 cookie，你可以快速访问它们：
``` Python
>>> url = 'http://example.com/some/cookie/setting/url'
>>> r = requests.get(url)

>>> r.cookies['example_cookie_name']
'example_cookie_value'
```
要想发送你的cookies到服务器，可以使用 cookies 参数：
```Python
>>> url = 'http://httpbin.org/cookies'
>>> cookies = dict(cookies_are='working')

>>> r = requests.get(url, cookies=cookies)
>>> r.text
'{"cookies": {"cookies_are": "working"}}'
```
Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar 传到 Requests 中：
```Python
>>> jar = requests.cookies.RequestsCookieJar()
>>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
>>> url = 'http://httpbin.org/cookies'
>>> r = requests.get(url, cookies=jar)
>>> r.text
'{"cookies": {"tasty_cookie": "yum"}}'
```

问题：为什么session不能处理药智网的问题

[1]: D:/study_notebook/电工导C/HTML属性介绍.png