#/usr/bin/env python

#coding:utf-8

import time

start = time.time()
op = "/root/access.txt"
with open(op, "r") as f:

    iplist = [x.split(" ")[0] for x in f ] #  取IP
    a = ( (i,iplist.count(i)) for i in {x for x in iplist} ) #去重并统计重复数量

    c = sorted(a, key=lambda x:x[1], reverse=True)[:10] #排序取前10个
    for i in c:
        print "%s,%10s" % (i[0],i[1])


print 
print "time:"
print time.time() - start
