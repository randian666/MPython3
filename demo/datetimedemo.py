#!/usr/bin/env python3

import sys
import time, datetime

if (len(sys.argv) == 4) :
    list_thisday=sys.argv[1].split('-')
    # thisday = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
    thirdid=sys.argv[2]
    tag=sys.argv[3]
else :
    thisday = list(datetime.datetime.now()) #默认当天
    thirdid='1300'  #默认油烟机
    tag='rangehood' #分区tag

for thisday in list_thisday:
    thisday=datetime.datetime.strptime(thisday, '%Y%m%d')
    delta1 = datetime.timedelta(days=-1)
    historyday1 = (thisday + delta1).strftime('%Y-%m-%d')

    delta15 = datetime.timedelta(days=-15)
    historyday15 = (thisday + delta15).strftime('%Y-%m-%d')

    add25=datetime.timedelta(days=24)
    future1=thisday.strftime('%Y-%m-%d')
    future25=(thisday+add25).strftime('%Y-%m-%d')

    print("thisday=",thisday)
    print("historyday1=",historyday1)
    print("historyday15=",historyday15)
    print("future1=",future1)
    print("future25=",future25)
    print("thirdid=",thirdid)
    print("tag=",tag)
    print("-----------------------------------------")

