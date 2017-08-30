#!/usr/bin/env python3
import sys
import time, datetime

if (len(sys.argv) == 2) :
    thisday = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
else :
    thisday = datetime.datetime.now()

delta1 = datetime.timedelta(days=-1)
historyday1 = (thisday + delta1).strftime('%Y-%m-%d')
print("historyday1=",historyday1)
list_third_names=['rangehood','stoves','waterheater','gaswaterheater','paneltv','airconditioning','refrigerator','washing'];#三级分类
for tag in list_third_names:
    print(tag)