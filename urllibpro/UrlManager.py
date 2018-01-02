#!/usr/bin/env python3
'''
URL管理器
new_urls管理新的链接地址并且去重
used_urls管理已经爬取过的链接地址
'''
class UrlManager(object):
    def __init__(self):
        #新链接地址集合
        self.new_urls=set()
        #已爬过的链接集合
        self.used_urls=set()
    #添加链接地址
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.used_urls:
            self.new_urls.add(url)
    #批量添加链接地址
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    #判断是否还有链接
    def has_new_url(self):
        return len(self.new_urls)>0
    #获取一个新的链接
    def get_new_url(self):
        temp_url=self.new_urls.pop()
        self.used_urls.add(temp_url)
        return temp_url

