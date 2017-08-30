#!/usr/bin/env python3
'''

由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，
线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
'''
import time,threading,multiprocessing
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    i=0;
    while i<5:
        i=i+1;
        print('thread %s >>> %s' % (threading.current_thread().name, i))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def thread_create():
    print('thread %s is running...' % threading.current_thread().name)
    t=threading.Thread(target=loop,name='thread1'); #新建一个线程
    t.start();  #启动一个线程
    t.join();  #等待线程执行完毕
    print('thread %s ended.' % threading.current_thread().name)

balance=0
# 创建一个锁就是通过threading.Lock()来实现
lock = threading.Lock()
def change_it(n):
    #设置全局变量
    global balance;
    balance=balance+n;
    balance=balance-n;

def thread_run():
    for i in range(100000):
        #获取锁 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止
        lock.acquire();
        try:
            change_it(i)
        finally:
            #释放锁
            lock.release();


def craete_th():
    th=threading.Thread(target=thread_run,name=(10,))
    th1 = threading.Thread(target=thread_run, name=(20,))
    th.start();
    th1.start();
    th.join()
    th1.join()
    print(balance)

if __name__ == '__main__':
    # thread_create();
    craete_th();
    print("cpu数量：",multiprocessing.cpu_count())

# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
#
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。


