#!/usr/bin/python
# --*-- coding:UTF-8 --*--
def yunsuan(x,str,y):
    if str == '+':
        return x + y
    elif str == '-':
        return x - y
    elif str == '*':
        return x * y
    elif str == '/':
        return x / y
    else:
        return "feifa"

print yunsuan(1,'+',1)
