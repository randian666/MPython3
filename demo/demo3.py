#!/usr/bin/env python3

# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
MyShinyClass = type('MyShinyClass', (), {})  # 返回一个类对象

m=MyShinyClass();
print(m)

Foo = type('Foo', (), {'bar':True})
f=Foo();
print(f.bar)

FooChild = type('FooChild', (Foo,),{})
fc=FooChild();
print(hasattr(fc,'bar'))
print(fc.bar)


import logging  #Python内置的logging模块可以非常容易地记录错误信息
logging.basicConfig(level=logging.INFO) #日志级别
try:
    print('try...')
    r = 10 / int('0')
    print('result:', r)
except ValueError as e:
    logging.error(e)
except ZeroDivisionError as e:
    logging.error(e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
# 程序也可以主动raise抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  #凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
    return 10 / n

foo('0')

