#!/bin/env python
# -*- encoding:utf-8 -*-
# 耗时 0m3.074s

file_path = '449944000PKK2017080132316600.i'
with open(file_path,"r") as f :
    lines = f.readlines()

#生成元素为列表的列表
#ips_tmp = []
#ips_tmp = [ line.split() for line in lines ]

#生成值键为IP,值为列表的字典
#ips = {}
#ips = { ip[0]:[ ip[3],ip[6],ip[8] ]  for ip in ips_tmp }

ips_tmp = []
ips_tmp = [ line.split()[0] for line in lines ]
print "1. ips_tmp type is " + str(type(ips_tmp))

ips = {}
ips = { ip:ips_tmp.count(ip) for ip in set(ips_tmp) }  ##主要耗时在这里
print "2. ips type is " + str(type(ips))
ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)
print "3. ips type is " + str(type(ips))

num = 0
for ip in ips :
    print "IP: %-20s 访问次数: %-10d" % ( ip[0] , ip[1] )
    num += 1
    if num > 10 :
        break
