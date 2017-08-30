#!/usr/bin/env python3
'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程

由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象
'''

from multiprocessing import Process,Pool,Queue
import os, time, random
def func_proc(name):
    print("Run child process %s (%s)" % (name,os.getpid()))
def create_proc():
    print("parents process is %s" % os.getpid())
    p = Process(target=func_proc, args=('test',))  # 创建一个子进程
    print("child process will start")
    p.start();  # 创建一个Process实例，用start()方法启动
    p.join();  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print("child process end.")
def func_pool_proc(name):
    print("Run task %s (%s)" % (name, os.getpid()))
    start=time.time();
    time.sleep(random.random()*3)
    end=time.time();
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def create_pool_proc():
    print("parents process is %s" % os.getpid())
    p=Pool(4);
    for i in range(5):
        p.apply_async(func_pool_proc,args=(i,))
    p.close() #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()
    print('All subprocesses done.')
def proc_write(q):
    print('Process to write: %s' % os.getpid())
    for v in ['a','b','c']:
        q.put(v)
        time.sleep(random.random())
def proc_read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value=q.get(True);
        print('Get %s from queue.' % value)
'''
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
'''
def proc_queue():
    # 父进程创建Queue，并传给各个子进程：
    q=Queue();
    wr=Process(target=proc_write,args=(q,))
    re = Process(target=proc_read,args=(q,))
    # 启动子进程wr，写入:
    wr.start();
    # 启动子进程re，读取:
    re.start();
    # 等待wr结束:
    wr.join()
    # re进程里是死循环，无法等待其结束，只能强行终止:
    re.terminate()


if __name__=="__main__":
    # create_proc();
    # create_pool_proc();
    proc_queue();
    # print(random.random())