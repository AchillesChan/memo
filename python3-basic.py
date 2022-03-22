''' basic

# -*- coding: utf-8 -*-

import os
from datetime import datetime
def main():
    print ('Hello world')
    print ('=' * 15)
    print ('')

    foo(-89,99)

    print ('Current working directory is ' + os.getcwd())

    counter = 0
    counter += 1
    print ('counter=',counter)

    food = ['Apple','Orange']
    for i in food:
        print ('I like to eat ' + i )

    now = datetime.now()
    st = now.timestamp()
    print('timestamp is %s' % st)

    L   =   ['User', 'Sarah',    'Tracy',    'Bob',  'Jack']  ###slice
    print(L[1:3])
    print (os.name)
    print (os.uname())
    print (os.environ.get('PATH'))
    print (os.environ.get('HOME'))
    print (os.path.abspath('.'))

    os.mkdir('/home/User/work/python/test')
    os.rmdir('/home/User/work/python/test')

def foo(p1,p2):
    res = p1 + p2
    print ('%s plus %s is equal to %s' %(p1,p2,res))
    if res <5:
        print ('foo')
    else:
        print ('bar')
    return res
    ''' this  is a multi-line
    comments.'''

if __name__ == '__main__':
    main()

'''




'''oop program

# -*- coding: utf-8 -*-
import os
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score =score
    def set_score(self,score):
        self.score =score
    def print_score(self):
        print('Student %s\'s score is %s' %(self.name,self.score))
##oop###01
def OOP01MAIN():
    foo = Student('foo',66)
    foo.print_score()
    foo.set_score(91)
    foo.print_score()
##oop###01
if __name__ == '__main__':
    OOP01MAIN()

'''




'''

#https://docs.python.org/3/library/shutil.html
#https://www.geeksforgeeks.org/python-shutil-copy-method/
# -*- coding: utf-8 -*-
# Python program to explain shutil.copy() method
###copy-file-op01###
# importing shutil module
import shutil
###copy-file-op01###
# Source path
source = "/home/Michael/Documents/file.txt"
###copy-file-op01###
# Destination path
destination = "/home/Michael/Documents/dest.txt"
###copy-file-op01###
# Copy the content of
# source to destination
###copy-file-op01###
try:
    shutil.copy(source, destination)
    print("File copied successfully.")
###copy-file-op01###
# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")
###copy-file-op01###
# If there is any permission issue
except PermissionError:
    print("Permission denied.")
###copy-file-op01###
# For other errors
except:
    print("Error occurred while copying file.")

'''


'''
####Functional programming https://coolshell.cn/articles/10822.html

# -*- coding: utf-8 -*-
from datetime import datetime
from functools import reduce
import functools   ####partial function must import
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):   ###map-reduce function

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


def f(x):      ###map function 01
    return x * x

def is_odd(n):
    return n % 2 == 1

def main():
    r = map(f, [1, 32, 5, 6, 7, 8, 9])
    print (list(r))      ###map

    print (list(map(str,   [1, 2,  3,  4,  5,  6])))  ###map2,shift int to string
    print (sorted([1,9,-34,62,32],key=abs))
    print (sorted(['bob',  'about',    'Zoo',  'Credit'], key=str.lower,reverse=True))
    print (list(filter(is_odd, [1,2,3,4,5])))
    print (str2int('15638'))   ###map-reduce call

    max2=functools.partial(max,10)    ###apend default parameter 10 to the max2 function,here result is 10
    print (max2(5,6,9))

    int2 = functools.partial(int,base=2)
    print (int2('111100'))

    print (list(map(lambda x: x+7,[1,3,9])))  ###like def fun(x) return x+7

if __name__ == '__main__':
    main()

'''
