#!/usr/bin/python
#coding:utf-8
import time
a=time.time()
list_1 = []
dict_1 = {}
dict_2 = {}
with open('aaa.txt') as f:
   
   #生成key是名字,value是分数的字典dict_1 
   for n in f:
       dict_1.setdefault(n.split(" ")[0],[])
       dict_1[n.split(" ")[0]].append( int(n.split(" ")[1].strip()))
  
   #生成名字的列表
   list_1 = dict_1.keys()
   for n in list_1:
       dict_2[n]=(sum(dict_1[n])/len(dict_1[n]))
       p = sorted(dict_2.items(),key=lambda d:d[1])
   #打印最终信息
   for n in range(len(p)):
       print "第%s名是%s,%s科的平均成绩%s" %((n+1),p[(-n-1)][0],len(dict_1[p[(-n-1)][0]]),p[(-n-1)][1])
b=time.time()
print "%s"  %(b-a)
