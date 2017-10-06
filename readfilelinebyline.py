##refer to
##http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
# -*- coding: utf-8 -*-
import os

def main():
    file_hander = open('ip.txt','r+')
    for line in iter(file_hander):
        print line
    file_hander.close()
if __name__ == '__main__':
    main()
