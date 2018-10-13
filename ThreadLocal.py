import threading
localobj=threading.local()

def threadfunc(name):
    localobj.name=name
    print("localobj.name is %s"%name)

if __name__=='__main__':
    t1=threading.Thread(target=threadfunc(name='yang'))
    t2=threading.Thread(target=threadfunc(name='zhi'))
    t3=threading.Thread(target=threadfunc(name='guang'))
    t1.start()
    t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()