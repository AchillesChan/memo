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
        
    return res      # 注释还可以像这样直接跟在一句代码的后面

if __name__ == '__main__':
    main()


#####文件中添加行
####https://stackoverflow.com/questions/10507230/insert-line-at-middle-of-file-with-python
def add_line_in_file(index,value):
    file_handler = open("your_file","r")
    content = file_handler.readlines()
    file_handler.close

    content.insert(index,"value\n")
    file_handler = open("your_file","w")
    content = "".join(content)
    file_handler.write(content)
    file_handler.close()


##refer to
##http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
# -*- coding: utf-8 -*-
import os

def read_a_file_line_by_line():
    file_hander = open('your_file_here','r+')
    for line in iter(file_hander):
        print line
    file_hander.close()




###ONLY REPLACE FIRST LINE???
######https://jerel.co/blog/2011/12/using-python-for-super-fast-regex-search-and-replace
def replace_in_place_in_file_handler():
    file_handler=open("your_file","r") ##read session
    txt=file_handler.read()
    file_handler.close()

    file_handler = open("your_file","w") ###write session
    file_handler.write(re.sub("^[a]","K",txt))                                
    file_handler.close()



##########regex replace file for all line in a file
#########https://stackoverflow.com/questions/18935626/regex-re-sub-list-in-a-file
def replace_in_place_in_file():
        output = open("out-your_need_regex_replace_file","w")
        input = open("your_need_regex_replace_file","r")

        for line in input:
            output.write(re.sub("regex_pattern","replaced_string", line))                                       
        input.close()
        output.close()
        os.remove("your_need_regex_replace_file")  ###权宜之计，不优雅
        os.rename("out-your_need_regex_replace_file","your_need_regex_replace_file")
