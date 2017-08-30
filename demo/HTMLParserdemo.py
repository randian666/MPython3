#!/usr/bin/env python3

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False

    def _attr(self,attrlist, attrname):
        for attr, value in attrlist:
            if attr == attrname:
                return value;
        return None
    def handle_starttag(self, tag, attrs):
        if tag=='a' and self._attr(attrs,"id")=="asdf":
            self.flag=True;

    def handle_endtag(self, tag):
        pass;

    def handle_startendtag(self, tag, attrs):
        pass;

    def handle_data(self, data):
        if self.flag==True:
            print(data)

    def handle_comment(self, data):
        pass;

    def handle_entityref(self, name):
        pass;

    def handle_charref(self, name):
        pass;

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<p/>
<!-- test html parser -->
    <p>Some <a href=\"#\" id="asdf">html</a> HTML&nbsp;tutorial...<br>END</p>
    <p>ssssssssssssssssss</p>
</body></html>''')

# 练习
#
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

class pythonparse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.h3_title=False;
        self.h3_time=False;
        self.h3_location=False;
        self._event_title = []
        self._event_location = []
        self._ecent_time = []
    def _attr(self,attrlist, attrname):
        for attr, value in attrlist:
            if attr == attrname:
                return value;
        return None
    def handle_starttag(self, tag, attrs):
        if tag=='h3' and self._attr(attrs,"class")=="event-title":
            self.h3_title=True
        if tag == 'time' and self._attr(attrs, "datetime"):
            self.h3_time = True;
        if tag == 'span' and self._attr(attrs, "class") == 'event-location':
            self.h3_location = True
    def handle_data(self, data):
        if self.h3_title==True:
            self._event_title.append(data);
            self.h3_title=False;
        if self.h3_time==True:
            self._ecent_time.append(data);
            self.h3_time=False;
        if self.h3_location==True:
            self._event_location.append(data);
            self.h3_location = False;
    @property
    def data(self):
        result=[];
        for i,title in (enumerate(self._event_title)):
            dic = {}
            dic["title"]=self._event_title[i];
            dic["time"]=self._ecent_time[i];
            dic["location"]=self._event_location[i];
            result.append(dic);
        return result;

def getHtml():
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read().decode('utf-8')
    return data
parser = pythonparse()
parser.feed(getHtml())
print(parser.data)