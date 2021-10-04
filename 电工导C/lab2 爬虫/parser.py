import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

sign_in_url = "https://www.yaozh.com/login/"
info_url = "https://www.yaozh.com/member/basicinfo/"

data = {"username": "startosphere",
        "pwd": "hxt20020512",
        "formhash": "4A95C39D38",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"}

headers={
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, \
    like Gecko) Chrome/58.0.3029.110Safari/537.36"
}
ss=requests.session()
response=ss.get(sign_in_url,headers=headers,data=data)
ss.cookies.update(ss.cookies)
response=ss.get(info_url,headers=headers)
print(ss.cookies)
soup=BeautifulSoup(response.text,features="html.parser")
print(soup.get_text())
