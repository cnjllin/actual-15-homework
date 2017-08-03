#!/usr/bin/python
#coding:utf-8
#作业要求：读取access.txt（从群共享下载）日志文件，找出重复次数前10的IP地址，打印地址和重复次数
#defaultdict会在初始化时指定默认值.
from collections import defaultdict
fo = open('access.txt')
#读取IP
a = []
for i in fo.readlines():
	a.append(i.split(' ')[0])
#给default_dict传入int，则可以用来计数：
b = defaultdict(int)
for j in a:
	b[j] += 1
#字典排序
b=sorted(b.items(),key=lambda item:item[1],reverse=True)[0:10]
for x in b:
        #把元祖转换为列表
	y = (list(x))
	print "ip:%s，出现的次数：%s" % (y[0],y[1])
