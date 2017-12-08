#coding=utf-8


import sys
def test():
    while True:
        try:
            x=int(input("请输入一个数字:"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again  ")
        except (RuntimeError,TypeError,NameError):
            pass
def test1():
    try:
        f=open('myfile.txt')
        s=f.readline()
        i=int(s.strip())
    except OSError as err:
        print("OS error:{0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
#test1()

def test2():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

#test2()
