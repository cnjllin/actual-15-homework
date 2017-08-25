#!/usr/bin/python
#-*- coding: UTF-8
count=0
time=1
jieguo=50
while time <= 3:
    try:
        n=int(raw_input("please input a num: "))
    except Exception,e:
        print "输入非法"
        exit(1)
    count=count+1
    time = time + 1
    if n < jieguo:
        print "{} is smaller than  jieguo,you have {} times least".format(n,3-count)
    elif n > jieguo:
        print "{} is bigger jieguo,you have {} times least".format(n,3-count)
    else:
        print "你猜对了"
        break
else:
    print "你的机会用完了,用户已被锁定 "
