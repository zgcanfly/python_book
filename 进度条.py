import sys,time

for i in range(100):
    if i == 99:
        sys.stdout.flush()
        sys.stdout.write('\r%s%s' % ((i + 1),''))
    else:
        sys.stdout.write('\r%s%s'%((i+0.2),'%'))
        sys.stdout.flush()
    time.sleep(0.1)