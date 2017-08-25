#!/usr/bin/python
'''
def f(x,y):
    return x+y
print reduce(f,range(10))
'''
def f(x,y):
    return x+y
print reduce(f,range(10),100)
