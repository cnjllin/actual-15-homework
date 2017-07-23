#!/usr/bin/python
# -*- coding:utf-8 -*-

a = [1,23,34,23,23,67,434,34]
print max(a)
max = 1

for i in a:
    if i > max:
        max = i
print max
