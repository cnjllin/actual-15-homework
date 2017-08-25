#!/usr/bin/python
# --*-- coding:UTF-8 --*--
str="who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forg    otten past you can’t go on well in lifeuntil you let go of your past failures and heartaches"
my_list=str.split(' ')
md=dict()
for v in my_list:
    if v in md:
        md[v]+=1
    else:
        md[v]=1

nd=dict()
od=dict()
'''
for k,v in md.items():
    if v in nd:
        nd[v]+=1
    else:
        nd[v]=1
for k in nd:
    if nd[k]>1 :
        od.setdefault(k,[])
for k,v in md.items():
    if v in od:
        od[v].append(k)
    else:
        od[v]=k
print od
'''
for k,v in md.items():
    od.setdefault(v,[])
    od[v].append(k)

'''
for k in od:
    if k >=3:
        print od[k]
'''
print sorted(od.items(),key=lambda k:k[0],reverse=True)[:3]
