#!/usr/bin/env python
# coding=utf-8
content = "who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on aforg otten past you can’t go on well in lifeuntil you let go of your past failures and heartaches "
dict={}
a=content.split(' ')
for i in a:
	dict[i]=dict.get(i,0)+1    
print dict

for i,v in dict.items():
	print "{},{}".format(i,v)

dict2 = { }
for i,v in dict.items():
	print "{},{}".format(v,i)
	dict2[v]=i
print dict2








