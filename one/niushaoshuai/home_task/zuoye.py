#!/usr/bin/python
#-!-  coding: UTF-8
user_name=raw_input("please input your username: ")
real_name="niushaoshuai"
real_pass="12345678"
count=0
times=1
if user_name==real_name :
    while times<=3:
        user_pass=raw_input("please input your password: ")
        count=count+1
        times=times+1
        if user_pass==real_pass:
            print "welcom {}".format(real_name)
            break
        else:
            print "input a error password,you have {} times".format(3-count)
    else:
        print "你的机会用完了,用户已被锁定 " 
else:
    print "user {} is not exist".format(user_name)
