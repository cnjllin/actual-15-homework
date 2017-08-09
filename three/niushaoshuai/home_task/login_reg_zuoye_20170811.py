#!/usr/bin/python
# --*-- coding:UTF-8 --*--
def my_login():
    f=open('user_message.db','r')
    user_name = raw_input("please input your name: ")
    md=dict()
    for line in f.readlines():
        mu = line.split(':')[0]
        mp = line.split(':')[1].strip('\n')
        md[mu]=mp
    if user_name in md.keys():
        user_pass = raw_input("please input your password: ")
        if user_pass==md[user_name]:
            print "login ok ,welcom {}".format(user_name)
        else:
            print "input a error password!"
    else:
        print "user is not exist!"
    #    exit(1)
    f.close()
def my_reg():
    f = open('user_message.db', 'a+')
    while True:
        user_name = raw_input("please input your name: ")
        if len(user_name) == 0:
            print "user is prohibit to null,please reinput the message"
            continue
        else:
            user_pass1 = raw_input("please input your password: ")
            user_pass2 = raw_input("please reinput your password: ")
            if len(user_pass1)==0 or user_pass1!=user_pass2:
                print "password is not ok"
                continue
            else:
                f.write('%s:%s'%(user_name,user_pass1))
                f.close()
                print "Congratulations,registe ok"
                break

my_input=str()
def start():
    my_input=raw_input("please input the type : login or reg ")
    if my_input=="reg":
        my_reg()
    elif my_input=="login":
        my_login()
    else:
        print "input fatal"

start()
