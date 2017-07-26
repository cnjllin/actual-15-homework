#!/usr/bin/python
#coding:utf-8

import string
import random

#用户名和密码信息
users={'gaofan':'1234567'}
#用户密码错误时输入最大次数和验证码错误时输入最大次数的计数器
times_pass=1
times_idcode=1
#开始输入账号和密码
account=raw_input('请输入您的账号:\n\033[0;31;40m******************\033[0m\n')
print "\033[0;31;40m*\033[0m" *18
while times_pass <=3 and times_idcode<=6:
#   输入密码
    passwd=raw_input('请输入密码:\n\033[0;31;40m******************\033[0m\n')
    print "\033[0;31;40m*\033[0m" *18
#   生成并输入验证码
    identifying_code="".join(random.sample(string.letters+'0123456789',4))
    print "本次验证码为:'%s'" % identifying_code
    i_code=raw_input('请输入验证码:\n\033[0;31;40m******************\033[0m\n') 
    print "\033[0;31;40m*\033[0m" *18
#   如果验证码正确
    if i_code == identifying_code:
#   如果账号不正确
        if not  users.get(account):
#   跳出循环，提示账号不存在
            print "\033[0;31;40m该账号不存在!\033[0m"
            break
#   如果账号正确
        else:
#   密码少于6位
            if len(passwd) < 6:
                print "\033[0;31;40m密码位数不足6位!\033[0m"
                continue
            else:
#   密码正确，提示登录成功,跳出循环
                if passwd == users[account]:
    		    print "\033[0;32;40m登录成功,欢迎！\033[0m"
		    break
#   密码不正确，提示并给出剩余登录机会
		else:
                    print "\033[0;31;40m密码错误！\n您还有%s次输入机会!\033[0m" % (3-times_pass)
                    times_pass=times_pass+1
		    continue
#   验证码如果不正确，结束当次循环，继续下次循环
    else:
        print "\033[0;31;40m验证码不正确!\033[0m"
        times_idcode=times_idcode+1        
else:
#   三次登录过后，退出循环，提示账户被锁住
    if times_pass == 4:     
        print "\033[0;31;40m连续登录失败次数达到三次，禁止登录!\033[0m"
#   验证码输错次数达到六次，提示15分钟后登录
    elif times_idcode == 7:
        print "\033[0;31;40m验证码输入错误次数过多，15分钟之后再登录!\033[0m"
