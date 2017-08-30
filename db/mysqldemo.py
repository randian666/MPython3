#!/usr/bin/env python3
import pymysql

# 打开数据库连接

conn = pymysql.connect(host='192.168.166.30',port= 3359,user = 'giftshow_rw',passwd='giftshow_rw',db='giftshop') #db：库名
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)
cursor.close()

# 创建表
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入数据
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
conn.commit()
cursor.close()

#查询数据
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()

# 关闭数据库连接
conn.close()