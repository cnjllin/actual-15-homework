#!/usr/bin/python
#coding:utf-8
import sys
number = 50
count = 0
time = 0
while count <3:
#while True:
        num = raw_input("pleae input num:")
        try:
            num = int(num)
        except Exception, e:
            print "输入非法"
            sys.exit()

        if num != number:
                count += 1
                time = 3-count
                  
                #if count >=3:
                #    pint "你输入超过三次，账户锁定"    
                #    break
                if num > number:
                    print "no~~no~~no，数字太大了，你还有 %s 次机会" % time
                else:
                    print "no~~no~~no，数字太小了，你还有 %s 次机会" % time

        else:           
             print "yes，猜对了"
             break
             #sys.exit(1)
print "game over"
