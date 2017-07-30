#!/usr/bin/python 
# -*- coding: utf-8 -* 
a = 50
c = 0
time = 3
while c <= 3:
    time -=1  
    b = int(raw_input("pleases input your number: "))
    if b == a:
       print '您猜对了'
       break
    elif b > a:
       print '您猜数值大了,你还剩余{}次机会'. format(time)   
       c +=1
    elif b < a:
       print '您猜数值小了,你还剩余{}次机会'. format(time)
       c +=1
       break
