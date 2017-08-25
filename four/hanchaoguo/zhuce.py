#!/usr/bin/python
#coding:utf-8

#注册函数
list_1 = []
def zhuc(username,passwd,passwdagin):
        with open('exce.txt','a+') as f:
            if len(username.strip()) == 0 or len(passwd.strip()) == 0:
                return "username or passwd can not be emety"
            else:
                if passwd == passwdagin:
                    f.write('%s:%s\n'%(username,passwd))
                    return  "注册成功"
                else:
                    return "两次输入密码不一致"



