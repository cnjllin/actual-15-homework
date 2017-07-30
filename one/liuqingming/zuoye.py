#!/bin/env python
# -*- coding:UTF-8 -*-
#

import string
import random
import json

#注册用户
def register():
    data = {}
    with open('user.json', 'r') as f:
        data = json.load(f)
        #print type (data)
        #data = json.loads(data)
        #print type (data)
    
    num = 0
    while num < 3 :
        num = num + 1
        user_name = raw_input("请输入用户名：")
        user_passwd1 = raw_input("请输入密码：")
        user_passwd2 = raw_input("请再次输入密码：")
        len_passwd = len(user_passwd1)
        code = "".join(random.sample(string.letters+string.digits,4))
        print "验证码:%s" % code
        lower_code = string.lower(code)
        user_code = string.lower(raw_input("请输入验证码，不区分大小写:"))
        if user_name not in data :
            if len_passwd < 6 :
                print "密码少于6位，请重新输入"
                continue
            else :
                if user_passwd1 == user_passwd2 and lower_code == user_code :     
                    data[user_name] = user_passwd1
                    #j_str = json.dumps(data)
                    with open('user.json', 'w') as f:
                        json.dump(data,f)
                    print "恭喜您注册成功，您的用户名为%s" % user_name
                    break
                elif user_passwd1 == user_passwd2 and lower_code != user_code :
                    print "验证码错误"
                    continue
                elif user_passwd1 != user_passwd2 and lower_code == user_code :
                    print "两次密码不一致"
                    continue
                else :
                    print "两次密码不一致且验证码错误"
                    continue
        else :
            print "用户名%s已经存在,请输入其他用户名" % user_name
            continue
    else :
        print "输入错误达到3次，您已被锁定"



#登陆用户
data = {}
with open('user.json', 'r') as f:
    data = json.load(f)
    #data = json.loads(data)

num = 0
while num < 3 :
    num = num + 1
    user_name = raw_input("请输入用户名：")
    if user_name in data :
        user_passwd = raw_input("请输入密码：")
        len_passwd = len(user_passwd)
        if len_passwd < 6 :
            print "密码少于6位，请重新输入"
            continue
        else :
            code = "".join(random.sample(string.letters+string.digits,4))
            print "验证码:%s" % code
            lower_code = string.lower(code)
            user_code = string.lower(raw_input("请输入验证码，不区分大小写:"))
            if data[user_name] == user_passwd and lower_code == user_code :
                print "登陆成功，欢迎%s" % user_name
                break
            elif data[user_name] == user_passwd and lower_code != user_code :
                print "登陆失败，验证码错误"
                continue
            elif data[user_name] != user_passwd and lower_code == user_code :
                print "登陆失败，密码错误"
                continue
            else :
                print "登陆失败，密码和验证码错误"
                continue
    else :
        print "用户名%s不存在,请重新输入" % user_name
        stat = raw_input("重新输入用户名请输入y,注册新用户请输入其他，再按回车键：")
        stat = string.lower(stat)
        if stat == 'y' :
            continue
        else :
            register()
            break
else :
    print "输入错误达到3次，您已被锁定"
