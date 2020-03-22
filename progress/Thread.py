
# coding: utf-8

# In[12]:


import multiprocessing as mp

def job(q, a, d):
    res = 0
    for i in range(1000):
        res += i + i**2 + i**3
    q.put(res) # queue


if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.g


# In[ ]:


import multiprocessing as mp

# share memery
value = mp.Value('d', 1)
array = mp.Array('i', [1, 2, 3])


# In[5]:


import multiprocessing as mp
import time
def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # 获取共享内存
        print(v.value)
    l.release() # 释放

def multicore():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job, args=(v,3,l)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()


# In[10]:


import threading

def thread_job():
    print("This is an added Thread, number is %s"% threading.current_thread)
    
def main():
    added_thread = threading.Thread(target = thread_job)
    added_thread.start()
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())
    
if __name__ == '__main__':
    main()


# In[15]:


# 多线程
import threading
import time

def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish \n")
    
def thread_job2():
    print("T2 start\n")
    print("T2 finish \n")
def main():
    added_thread = threading.Thread(target = thread_job, name = "T1")
    thread2 = threading.Thread(target = thread_job2, name = "T2" )
    added_thread.start()
    thread2.start()
    added_thread.join()
    thread2.join()
    print("all done\n")
    
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())
    
if __name__ == '__main__':
    main()


# In[ ]:


import threading
import time

from queue import Queue

def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading():
    q =Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name___=='__main__':
    multithreading()


# In[1]:


import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)


# In[ ]:


import threading

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()

if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

