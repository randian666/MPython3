#!/usr/bin/env python3

'''
Python内置的os模块也可以直接调用操作系统提供的接口函数
'''
import os

print(os.name) # 操作系统类型  如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

# print(os.uname()) #要获取详细的系统信息，可以调用uname()函数 uname()函数在Windows上不提供

print(os.environ) #操作系统中定义的环境变量，全部保存在os.environ这个变量中

print(os.environ.get("JAVA_HOME")) #要获取某个环境变量的值

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用

print(os.path.abspath(".")) # 查看当前目录的绝对路径:

print(os.path.join("E:\\pywork",'pythonos4'))  # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.mkdir("E:\\pywork\\pythonos4") # 然后创建一个目录:
# os.rmdir('E:\\pywork\\pythonos4') # 删掉一个目录:
print(os.path.split("e:\\count.txt")) #拆分文件目录 # 而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.splitext("e:\\count.txt"))  #获取文件后缀 os.path.splitext()可以直接让你得到文件扩展名


# os.rename("e:\\count.txt_bak","e:\\count.txt") #重命名文件
# os.remove("e:\\count.txt")  #删除文件
#过滤文件
fi= [x for x in os.listdir('.') if os.path.isdir(x)]
print(fi)
# 要列出所有的.py文件
l=[f for f in os.listdir(".") if os.path.splitext(f)[1]==".py"]
print(l)

# 利用os模块编写一个能实现dir -l输出的程序。
from datetime import datetime
pwd = os.path.abspath('.')
for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def find_fname(name,input='.'):
    if os.path.isdir(input):
        for f in os.listdir(input):
            p=os.path.join(input,f)
            if os.path.isfile(p):
                if name in f:
                    print(p)
            else:
                find_fname(name,p)
    else:
        if name in input:
            print(input)
if __name__=="__main__":
    find_fname('ount',"E:\count.txt")
