#!/usr/bin/env python3
'''
1、编写单元测试，我们需要引入Python自带的unittest模块
2、编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
3、以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
4、对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的

'''
import unittest

from demo.mydict import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test');
        self.assertEqual(d.a,1)
        self.assertTrue(isinstance(d, dict))
        # 另一种重要的断言就是期待抛出指定类型的Error
        # with self.assertRaises(KeyError):
        #     value = d['empty']
        # 可以在单元测试中编写两个特殊的setUp()
        # 和tearDown()
        # 方法。这两个方法会分别在每调用一个测试方法的前后分别被执行

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

if __name__ == '__main__':
    #运行单元测试
    unittest.main()