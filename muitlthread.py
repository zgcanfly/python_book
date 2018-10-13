#coding:utf-8
import threading,time


balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in  range(10000):
        change_it(n)



thread1=threading.Thread(target=run_thread,args=(5,))
thread2=threading.Thread(target=run_thread,args=(8,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(balance)