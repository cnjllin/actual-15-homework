#!/usr/bin/python
# -*- coding:utf-8 -*-
# description:Analyse a nginx access log for the top 10 ip addresses

import time
import re
start = time.time()

# create a dictionary named dict to store the key:ip and the value:access times.
dict = {}

# opening a file with the mode 'rU' will open a file for reading in universal newline mode
# traverse the log file to ouput index and content
for index,line in enumerate(open('./access.txt','rU')):
    ip = line.split(' ')[0]
    if ip in dict:
        dict[ip]+=1
    else:
        dict[ip]=1

# sort by the access time of ip
sort_dict = sorted(dict.items(), key=lambda l:l[1],reverse=True)[:10]
# print top 10 access ip by access times
for item in sort_dict:
    print("IP:%-15s  Access Times: %s"%(item[0],item[1]))
end = time.time()
interval = end -start
print "Execute time::%0.3fs" % interval

