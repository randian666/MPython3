#!/usr/bin/env python3
'''
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
Python提供了pickle模块来实现序列化。
'''

import pickle
d=dict(name='bob',age=12,score=45)
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
with open("e:\\count.txt", "wb") as w:
    pickle.dump(d, w)
with open("e:\\count.txt","rb") as f:
    print(f.read())
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
with open("e:\\count.txt","rb") as f:
    print(pickle.load(f))  #这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已


'''
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
JSON类型	        Python类型
{}	            dict
[]	            list
"string"	    str
1234.56	        int或float
true/false	    True/False
null	        None
Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
'''
import json
d=dict(a=1,b=2,c=3)
# dumps()方法返回一个str，内容就是标准的JSON
print(json.dumps(d))
# 用loads()或者对应的load()方法，前者把JSON的字符串反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(type(json.loads(json_str)))
print(json.loads(json_str))

class Student(object):

    def __init__(self,name,age):
        self._name=name;
        self._age=age;
    @property
    def name(self):
        return self._name;
    @name.setter
    def name(self,value):
        self._name=value;
    @property
    def age(self):
        return self._age;
    @name.setter
    def age(self,value):
        self._age=value;
stu=Student('张三',23);
# 把任意class的实例变为dict,因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(stu,default=lambda obj:obj.__dict__))
# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
str='{"name": "张三", "age": 23}'
def dictToStudent(p):
    return Student(p['name'],p['age'])
print(json.loads(str,object_hook=dictToStudent))