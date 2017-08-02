#!/usr/bin/env python
#coding:utf-8

'''
作业需求：
实现python基于nginx的访问日志统计客户端IP的访问量，并以排序的方式取出TOP10的IP和访问次数
'''

import time

start = time.clock()

# 定义一个空字典
nginxip = {}

# 打开一个文件以readlines方式进行读取所有行
with open('access.txt') as f:
    logs = f.readlines()

# 循环日志文件以空格为分隔符截取位置为0及IP这个元素
for line in logs:
    ip = line.split()[0]

    # 判断ip出现的次数分别以计数的方式写入字典里
    if ip in nginxip:
        nginxip[ip] += 1
    else:
        nginxip[ip] = 1

# 定义一个新列表，使用sorted进行降序排列，使用key排序，截取前十个IP
list = sorted(nginxip.iteritems(),key=lambda x:x[1],reverse=True)[:10]

# 遍历list列表，enumerate会将该数据对象组合为一个索引序列，同时列出数据和数据下标
for k,v in enumerate(list):
    print "访问IP和次数：%s --> %s" %(k,v)

end = time.clock()
print "统计运行时间: %f s" % (end - start)
