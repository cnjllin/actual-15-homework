#!/usr/bin/python
#coding:utf-8
ips_list = {}

#读文件
with open("/server/scripts/python/access.txt",'r') as f:
     
     #遍历文件，生成key为ip,value为次数的字典
     for n in f.read().split("\n"):
         ips_list[n.split(" - - ")[0]]=ips_list.get(n.split(" - - ")[0],0)+1    
    
     #排序，并取出前十
     p = sorted(ips_list.items(),key=lambda d:d[1])
     for n in range(10): 
         print "第%s名为%s,出现了%s次" %((n+1),p[(-n-1)][0],p[-n-1][1])
