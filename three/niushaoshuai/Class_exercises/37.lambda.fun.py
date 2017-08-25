#!/usr/bin/python
'''
f=lambda x :x**2
print f(3)
'''
'''
f=lambda x: x+2
l=range(10)
print map(f,l)
'''
f=lambda x,y : x+y
l=range(10)
print reduce(f,l)
