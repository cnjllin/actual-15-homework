#!/usr/bin/python
# --*-- coding:UTF-8 --*--
my_list=list()
f = open('test.txt','r')
for line in open('test.txt','r'):
     line=f.readline()
     my_list.append(line.split(' ')[0])
f.close()
my_list1=list()
my_key=dict()
v1=str()
v=str()
my_list1=list(set(my_list))
for v in my_list1:
     n=0 
     for v1 in my_list:
         if v1 in my_list1 and v==v1:
             n+=1
             my_key[v]=n
print sorted(my_key.iteritems(),key = lambda asd:asd[1],reverse=True)[:10]
