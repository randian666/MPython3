#!/usr/bin/env python3

from urllib import request
import chardet

if __name__ == '__main__':
    response=request.urlopen("https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4");
    #读取页面源码
    html=response.read();
    #获取页面编码
    charset=chardet.detect(html);
    html=html.decode(charset['encoding'])
    print(html)
