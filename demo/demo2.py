#!/usr/bin/env python3

from demo import my_abs
import math

print(my_abs(-222));

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

#限制关键字参数的名字 而且必须传入限制后的参数
def persion(name ,age, *, city,code):
    print(name,age,city,code);

persion('liuxun',23,city='beijing',code=1234123);

L = ['Hello', 'World', 18, 'Apple', None]
print([n.lower() for n in L if isinstance(n,str)]);

# 每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
k=(l for l in range(1000))
print(next(k))
for h in k:
    print(h)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
g=fib(10)
while True:
    try:
        x=next(g);
        print(x);
    except StopIteration as e:
        print('StopIteration:'+e.value)
        break;

def triangles():
    L=[1]
    while True:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

t=triangles()
n=10;
while n>0:
        print(next(t))
        n=n-1;

for x in range(1):
    print(x)

# generator定义
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        print(next(it))
    except:
        break;

def f(x):
    return x*x;

L=map(f,[1,2,3,4])
print(list(L))



from functools import reduce
def h(x,y):
    return x+y;
print(reduce(h,[1, 3, 5, 7, 9]))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name[0].upper()+name[1:].lower();

LL=['adam', 'LISA', 'barT']
L1=list(map(normalize,LL))
print(L1)
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L);
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2float(s):
    print(s.index("."))
    sp=s.split('.')
    flag=len(s)-1-s.index('.');
    s1=reduce(lambda x,y:x*10+y,map(char2num,sp[0]))#把'123'转成123
    s2=reduce(lambda x, y: x * 10 + y, map(char2num, sp[1]))/(10**(flag))#把'456'转换成0.456
    return s1+s2;
print('str2float(\'123.456\') =', str2float('123.456789'))

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
L=[x for x in range(1,1000)]
print(list(filter(lambda x:str(x)==str(x)[::-1] and x>10,L)))

print(sorted([36, 5, -12, 9, -21]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21],key=abs))

# 请用sorted()对上述列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=lambda x:x[0].lower()))
# 再按成绩从高到低排序：
print(sorted(L,key=lambda y:y[1],reverse=True))

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
import functools
def dolog(ar='execute'):
    def log(func):
        @functools.wraps(func)  #避免原函数的__name__的值被修改成返回函数的值
        def wrapper(*args,**kwargs):
            print(ar,"begin call")
            result=func(*args,**kwargs)
            print(ar,"end call")
            return result;
        return wrapper;
    return log;
@dolog("f() ")
def f():
    print('f() running')
f();

from PIL import Image
im=Image.open("C:\\Users\\Public\\Pictures\\Sample Pictures\\stock-photo-83625707.jpg")
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

import sys
print(sys.path)


class Student(object):
    name='zhangsan'
    def run(self):
        print("sssss")
    def __len__(self):
        return 100;

o=Student();
print(dir(o))
print(len(o))
print(hasattr(o,'x')) # 有属性'x'吗？
setattr(o, 'y', 19) # 设置一个属性'y')
print(getattr(o,'y'))# 获取属性'y'
print(getattr(o,'h',404)) #如果属性没有获取到就返回默认值


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def width(self):
        return self._width;
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an Integer');
        if value<0 or value>1000:
            raise ValueError('width must between 0 ~ 100!')
        self._width=value;

    @property
    def height(self):
        return self._height;

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an Integer');
        if value < 0 or value > 1000:
            raise ValueError('height must between 0 ~ 100!')
        self._height = value;
    @property
    def resolution(self):
        return self._width * self._height;
o =Screen();
o.width=100;
o.height=100;
print(o.resolution)
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
stu=Student("liu")
print(stu.__str__())
print(stu)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
for n in Fib():
    print(n)


class Chain(object):

    def __init__(self, path='GET'):
        self._path = path

    def __getattr__(self, path): # 动态获取属性时返回新实例 获取不存在的属性或者方法时候会调用__getattr__
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, attr): # 将新对象当函数调用时做相同操作
        return Chain('%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path

    __repr__ = __str__
c=Chain()
print(c.user("aaaa").list.user)

from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Sun)
print(Weekday["Sun"])
print(Weekday.Sun.name)
print(Weekday.Sun.value)
print(dir(Weekday))
for member in Weekday:
    print(member)
for name, member in Weekday.__members__.items():
    print(name,member)
