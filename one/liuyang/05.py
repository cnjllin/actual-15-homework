#coding=utf-8
a = [1,23,34,23,23,67,434,34]
max_num = 0
for i in a:
	if max_num < i:
		max_num = i
print 'the max num is %s'%max_num
