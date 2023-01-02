######Startmemoof pythondemo.py #######
######Start pythondemo.py #######
https://github.com/michaelliao/learn-python3
https://www.analyticsvidhya.com/blog/2021/06/15-pandas-functions-to-replicate-basic-sql-queries-in-python/
https://www.analyticsvidhya.com/blog/2021/06/join-the-dataframes-like-sql-tables-in-python-using-pandas/
https://stackoverflow.com/questions/42429023/how-can-i-perform-an-inner-join-with-two-object-arrays-in-javascript
https://stackoverflow.com/questions/54287262/joining-lists-in-python-3-like-sql-join

https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python
https://realpython.com/python-testing/

https://www.programiz.com/python-programming/break-continue
# program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1

    if (num % 2) == 0:
        continue           ###skip current ,enter next

    print(num)

# program to find first 5 multiples of 6

i = 1

while (i<=10):
    print('6 * ',(i), '=',6 * i)
    if i >= 5:
        break            ###terminal loop
    i = i + 1




https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888 ####parameters detail
##1 default parameters MUST point to none-variable object
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

>>> power(5)
25
>>> power(5, 3)
125

#special for list
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


###variable parameter
def calc(*numbers):   #with * then name
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

>>> calc(1, 2)
5
>>> calc()
0
>>> nums = [1, 2, 3]
>>> calc(*nums)
14

###keyword parameter
>>> def person(name, age, **kw):
...     print('name:', name, 'age:', age, 'other:', kw)
...
>>>
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'job': 'Engineer', 'gender': 'M'}
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'job': 'Engineer', 'city': 'Beijing'}
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

###named keyword parameter
>>> def person(name, age, *, city, job):   ####with * independly
...     print(name, age, city, job)
...
>>>
>>> person('Jack', 24, city='Beijing', job='Engineer')   ###MUST with paramter name
Jack 24 Beijing Engineer
>>>
>>>
>>> def person(name, age, *, city='Beijing', job):
...     print(name, age, city, job)
...
>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer






$ python3  ##tuple ,content can not be modified,no apped insert method
Python 3.4.6 (default, Mar 22 2017, 12:26:13) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> name=('Adan','Bob','Cindy')
>>> name
('Adan', 'Bob', 'Cindy')
>>> len(name)
3
>>> name(0)
'Adan'
>>> name(1)
'Bob'
>>> name(2)
'Cindy'
>>> name(3)
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      IndexError: list index out of range

>>> t
(1, 2, 3)
>>> t(0)=3   ##tuple ,content can not be modified,no apped insert method
  File "<stdin>", line 1
  SyntaxError: can't assign to function call
  >>> t
  (1, 2, 3)




>>> t=(1,)    ###for only one elements,MUST use this
>>> t
(1,)


>>> t   =   ('a',   'b',    ['A',   'B'])
>>> t[2][0] =   'X'
>>> t[2][1] =   'Y'
>>> t
('a',   'b',    ['X',   'Y'])



$ python3  ##list
Python 3.4.6 (default, Mar 22 2017, 12:26:13) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> name=['Adan','Bob','Cindy']
>>> name
['Adan', 'Bob', 'Cindy']
>>> len(name)
3
>>> name[0]
'Adan'
>>> name[1]
'Bob'
>>> name[2]
'Cindy'
>>> name[3]
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      IndexError: list index out of range

>>> name.append('Ele')
>>> name
['Adan', 'Bob', 'Cindy', 'Ele']
>>> name.insert(1,'Jia')
>>> name
['Adan', 'Jia', 'Bob', 'Cindy', 'Ele']
>>> name.pop()
'Ele'
>>> name
['Adan', 'Jia', 'Bob', 'Cindy']
>>> name.pop(1)
'Jia'
>>> name
['Adan', 'Bob', 'Cindy']
>>> name[1]='Yi'
>>> name
['Adan', 'Yi', 'Cindy']

>>> s=['python','java',['asp','php'],'scheme']    ###multiple demision
>>> s
['python', 'java', ['asp', 'php'], 'scheme']

>>> s[2][1]
'php'


###set
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}

>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}

>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}

>>> s.remove(4)
>>> s
{1, 2, 3}

>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}



所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'


当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：

####dict ->map
>>> d=  {'Michael':     95,     'Bob':  75,     'Tracy':        85}
>>> d['Michael']
95
>>> d['Adam']   =       67
>>> d['Adam']
67
>>> d['Jack']   =       90
>>> d['Jack']
90
>>> d['Jack']   =       88
>>> d['Jack']
88
>>> d['Thomas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Thomas'
>>> 'Thomas'    in d
False
>>> d.get('Thomas')
>>> d.get('Thomas',     -1)
-1
>>> d.pop('Bob')
75
>>> d
{'Adam': 67, 'Michael': 95, 'Jack': 88, 'Tracy': 85}


$> python3  ###variables
Python 3.4.6 (default, Mar 22 2017, 12:26:13) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a='abc'
>>> b=a
>>> a='xyz'
>>> print(b)
abc         ####because b point to abc(the content,not pointer of a)



####c embedding python###
https://dev.to/erikwhiting88/how-to-use-c-functions-in-python-7do

$ cat cfactorial.c
long factorial(int user_input) {
  long return_val = 1;
  long int i;
  if (user_input <= 0) {
    return -1;
        }
  else {
    for (i = 1; i <= user_input; i++) {
      return_val *= i;
    }
  }
  return return_val;
}

int main() {
  return 0;
}


$ cat pyfactorial.py
from ctypes import *
so_file = '/home/cfactorial.so'
cfactorial = CDLL(so_file)

def factorial(num):
  c_return = cfactorial.factorial(num)
  if (c_return != -1):
    return c_return
  else:
    return "C Function failed, check inputs"


$ gcc -fPIC -shared -o cfactorial.so cfactorial.c


$ ls cfa* pyfactorial.py
cfactorial.c  cfactorial.so  pyfactorial.py

$ python
Python 2.7.5 (default, Nov  6 2016, 00:28:07)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyfactorial as pf
>>> pf.factorial(3)
6
>>> pf.factorial(9)
362880
>>> pf.factorial(-2)
'C Function failed, check inputs'

####c embedding python###


http://ginstrom.com/scribbles/2009/09/14/easy-sftp-uploading-with-paramiko/ Easy SFTP uploading with paramiko

https://paramiko-docs.readthedocs.io/en/1.15/api/sftp.html
https://www.liaoxuefeng.com/ python教学


################generate OTP###########
https://www.geeksforgeeks.org/python-program-to-generate-one-time-password-otp/
--10
vm> #cat otp.py
# Importing random to generate
# random string sequence
import random

# Importing string library function
import string

def rand_pass(size):

    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                            string.digits)
                                            for n in range(size)])
    return generate_pass

if __name__ == "__main__" :
    print("OTP of 8 chars:", rand_pass(8))

--20
vm> # python otp.py
('OTP of 8 chars:', 'Bwixg7tO')

################generate OTP###########


###centos install 3.6 python####
sudo yum install centos-release-scl
sudo yum install rh-python36
scl enable rh-python36 bash
python --version
###centos install 3.6 python####

###pylint
--10 install
pip install pylint || sudo zypper install pylint || \
yum install pylint

--20 run
https://www.mantidproject.org/How_to_run_Pylint
pylint your.py

###pylint

#########sftp update file#####
1 link
http://mingxinglai.com/cn/2015/06/paramiko/
https://paramiko-docs.readthedocs.io/en/1.15/api/sftp.html


2 code

# -*- coding:utf-8 -*-
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ip-or-host" ,port_number , "user", "passwd")

sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
sftp = ssh.open_sftp()
sftp.chdir('operation_dir')
sftp.put('/exact/path/2/local_file', 'remote_file')


#########sftp update file#####






####read staff from stdin to var,stdout to file

#-*- coding:utf-8 -*-
import os
def main():
    file_handle = open("1.txt","a")                              ###define open file's handle,append style,"w" is rewrite style
    name = raw_input("waht's your name:")                        ###keyboard input to name var
    print >>file_handle, ("Nice to meet you " + name +"!")       ###Output to file,not support '>' operation
    file_handle.close()
if __name__ == '__main__':
    main()

####read staff from stdin to var,stdout to file

#####call system cmd and get return code,suppress stdout and errout
# -*- codingi:utf-8 -*-
import os
import subprocess
def ping_check(var_hostname):                                                                     ####can not use - to link
    devnull = open(os.devnull,'w')                                                                ####link to /dev/null
    response = subprocess.call \                                                                  ####use \ span lines
    (["ping","-c","1",var_hostname],stdout=devnull,stderr=devnull)                                ####PATT CMD PARA var
    return response

def main():
    flag = ping_check("192.168.5.3")
    print flag

if __name__ == '__main__':
    main()
#####call system cmd and get return code,suppress stdout and errout


#########function call and return
# -*- codingi:utf-8 -*-

def main():
    sum = add(3,5)
    print sum
def add(foo,bar):
    res = foo + bar
    return res

if __name__ == '__main__':
    main()

#########function call and return






# -*- coding: utf-8 -*-
# 给 Python 初学者的超快速脚本解说

import os

def main():
    print '你好, 世界!'
    print "单引号，双引号，其实是一码事"
    print '字符串内的引号需被转义(如 O\'Neil)'
    print "换个不同的引号就无需转义了(看 O'Neil)"

    print """三引号（亦可以是三个单引号）可以安全地处理单双引号混用，例如：
    O'Neil 说: "姚明太瘦。"
    姚明说: "O'Neil 太老。"
而且还能跨行，跨行后的格式也能被保留。
"""

    print '=' * 10
    print '这将直接执行', os.getcwd()

    add(5, 10)

    counter = 0
    counter += 1

    food = ['苹果', '杏子', '李子', '梨']
    for i in food:
        print '俺就爱整只: %s' % i

    print '从0数到9'
    for i in range(10):
        print i




def add(param1, param2):
    """做了点加法.
喔，其实还胡乱判断了一气。
    """
    # 这也是一个注释。
    res = param1 + param2
    print '%s + %s = %s' %(param1, param2, res)

    if res < 50:
        print '这个这个'
    elif res >= 50 and (param1 == 42 or param2 == 24):
        print '那个那个'
    else:
        print '嗯哼...'

    return r es      # 注释还可以像这样直接跟在一句代码的后面

if __name__ == '__main__':
    main()

###########call linux command in python##########
$>cat dp.py   ##code
# -*- coding: utf-8 -*-

import subprocess

def main():
    subprocess.call("date")
    subprocess.call(["ls","-l","/home/Michael/dp.py"])

if __name__ == '__main__':
    main()


$> python dp.py  ####run
Tue Jan 16 15:19:08 CST 2018
-rwxr-xr-x 1 Michael users 178 Jan 16 15:18 /home/Michael/dp.py

###########call linux command in python##########



#####文件中添加行
####https://stackoverflow.com/questions/10507230/insert-line-at-middle-of-file-with-python
def add_line_in_file(index,value):
    file_handler = open("file","r")
    content = file_handler.readlines()
    file_handler.close

    content.insert(index,"value\n")
    file_handler = open("file","w")
    content = "".join(content)
    file_handler.write(content)
    file_handler.close()


##refer to
##http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
# -*- coding: utf-8 -*-
import os

def read_a_file_line_by_line():
    file_hander = open('file','r+')
    for line in iter(file_hander):
        print line
    file_hander.close()





##########regex replace file for all line in a file
#########https://stackoverflow.com/questions/18935626/regex-re-sub-list-in-a-file
def replace_in_place_in_file():
        output = open("regex_replace_out_file","w")
        input = open("regex_replace_file","r")

        for line in input:
            output.write(re.sub("regex_pattern","will_be_replaced_string", line))
        input.close()
        output.close()
        os.remove("regex_replace_file")  ###不优雅
        os.rename("regex_replace_out_file","regex_replace_file")



####http://pythontesting.net/python/regex-search-replace-examples/
######regex replace file for all line in a file###
#######PERFECT###############
####and https://pymotw.com/2/fileinput/ common replace
####call by
######python regex_replace_in_file.py example.txt
import fileinput,re
def replace_in_place_in_file():

        for line in fileinput.input(inplace=1, backup='.bak'):
            line = re.sub('regex_pattern','will_be_replaced_string', line.rstrip())
            print(line)
###The fileinput module takes care of the stream verses filename input handling.
###The re (regex, regular expression) module has sub which handles the search/replace.
###The ‘rstrip’ is called on the input just to strip the line of it’s newline, since the next ‘print’ statement is going to add a newline by default.
###If you leave the ‘backup’ flag out, no backup will be made.
###As I’ve shown it with backup=’.bak’, an example.txt.bak file will be created.



###########detect port if open
###https://stackoverflow.com/questions/19196105/python-how-to-check-if-a-network-port-is-open-on-linux
# -*- coding: utf-8 -*-
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('ip_or_host',port_number))
if result == 0:
    print "Port is open"
else:
    print "Port is not open"




##############mysql operation
############http://www.runoob.com/python/python-mysql.html
--install modle
$> pip install MySQL-python
or
$> yum install MySQL-python



import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("server_ip_or_host","user","pwd","DB_name" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data




cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)


# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"


# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()


# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()




###call procedure
cat callmysqlproc.py |grep -v '#'
###https://pythonmana.com/2021/06/20210603215645724b.html
import MySQLdb
db = MySQLdb.connect("192.168.8.15","root","pwd","database")
cursor = db.cursor()
cursor.callproc('select_vm_info',args=('172.30.3.10',))
res1=cursor.fetchall()
print(res1)
data = cursor.fetchone()
print "Database version : %s " % data
cursor.close()
db.close()


#####get full path and name ###########
https://stackabuse.com/python-list-files-in-a-directory/

####--10 function
# -*- coding:utf-8 -*-
import os
import time
from ftplib import FTP

def printfile(mypath):
    shpfiles = []
    for dirpath, subdirs, files in os.walk(mypath):
        for x in files:
                shpfiles.append(os.path.join(dirpath, x))
    print shpfiles



####--15 another function
import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "*.py"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (entry)

####--20 call
printfile('/home/user')

#####get full path and name ###########


######End pythondemo.py #######
######Endmemoof pythondemo.py #######
