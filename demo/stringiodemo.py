#!/usr/bin/env python3
'''
StringIO顾名思义就是在内存中读写str要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可

'''
def stringio_test():
    from io import StringIO
    s = StringIO()
    s.write("zhangsan")
    s.write("李白")
    print(s.getvalue())
    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        ss=f.readline()
        if ss=='':
            break;
        print(ss.strip())
def byteio_test():
    from io import BytesIO
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue().decode("utf-8"))
if __name__ == "__main__":
    stringio_test()
    byteio_test();