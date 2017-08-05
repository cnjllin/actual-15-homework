#!/usr/bin/python
## -*- coding: utf-8 -*-
import os

Log_Dict = {}


File = open('access.log','r')           #只读方式打开文件
with open('/Users/playcrab/python/test/day2/access.log','r') as file:
    for line in file.readlines():       #循环读取每一行日志
        ip = line.strip().split()[0]    #通过列表的split切片获取到ip
        if ip in Log_Dict:              #判断ip是否存在定义的空字典中
            Log_Dict[ip]+=1             #如果获取到的ip存在字典中，则加1
        else:
            Log_Dict[ip]=1              #如果不存在，则把ip次数设置1

Log_List = Log_Dict.items()             #字典转化成列表
length = len(Log_List)

#使用冒泡排序进行排序
for j in range(1,11):
    for k in range(0,length-1):
        if Log_List[k][1] > Log_List[k+1][1]:
            Log_List[k],Log_List[k+1] = Log_List[k+1],Log_List[k]
    print "IP:%s  出现了%s次" % (Log_List[-j][0],Log_List[-j][1])
