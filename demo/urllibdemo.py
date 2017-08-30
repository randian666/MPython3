#!/usr/bin/env python3

import urllib
from urllib import request,parse
from html.entities import name2codepoint
import http.cookiejar
import json
#GET
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
     data=f.read();
     print("status:",f.status,f.reason)
     for k,v in f.getheaders():
         print(k,v)
     print(data)
# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页
re=request.Request('http://www.douban.com/');
re.add_header("User-Agent","Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25");
with request.urlopen(re) as f:
    data = f.read();
    print("status:", f.status, f.reason)
    for k, v in f.getheaders():
        print(k, v)
    print(data)


# Post
#
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。模拟登陆
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data=parse.urlencode([('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])
login_url="https://passport.weibo.cn/sso/login";
home_url="https://m.weibo.cn/feed/friends?version=v4";
url="";
header={'Origin': 'https://passport.weibo.cn',
        'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25',
        'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'}
req = urllib.request.Request(login_url,login_data.encode('utf-8'),header)
# response = urllib.request.urlopen(request) #没有cookie的post访问
#自动记住cookie
cj = http.cookiejar.CookieJar()
# 自定义opener,并将opener跟CookieJar对象绑定
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#安装opener,此后调用urlopen()时都会使用安装过的opener对象
r = opener.open(req)
print(r.read().decode('utf-8'))
#登陆后访问home_url
req_home = urllib.request.Request(home_url,headers=header)
home_result=opener.open(req_home)
html=home_result.read().decode('utf-8');
print(html)
#json解析
tagert=json.loads(html)#解析json格式,解出来是一个字典
print(type(tagert))
print(type(tagert[0]))
weibo_content_list=tagert[0]["card_group"];
for group in weibo_content_list:
    if "mblog" in group:
        print(group["mblog"]["user"]["screen_name"],group["mblog"]["text"])
