#!/usr/bin/env python3

from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

'''
collections是Python内建的一个集合模块，提供了许多有用的集合类。
1、namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
2、使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
3、使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
4、使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
5、Counter是一个简单的计数器
'''

# namedtuple是用来表示一个坐标
Point = namedtuple('Point', ['x', 'y'])
p=Point(1,2)
print(p.x)
print(p.y)

#deque deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q.pop())
print(q)

#defaultdict 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
dd=defaultdict(lambda: 'N/A')
dd["key"]='dddd'
print(dd["key"])
print(dd['key1'])

#OrderedDict

od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
print(list(od.keys()))
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
last=LastUpdatedOrderedDict(2)
last['b']=2
last['c']=3
print(last.popitem())
print(last)


# Counter 统计字符出现的个数
count=Counter();
for ch in 'programming':
    count[ch]=count[ch]+1;
print(count)

