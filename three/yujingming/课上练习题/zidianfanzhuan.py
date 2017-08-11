#!/usr/bin/env python
# coding=utf-8

content="who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forg    otten past you can’t go on well in lifeuntil you let go of your past failures and heartaches"
dict={}
a=content.split(' ')
for k in a:
	dict[k]=dict.get(k,0)+1    
#print dict


dict2 = { }
for k,v in dict.items():

	dict2.setdefault(v,[]) 
	dict2[v].append(k)
	print dict2

for k,v in dict2.items():
	if k >1:
		print "{}times,value is {}".format(k,v)


