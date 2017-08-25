#!/usr/bin/python
# -*- coding:UTF-8 -*- 
m=float()
times=0
while 2>1 :
    n=raw_input('please input num: ')
    if n=='':
        break
    m+=float(n)
    times+=1
    avg01=m/times
print 'Average num is {}'.format(avg01)
