#!/usr/bin/python
# -*- coding:utf-8 -*-

count = 1
num = 10
total =3

while count <=3:
    total=total-1
    count+=1
    input_num = int(raw_input("please input num:"))
    if input_num == num:
        print "输入正确"
        break
    elif input_num > num:
        print "输入的数字太大,你还有%d次机会" % total
    else:
        print "输入的数字太小,你还有%d次机会" % total
else:
    print "输入错误超过三次，退出"
