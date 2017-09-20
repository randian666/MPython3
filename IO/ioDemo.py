#!/usr/bin/env python3
'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，
调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。

默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
 f = open('/Users/michael/test.jpg', 'rb')
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
 f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
 f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
 f = open('/Users/michael/test.txt', 'w')
'''



def read_txt():
    try:
        f=open("e:\\count.txt","r")
        print(f.read())
    finally:
        if f:
            f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
def read_txt_with():
    with open("e:\\count.txt","r") as f:
        print(f.read())

def write_txt():
    with open("e:\\count.txt","w") as w:
        w.write("my name is libai")

if __name__=="__main__":
    read_txt_with()
    write_txt();
    read_txt()