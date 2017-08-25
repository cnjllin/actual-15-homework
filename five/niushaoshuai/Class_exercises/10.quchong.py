#!/usr/bin/python
# --*-- coding:UTF-8 --*--
a=[1,1,2,3,4,5,7,6,7]
b=[]
for num in a:
    if num not in b:
        b.append(num)
b.sort()
print b
