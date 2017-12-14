#!/usr/bin/env python
#coding:utf8


import os
for i in range(65,91):
   # print i
    volume = chr(i)+':/'       #chr()函数将数字的accii码转换为字符
   # print volume
    if os.path.isdir(volume):
        print volume
       
        
