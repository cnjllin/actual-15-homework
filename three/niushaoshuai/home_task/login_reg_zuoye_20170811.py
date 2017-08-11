#!/usr/bin/python
# --*-- coding:UTF-8 --*--
def my_login():
    f=open('user_message.db','r')
    md=f.readlines()
    user_name = raw_input("please input your name: ")
    for line in md:
        mu=line.split(':')[0]
        mp=line.split(':')[1].strip('\n')
        print mu,mp
        if mu==user_name:
            user_pass = raw_input("please input your password: ")
            if mp==user_pass:
                print "login ok ,welcom {}".format(user_name)
                break
            else:
                print "input a error password!"
                pass
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
            pass
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
