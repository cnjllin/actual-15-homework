#!/usr/bin/env python

def d(**he):
	return he
x = {'name':1,'agee':2}
res = d(**x)
print res

def b(*arg):
	return tuple(list(arg))
x = ([20,30],5,6)
res = b(*x)
print res


