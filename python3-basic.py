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


##oop###01 # -*- coding: utf-8 -*-
##oop###01 import os
##oop###01 class Student(object):
##oop###01     def __init__(self,name,score):
##oop###01         self.name = name
##oop###01         self.score =score
##oop###01     def set_score(self,score):
##oop###01         self.score =score
##oop###01     def print_score(self):
##oop###01         print('Student %s\'s score is %s' %(self.name,self.score))
##oop###01
##oop###01 def OOP01MAIN():
##oop###01     foo = Student('foo',66)
##oop###01     foo.print_score()
##oop###01     foo.set_score(91)
##oop###01     foo.print_score()
##oop###01
##oop###01 if __name__ == '__main__':
##oop###01     OOP01MAIN()
##oop###01



###copy-file-op01### #https://docs.python.org/3/library/shutil.html
###copy-file-op01### #https://www.geeksforgeeks.org/python-shutil-copy-method/
###copy-file-op01### # -*- coding: utf-8 -*-
###copy-file-op01### # Python program to explain shutil.copy() method
###copy-file-op01###
###copy-file-op01### # importing shutil module
###copy-file-op01### import shutil
###copy-file-op01###
###copy-file-op01### # Source path
###copy-file-op01### source = "/home/Michael/Documents/file.txt"
###copy-file-op01###
###copy-file-op01### # Destination path
###copy-file-op01### destination = "/home/Michael/Documents/dest.txt"
###copy-file-op01###
###copy-file-op01### # Copy the content of
###copy-file-op01### # source to destination
###copy-file-op01###
###copy-file-op01### try:
###copy-file-op01###     shutil.copy(source, destination)
###copy-file-op01###     print("File copied successfully.")
###copy-file-op01###
###copy-file-op01### # If source and destination are same
###copy-file-op01### except shutil.SameFileError:
###copy-file-op01###     print("Source and destination represents the same file.")
###copy-file-op01###
###copy-file-op01### # If there is any permission issue
###copy-file-op01### except PermissionError:
###copy-file-op01###     print("Permission denied.")
###copy-file-op01###
###copy-file-op01### # For other errors
###copy-file-op01### except:
###copy-file-op01###     print("Error occurred while copying file.")
###copy-file-op01###




###function-styple-map-reduce01### # https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
###function-styple-map-reduce01### # -*- coding: utf-8 -*-
###function-styple-map-reduce01### from datetime import datetime
###function-styple-map-reduce01### from functools import reduce
###function-styple-map-reduce01### DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
###function-styple-map-reduce01###
###function-styple-map-reduce01###
###function-styple-map-reduce01### def str2int(s):   ###map-reduce function
###function-styple-map-reduce01###
###function-styple-map-reduce01###     def fn(x, y):
###function-styple-map-reduce01###         return x * 10 + y
###function-styple-map-reduce01###
###function-styple-map-reduce01###     def char2num(s):
###function-styple-map-reduce01###         return DIGITS[s]
###function-styple-map-reduce01###     return reduce(fn, map(char2num, s))
###function-styple-map-reduce01###
###function-styple-map-reduce01###
###function-styple-map-reduce01### def f(x):      ###map function 01
###function-styple-map-reduce01###     return x * x
###function-styple-map-reduce01###
###function-styple-map-reduce01### def main():
###function-styple-map-reduce01###     print (list(map(str,   [1, 2,  3,  4,  5,  6])))  ###map02,shift int to string
###function-styple-map-reduce01###
###function-styple-map-reduce01###     r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
###function-styple-map-reduce01###     print (list(r))      ###map
###function-styple-map-reduce01###
###function-styple-map-reduce01###     print (str2int('15638'))   ###map-reduce call
###function-styple-map-reduce01###
###function-styple-map-reduce01### if __name__ == '__main__':
###function-styple-map-reduce01###     main()

