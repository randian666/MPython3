#!/usr/bin/env python3

'''
下载器
对指定的URL网页内容进行下载。
'''
from urllib import request
import chardet
from urllibpro import HtmlParser

class HtmlDownLoader(object):
    def download(self,url,html_encode="utf-8"):
        reponse=request.urlopen(url)
        if reponse.getcode()!=200:
            return None
        #获取页面内容
        html=reponse.read()
        # 获取页面编码
        # charset = chardet.detect(html);
        return html.decode(html_encode)
if __name__ == '__main__':
    url="https://book.douban.com/subject/1082154/"
    html=HtmlDownLoader()
    data=html.download(url,'utf-8')
    parser=HtmlParser.HtmlParser()
    new_urls,new_datas=parser.parse(url,data)
    print(new_urls)
    print(new_datas)
