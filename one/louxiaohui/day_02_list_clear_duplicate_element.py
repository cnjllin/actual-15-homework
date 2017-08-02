#!/usr/bin/python
# -*- coding:utf-8 -*-

a=[1,1,2,3,4,5,7,6,7]

b = []

for i in a:
    if i in b:
        continue
    else:
	b.append(i)
print b

'''
for i in a:
    if not i in b:
        b.append(i)
print b
'''
