#!/usr/bin/python
def f(x):
    return x % 2 != 0
l=range(10)
print filter(f,l)
