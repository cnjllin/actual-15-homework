#!/usr/bin/python
#coding:utf-8
ip_list = []
ips_list = {}

#读文件，并生切割成IP列表
with open('/server/scripts/python/access.txt','rb') as f:
     for item in f:
         ip_list.append(item.strip('\n').split(' - - ')[0])

     #去重并统计所有ip出现的次数，最终生成一个key为IP,value为次数的字典
     for m in set(ip_list):
         b = 0
         for o in ip_list:
             if o == m:
                 b +=1
             ips_list[m] =b

     #排序，并取出前十
     p = sorted(ips_list.items(),key=lambda d:d[1])
     for n in range(10): 
         print "第%s名为%s,出现了%s次" %((n+1),p[(-n-1)][0],p[-n-1][1])
