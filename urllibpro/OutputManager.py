#!/usr/bin/env python3
from elasticsearch import Elasticsearch

class OutputManager(object):
    def __init__(self):
        self._es=Elasticsearch([{'host':'203.76.214.3','port':9000}])
    def _add_data_to_es(self,data):
        if data is None:
            return
        # self._es.indices.create(index="douban")
        self._es.index(index="douban",doc_type="tushu",body={"url":data["url"],"title":data["title"],"content":data["content"]})
        # res = self._es.get(index="douban", doc_type="tushu", id=01)
        # 根据url查询
        res = self._es.search(index="douban",doc_type="tushu",body={"query": {"match": {'url':data["url"]}}})
        print(res)

if __name__ == '__main__':
    out=OutputManager()
    out._add_data_to_es(data={"url":"www.baidu.com","title":"放风筝的人","content":"555555555555555555555555"})
