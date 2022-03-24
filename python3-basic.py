'''
###url
https://pythongeeks.org/python-unit-testing/

###code
 import unittest

 def div(a,b):
    return a/b


 class TestMethods(unittest.TestCase):
  def setUp(self): #Function that runs before each test to set any pre-requisites
    pass

  def test_abs(self):
    self.assertEqual( abs(-5), 5) #tests if the absolute value of -5 is 5

  def test_pow(self):      #tests if 2 to the power of 5 is 32
    self.assertEqual(pow(2,4),32)   ####error here

  # Tests and returns TRUE if the boolean value is non empty or non 0
  # or else returns False.
  def test_bool(self):
    self.assertTrue(bool(5))
    self.assertFalse(bool(''))

  # Returns true if the string splits and matches
  # the given output.
  def test_div(self):
    s = 'hello world'
    self.assertEqual(div(2,5),0.4)
    with self.assertRaises(ZeroDivisionError):
      div(2,0)

 if __name__ == '__main__':
    unittest.main()

###result
$> python3 unittest01.py
...F
======================================================================
FAIL: test_pow (__main__.TestMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest01.py", line 15, in test_pow
    self.assertEqual(pow(2,4),32)
AssertionError: 16 != 32

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)

'''

'''
###https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python
import doctest


def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    """
    return a * b

doctest.testmod()



def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word.

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2

    >>> count_vowels('Manila')
    3

    >>> count_vowels('Istanbul')
    3
    """
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels

if __name__ == "__main__":
    import doctest
    doctest.testmod()


###result(all correct)
$ python3 doctest01.py -v
Trying:
    add(2, 3)
Expecting:
    5
ok
Trying:
    add(0, 0)
Expecting:
    0
ok
Trying:
    count_vowels('Cusco')
Expecting:
    2
ok
Trying:
    count_vowels('Manila')
Expecting:
    3
ok
Trying:
    count_vowels('Istanbul')
Expecting:
    3
ok
1 items had no tests:
    __main__
2 items passed all tests:
   2 tests in __main__.add
   3 tests in __main__.count_vowels
5 tests in 3 items.
5 passed and 0 failed.
Test passed.




###result(with error):
$ python3 doctest01.py  -v
Trying:
    add(2, 3)
Expecting:
    5
**********************************************************************
File "doctest01.py", line 34, in __main__.add
Failed example:
    add(2, 3)
Expected:
    5
Got:
    6
Trying:
    add(0, 0)
Expecting:
    0
ok
Trying:
    count_vowels('Cusco')
Expecting:
    1
**********************************************************************
File "doctest01.py", line 8, in __main__.count_vowels
Failed example:
    count_vowels('Cusco')
Expected:
    1
Got:
    2
Trying:
    count_vowels('Manila')
Expecting:
    3
ok
Trying:
    count_vowels('Istanbul')
Expecting:
    3
ok
1 items had no tests:
    __main__
**********************************************************************
2 items had failures:
   1 of   2 in __main__.add
   1 of   3 in __main__.count_vowels
5 tests in 3 items.
3 passed and 2 failed.
***Test Failed*** 2 failures.



'''


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
