#!/usr/bin/python
# -*- coding:utf-8 -*-
# description:Analyse a nginx access log for the top 10 ip addresses

import time
import re
start = time.time()

f = open('access.txt','a+')
l = f.readlines()
f.close
l_ip = []

# 1.remove blank and duplicate rows
# 2.l_ip list stores all the access ip
for i in l:
    blank_row=re.findall(r'^ *$',i)
    if blank_row:
        continue
    else:
        l_ip.append(i.split(' ')[0])
# create a dictionary named dict to store the key:ip and the value:access times.
dict = {}
# traverse the list l_ip to statistics the access times of every ip.
for i in l_ip:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
# sort by the access time of ip
sort_dict = sorted(dict.items(), key=lambda l:l[1],reverse=True)[:10]
# print top 10 access ip by access times
for item in sort_dict:
    print("IP:%-15s  Access Times: %s"%(item[0],item[1]))
end = time.time()
interval = end -start
print "Execute time::%0.3fs" % interval

