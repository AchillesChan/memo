http://ginstrom.com/scribbles/2009/09/14/easy-sftp-uploading-with-paramiko/ Easy SFTP uploading with paramiko

https://paramiko-docs.readthedocs.io/en/1.15/api/sftp.html 
https://www.liaoxuefeng.com/ python教学


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
