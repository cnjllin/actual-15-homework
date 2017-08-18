#!/usr/bin/python
# --*-- coding:UTF-8 --*--
b="100"
def a(x):
    global c
#    global x
    c = x
    return c
#return后的语句不会被执行。
    return b

def d(x):
    c = x
    b='1'
    return c

print a('10')
print d('20')
print b
