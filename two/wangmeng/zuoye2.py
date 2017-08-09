#!/usr/bin/python
# encoding: utf-8
''' 
    作业要求：
    将access.txt里面的访问IP取出来，
    并且打印出现次数最多的前十位。
'''
# 读取access
with open('access.txt','a+') as f:
    out = f.read()
    over = 0
    while not over:
        if out != '':
            print out.split('\n')[1].split(',')[0].split()[0]
            out =f.next()
        else:
            over = 1
    f.close()
