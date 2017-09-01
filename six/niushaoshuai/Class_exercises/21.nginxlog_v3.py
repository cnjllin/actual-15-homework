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


nd=dict()
od=dict()
'''
for k,v in my_key.items():
    if v in nd:
        nd[v]+=1
    else:
        nd[v]=1
for k in nd:
    if nd[k]>1 :
        od.setdefault(k,[])
for k,v in my_key.items():
    if v in od:
        od[v].append(k)
    else:
        od[v]=k
'''
          
for k,v in my_key.items():
    od.setdefault(v,[])
    od[v].append(k)

#对字典进行排序，取出前十。
for t in range(10):
    m_key=max(od.keys())
    print "{} {}".format(m_key,od[m_key])
    od.pop(m_key)
