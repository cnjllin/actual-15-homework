#!/bin/usr/env python
#coding:utf-8

'''
判断用户名密码是否正确，正确则打印欢迎信息，错误输出具体的错误原因信息
用户可以连续输入三次密码，超过三次则锁定用户
用户输入的密码位数必须超过6位
'''

import sys

count = 0
time = 0

while count < 3:
    loginuser = raw_input("please input your name: ").strip()
    user1_file = open('/Users/guanqing/PycharmProjects/reboot15/day1/user_lock','r+')      #打开一个本地文件，用于读写

    for line1 in user1_file.readlines():       #循环读取文件里的每行信息
        line1 = line1.strip()
        if loginuser == line1:
            sys.exit("The user %s has been locked!" % loginuser)     #如果用户存在于锁定文件中，将退出主程序

    user2_file = open('/Users/guanqing/PycharmProjects/reboot15/day1/user','r')     #打开一个本地文件user，用于只读

    for line2 in user2_file.readlines():
        loginuser01,loginpw01 = line2.strip().split(':')     #以':'将每行的字符分开，传参数等于变量loginuser01和loginpw01

        if loginuser == loginuser01:
            count1 = 0
            while count1 < 3:        #此时验证用户正确后进行密码的三次判断循环
                time = 2 - count1
                count1 += 1

                loginpw = raw_input("please input your password: ").strip()
                if len(loginpw) < 6:       #判断密码的长度是否小于6位，如果是的话将给三次机会重新输入，之后将退出整个程序
                    print "Your password length must be more than 6, you have %s times left!" % time
                else:
                    if loginpw == loginpw01:
                        sys.exit("Welcome to login %s!"% loginuser)
                    else:
                        if count1 != 2:
                            print "Your password is wrong, you have %s times left!" % time

            else:
                user1_file.write(loginuser + '\n')      #用户密码进行while循环三次验证后，将用户写入user_lock文件中
                sys.exit("The user %s is locked!" % loginuser)

    else:
        sys.exit("Your account does't exist, please register, thanks. ")  #如果输入的用户不在文件库中，将提示并退出整个程序


user1_file.close()     #上面open是一个系统的调用函数打开或创建一个文件，而此时的close是关闭一个打开的文件
user2_file.close()







