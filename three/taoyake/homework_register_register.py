# -*- coding: utf-8 -*-
def register():
    username = raw_input("请输入用户名:")
    if username == '':
        return "您输入的用户为空"
    else:
        password = raw_input("请输入您的密码: ")
        if password == '':
            return "您输入的密码为空"
        else:
            password_two = raw_input("请您再次输入的密码: ")
            if password == password_two:
                File = open('user.txt','a+')
                File.write('%s:%s\n' % (username,password))
                File.close()
                return "恭喜你,注册成功"
            else:
                return "密码不匹配"

def Signin():
    #通过user变量，获取到输入的用户名
    user = raw_input("请输入您的用户名: ")
    with open('user.txt','r') as file:
        for line in file.readlines():
            username = line.strip().split(":")[0]
            password = line.strip().split(":")[1]
    if user != username:  #如果输入的用户不等于预先定义的用户名,则打印用户不存在并且退出循环
        return "对不起，你输入的%s用户不存在" % user
    else:
        pwd = raw_input("请输入您的密码: ")  #输入密码
        if pwd != password:  #如果密码连续输错三次，提示账号锁定并退出
            return "您的密码不正确"
        else: #如果上边的都不成立，说明输入密码正确，提示登录成功
            return "恭喜您%s成功登录" % user

def start():
    action = raw_input("请输入 Signin or register :").strip()
    if action == "Signin":
        return Signin()
    elif action == "register":
        return register()
    else:
        return "什么都没有输入,或者输入与提示不符合,退出程序"
result = start()
print  result
