import sys,time

def ProgressBar(Time):
    num=Time/100
    for i in range(100):
        if i == 99:
            sys.stdout.flush()
            sys.stdout.write('\r%s%s' % ((i + 1),''))
        else:
            sys.stdout.write('\r%s%s'%((i+num),'%'))
            sys.stdout.flush()
        time.sleep(0.1)

if __name__=="__main__":
    ProgressBar(20)
