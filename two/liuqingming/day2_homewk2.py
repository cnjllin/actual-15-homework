#!/bin/env python
# -*- encoding:utf-8 -*-
# 耗时 0m0.178s

file_path = '/root/access.txt'
ips = {}
with open(file_path,"r") as f :
    for line in f :
        ip = line.split()[0]
        ips[ip] = ips.get(ip,0) + 1
ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)

print "============= IP TOP10 信息 ============="
num = 0
for ip in ips :
    print "IP: %-20s 访问次数: %8s" % ( ip[0] , str(ip[1])+"次" )
    num += 1
    if num > 10 :
        break
