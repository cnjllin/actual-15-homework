#!/usr/bin/python
# --*-- coding:UTF-8 --*--

#生成ip为元素的列表。
my_list=list()
f=open('/home/niushaoshuai/access.txt','r')
for line in f.readlines():
    my_list.append(line.split(' ')[0])
f.close()

#生成{ip:times}为元素的字典。
my_key=dict()
for ip in my_list:
    if ip in my_key:
        my_key[ip]+=1
    else:
        my_key[ip]=1
    

#对字典进行排序，取出前十。
for i in  sorted(my_key.iteritems(),key = lambda asd:asd[1],reverse=True)[:10]:
    print "%s request %d times" % i

