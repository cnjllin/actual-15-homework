#!/usr/bin/python
#coding:utf-8
import sys
numb = 50
count = 1
time = 3
while count <= 3:
    time -=1
    eg = raw_input("plrase input numb: ")
    try:
        eg = int(eg)
    except Exception,e:
        print e.message
        sys.exit()
    if eg == numb:
        print "恭喜，你猜对了 就是 {}".format(eg)
        break
    elif eg < numb:
        print "数字小了你还有{} 次机会".format(time)
        count +=1
    else:
        print "数字小了你还有{} 次机会".format(time)
        count +=1
else:
    print "账号锁定 "
