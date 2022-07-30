'''
Importing data from a MySQL database into Pandas dataframe
https://pythontic.com/pandas/serialization/mysql
https://www.geeksforgeeks.org/how-to-print-dataframe-in-python-without-index/
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
https://stackoverflow.com/questions/48641632/extracting-specific-columns-from-pandas-dataframe

adan@ha1:~$ cat pa02.py
from sqlalchemy import create_engine
import pymysql
import pandas as pd

sqlEngine       = create_engine('mysql+pymysql://root:my-secret@127.0.0.1:5306', pool_recycle=3600)
dbConnection    = sqlEngine.connect()
basic           = pd.read_sql("select id as uid,name as User from Student.basic", dbConnection);
subjective      = pd.read_sql("select id as sid,name as Sub from Student.subjective", dbConnection);
score           = pd.read_sql("select * from Student.score", dbConnection);

pd.set_option('display.expand_frame_repr', False)
df1 = pd.merge(score, basic, on='uid', how='inner')
df2 = pd.merge(subjective,df1, on = 'sid' ,how = 'inner')
print ("before join:")
print (basic)
print (subjective)
print (score)

print ("")
print ("joined:")

### cols = [1,2,3,4]
### df = df[df.columns[cols]]
### the same below

print(df2[["User","Sub","score"]].to_string(index=False))
dbConnection.close()

adan@ha1:~$ python3 pa02.py
before join:
   uid   User
0    1  zhang
1    2   wang
2    3    xia
3    4   Yang
4    5   Tang
   sid   Sub
0   11   CHN
1   22   ENG
2   33  Math
   uid  sid  score
0    1   11     66
1    1   22     77
2    2   22     88
3    2   11     99
4    3   33     98

joined:
 User  Sub  score
zhang  CHN     66
 wang  CHN     99
zhang  ENG     77
 wang  ENG     88
  xia Math     98

'''


'''
[root@c1 python]# cat db02.py
###https://pypi.org/project/PyMySQL/
###https://zetcode.com/python/pymysql/ ***
import pymysql
import pymysql.cursors

###0x1 with cursor

con = pymysql.connect(host='127.0.0.1',
        user='root',
        password='my-secret',
        db='testdb',
        cursorclass=pymysql.cursors.DictCursor)

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM cities')

        rows = cur.fetchall()

        for row in rows:
            print(row['id'], row['name'])

finally:

    con.close()


###0x2 fetchall
con = pymysql.connect(host='127.0.0.1', user='root',password='my-secret', db='testdb')
try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM cities')

        rows = cur.fetchall()

        for row in rows:
            print(f'{row[0]} {row[1]} {row[2]}')

finally:

    con.close()

###0x3 get version
con = pymysql.connect(host='127.0.0.1', user='root',password='my-secret', db='testdb')
try:
    with con.cursor() as cur:

        cur.execute('SELECT VERSION()')

        version = cur.fetchone()

        print(f'Database version: {version[0]}')

finally:

    con.close()

[root@c1 python]# python3 db02.py
1 Bratislava
2 Budapest
3 Prague
4 Warsaw
5 Los Angeles
6 New York
7 Edinburgh
8 Berlin
1 Bratislava 432000
2 Budapest 1759000
3 Prague 1280000
4 Warsaw 1748000
5 Los Angeles 3971000
6 New York 8550000
7 Edinburgh 464000
8 Berlin 3671000
Database version: 5.7.24
'''


'''
https://zetcode.com/python/pymysql/
'''


'''
###padas
###url
##install
$> pip3 install matplotlib -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
$> pip3  install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
$> pip3 install pandas -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
$> pip3  install seaborn scipy  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

[root@c1 python]# cat padas02.py
# importing pandas
import pandas as pd

# Creating dataframe a
a = pd.DataFrame()

# Creating Dictionary
d = {'id': [1, 2, 10, 12],
        'name': ['zhao', 'qian', 'sun', 'li']}

a = pd.DataFrame(d)
print('dataframe a is:')
print(a)
# Creating dataframe b
b = pd.DataFrame()

# Creating dictionary
d = {'id': [1, 2, 9, 8],
        'city': ['luoyang', 'changan', 'youzhou', 'jinling']}
b = pd.DataFrame(d)
print('dataframe b is:')
print(b)
# inner join
df = pd.merge(a, b, on='id', how='inner')

# display dataframe
print('dataframe join a and b is:')
print (df)

[root@c1 python]# python3 padas02.py
dataframe a is:
   id  name
0   1  zhao
1   2  qian
2  10   sun
3  12    li
dataframe b is:
   id      city
0   1   luoyang
1   2  changan
2   9   youzhou
3   8   jinling
dataframe join a and b is:
   id  name      city
0   1  zhao   luoyang
1   2  qian  changan


'''


'''
###data merge and join
###https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/



'''
###re module
[root@c1 python]# cat re1.py
import re
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'),'###use multiple delimeter')
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print('m0 is: %s' % m.group(0),'###return all groups')
print('m1 is: %s' % m.group(1),'###return one group')

print(re.match(r'^(\d+)(0*)$', '102300').groups(),'###greedy match,return all groups')   ##greedy match
print(re.match(r'^(\d+?)(0*)$', '102300').groups(),'###non-greedy match,return all groups')

re_telephone = re.compile(r'^(\d{1,3})-(\d{3,8})-(\d{1,3})$')  ###compile for latter use,more effient
print(re_telephone.match('10-12345-12').group(1),'###return only one group')
print(re_telephone.match('10-22345-12').group(2),'###return only one group')

[root@c1 python]# python3 re1.py
['a', 'b', 'c', 'd'] ###use multiple delimeter
<re.Match object; span=(0, 9), match='010-12345'>
m0 is: 010-12345 ###return all groups
m1 is: 010 ###return one group
('102300', '') ###greedy match,return all groups
('1023', '00') ###non-greedy match,return all groups
10 ###return only one group
22345 ###return only one group

'''


'''
###asyncio
###url https://realpython.com/async-io-python/

###version
[root@c1 python]# python3
Python 3.9.6 (default, Mar 26 2022, 07:32:44)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux

###code
[root@c1 python]# cat a1.py
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
async def main():
    await asyncio.gather(count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    #loop = asyncio.get_event_loop()    ###old style before v3.5;same as asyncio.run(main())
    #loop.run_until_complete(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


###result,only cost 1 second,not 2second.
[root@c1 python]# python3 a1.py
One
One
Two
Two
/root/work/python/a1.py executed in 1.00 seconds.



###another example1
###https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python

###code:
[root@c1 python]# cat a4.py
import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')



##result
[root@c1 python]# python3.9 a4.py
Task A: Computing 0+1
Time: 0.00
Task B: Computing 0+1
Time: 0.00
Task A: Computing 1+2
Time: 1.00
Task B: Computing 1+2
Time: 1.00
Task A: Sum = 3

Task B: Computing 3+3
Time: 2.01
Task B: Sum = 6

Time: 3.01 sec




###another example2


##https://tutorialedge.net/python/concurrency/getting-started-with-asyncio-python/

[root@c1 python]# cat a3.py
import asyncio
import random

async def myCoroutine(id):
    process_time = random.randint(1,5)
    await asyncio.sleep(process_time)
    print("Coroutine: {}, has successfully completed after {} seconds".format(id, process_time))

async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(myCoroutine(i)))

    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

[root@c1 python]# python3 -V
Python 3.9.6


[root@c1 python]# python3 a3.py
Coroutine: 1, has successfully completed after 1 seconds
Coroutine: 6, has successfully completed after 1 seconds
Coroutine: 9, has successfully completed after 1 seconds
Coroutine: 0, has successfully completed after 2 seconds
Coroutine: 8, has successfully completed after 2 seconds
Coroutine: 3, has successfully completed after 3 seconds
Coroutine: 5, has successfully completed after 3 seconds
Coroutine: 4, has successfully completed after 4 seconds
Coroutine: 2, has successfully completed after 5 seconds
Coroutine: 7, has successfully completed after 5 seconds

'''



'''
###install python3 on centos
###https://tecadmin.net/install-python-3-7-on-centos/
$> yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel
$> cd /usr/src   && wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz
$> tar vzxf Python-3.7.11.tgz
$> cd Python-3.7.11 && ./configure --enable-optimizations  && make altinstall

'''

'''
##url https://www.geeksforgeeks.org/coroutine-in-python/
##https://stackabuse.com/coroutines-in-python/
###code
#-*- coding: utf-8 -*-
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try :
        while True:
                name = (yield)
                if prefix in name:
                    print(name)
    except GeneratorExit:
            print("Closing coroutine!!")

# calling coroutine, nothing will happen
corou = print_name("Dear")

# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()

# sending inputs
corou.send("Atul")      ###This will NOT print anything due to  if prefix in name:
corou.send("Dear Atul") ###This will print Dear Atul
corou.close()
print()

###result
$ python3 coroutins.py
Searching prefix:Dear
Dear Atul
Closing coroutine!!

###example 2
#-*- coding: utf-8 -*-
from datetime import datetime
def producer(cor):
    n = 1
    cor.send(None)
    while n < 100:
        cor.send(n)
        n = n * 2

#@coroutine
def my_filter(num, cor):
    cor.send(None)
    while True:
        n = (yield)
        if n < num:
            cor.send(n)

#@coroutine
def printer():
    while True:
        n = (yield)
        print(n)
now=datetime.now()
print('%s: ' %now)
prnt = printer()
filt = my_filter(50, prnt)
producer(filt)


##result
$ python3 c1.py
2022-01-21 17:31:01.378527:
1
2
4
8
16
32

'''



'''
###yield
###url
https://www.guru99.com/python-yield-return-generator.html
https://www.geeksforgeeks.org/python-yield-keyword/

Advantages of yield:

Since it stores the local variable states, hence overhead of memory allocation is controlled.
Since the old state is retained, the flow doesn’t start from the beginning and hence saves time.

Disadvantages of yield:

Sometimes, the use of yield becomes erroneous if the calling of function is not handled properly.
Time and memory optimization has a cost of complexity of code and hence sometimes hard to understand the logic behind it.

###code
 # -*- coding: utf-8 -*-
 def getFibonnaciSeries(fin):
     c1, c2 = 0, 1
     count = 0
     while count < fin:
         yield c1
         c3 = c1 + c2
         c1 = c2
         c2 = c3
         count += 1


 fin = getFibonnaciSeries(7)    ##use list style
 print()
 print("Start from list:")
 print(list(fin))
 print()

 fin = getFibonnaciSeries(7)    ###only return generator memory address,Must recall
 print("only print memory address:")
 print(fin)

 fin = getFibonnaciSeries(7)    ###use for-loop style,Must recall
 print()
 print("from for-loop style:")
 for i in fin:
     print(i)

 fin = getFibonnaciSeries(7)    ###use next() style,Must recall
 print("from next() style:")
 print(next(fin))
 print(next(fin))
 print(next(fin))
 print(next(fin))
 print(next(fin))

 ########
 def test(n):
     return n*n

 def getSquare(n):
     for i in range(n):
         yield test(i)    ###calling function

 sq = getSquare(6)
 print()
 print("Example calling function result:",list(sq))

###result

$ python3 yieldfun.py

Start from list:
[0, 1, 1, 2, 3, 5, 8]

only print memory address:
<generator object getFibonnaciSeries at 0x7f76af2bcbd0>

from for-loop style:
0
1
1
2
3
5
8
from next() style:
0
1
1
2
3

Example calling function result: [0, 1, 4, 9, 16, 25]

'''



'''
###logging
###url https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3


###code

import logging

 logger1 = logging.getLogger("module_1")
 logger2 = logging.getLogger("module_2")


 logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )


 class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logging.debug("Pizza created: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        logging.debug("Made {} {} pizza(s)".format(quantity, self.name))

    def eat(self, quantity=1):
        logging.debug("Ate {} pizza(s)".format(quantity, self.name))

 logger1.debug("Module 1 debugger")
 logger2.debug("Module 2 debugger")

 pizza_01 = Pizza("Sicilian", 18)
 pizza_01.make(5)
 pizza_01.eat(4)

 pizza_02 = Pizza("quattro formaggi", 16)
 pizza_02.make(2)
 pizza_02.eat(2)


###result

$ cat test.log
2022-03-24 11:27:38,405:DEBUG:Module 1 debugger
2022-03-24 11:27:38,405:DEBUG:Module 2 debugger
2022-03-24 11:27:38,405:DEBUG:Pizza created: Sicilian ($18)
2022-03-24 11:27:38,405:DEBUG:Made 5 Sicilian pizza(s)
2022-03-24 11:27:38,406:DEBUG:Ate 4 pizza(s)
2022-03-24 11:27:38,406:DEBUG:Pizza created: quattro formaggi ($16)
2022-03-24 11:27:38,406:DEBUG:Made 2 quattro formaggi pizza(s)
2022-03-24 11:27:38,406:DEBUG:Ate 2 pizza(s)

'''



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
