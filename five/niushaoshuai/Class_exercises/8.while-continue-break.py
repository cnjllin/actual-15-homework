#/usr/bin/python
# --*-- coding:UTF-8 --*--
n=0
while n<10:
    n+=1
    if n==3:                #放到最后会死循环
        continue
    elif n==8:
        break
    print n
