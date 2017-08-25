#!/usr/bin/python
# --*-- coding:UTF-8 --*--
md={'age': 12, 'job': 'IT', 'name': 'pc', 'teach': 'pc', 'waihao': 'pc'}
nd=dict()
od=dict()

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


