#!/usr/bin/env python3

'''

协程，又称微线程，纤程。英文名Coroutine。

子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。

子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

Python对协程的支持是通过generator实现的。

'''

def consumer():
    r=''
    while True:
        n=yield r;
        print('consumer %s'%n)
        r='OK'

def produce(c):
    c.send(None) #启动生成器
    n=0;
    while n<5:
        n=n+1;
        print('produce %s'%n)
        t=c.send(n)
        print('consumer result %s'%t)
    c.close();


c=consumer();
produce(c)


# 首先调用c.send(None)启动生成器；
#
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
# produce拿到consumer处理的结果，继续生产下一条消息；
#
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

import asyncio
import threading
@asyncio.coroutine
def hello():
    print("hello world! %s"%threading.current_thread())
    r=yield from asyncio.sleep(1)
    print("hello again! %s"%threading.current_thread())

#先获取EventLoop
loop=asyncio.get_event_loop();
#执行协程（coroutine）
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks));
loop.close();

# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
#
# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
#
# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await

# async def hello1():
#     print("Hello world!")
#     r = await asyncio.sleep(1)
#     print("Hello again!")
#
# lo=asyncio.get_event_loop();
# tasks=[hello1(),hello1()]
# lo.run_until_complete(hello1())
# lo.close()


