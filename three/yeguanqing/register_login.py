#!/usr/bin/env python
#coding:utf-8

'''
通过函数实现用户注册、登陆python脚本
'''

# 定义一个登陆函数，在这里并不需要参数
def login():

    # 使用input获得用户输入的字符串判断是否存在test文件中
    username = raw_input("please input your name:").strip()
    # 定义一个文件并赋予可读的权限
    login_file = open('/Users/guanqing/PycharmProjects/reboot15/day3/test','r')
    # for循环这个文件并通过':'的格式将用户名和密码传参到usernum和passwordnum
    for line in login_file.readlines():
        usernum,passwordnum = line.strip().split(':')
        # 判断用户以及密码是否正确，用户名和密码错误的时候有相应的提示
        if username == usernum:
            pass01 = raw_input("please input your password:").strip()
            if pass01 == passwordnum:
                return "welcome to login."
            else:
                return "your password is wrong."
        else:
            return "your username is wrong."
    login_file.close()

# 定义一个注册函数
def register():
    # 定义一个文件并赋予权限读写权限
    register_file = open('/Users/guanqing/PycharmProjects/reboot15/day3/test', 'a+')
    username = raw_input("please input your name:").strip()
    # 判断用户输入是否为空
    if len(username) == 0:
        return "your username can't empty."
    else:
        # 判断用户输入的密码是否正确以及是否为空
        password = raw_input("please input your password:").strip()
        repassword = raw_input("please input your password again:").strip()
        if password != repassword or len(password) == 0:
            return "the password is wrong. "
        else:
            # 将用户输入的账号信息写入到test文件里
            register_file.write("%s:%s\n" %(username,password))
            register_file.close()
            return "congratulations, your register is success."

# 通过input的方式判断并调用函数
def start():
    action = raw_input("please select:register/login:").strip()
    if action == "login":
        res = login()
    elif action == "register":
        res = register()
    else:
        return "your input is wrong."

    return res

print start()
