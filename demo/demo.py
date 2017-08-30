#!/usr/bin/env python3

print('hello, world')
print('The quick brown fox', 'jumps over', 'the lazy dog')
print("1024 * 768 =",1024 * 768)
# IO
# name =input("please you name:")
# print("hello,",name)
# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m ok.')
# Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

print( 9 / 3)
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10//3)
# 因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：
print(10 % 3)
# Python还允许用r''表示''内部的字符串默认不转义
s4 = r'''Hello,\n
Lisa!'''
print(s4)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x