#!/usr/bin/env python3

import json

myDict= {"spam" : "foo", "parrot" : 42}
myJson= json.dumps(myDict) # 编码数据
print(type(myJson))
tagert=json.loads(myJson)#解析json格式,解出来是一个字典
print(tagert["spam"])
print(type(tagert))

jsons='''
rating: {
 max: 10,
 numRaters: 79,
 average: "9.1",
 min: 0
}'''
myJson= json.dumps(jsons) # 编码数据
tagert=json.loads(myJson)#解析json格式,解出来是一个字典
print(type(tagert))
print(tagert["rating"]['max'])