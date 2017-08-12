#!/usr/bin/python
#coding:utf-8 

'''
将注册和登录接口定义成函数，并模拟前台登录写一段代码，加载注册和登录函数
思路：
1）分别写出登陆和注册函数
2）写出入口函数，分别调用登陆和注册函数
'''
# 定义登陆函数
def login():
    fo = open('user.txt')
    users = {}
    content = fo.readlines()
    fo.close()
    for user in content:
        name = user.rstrip("\n").split(":")[0]
        users[name] = user.rstrip("\n").split(":")[1]
    name = raw_input("请输入用户名: ").strip()
    if name not in users:
        return  "用户名不存在，请联系管理员"
    else:
        password = raw_input("请输入密码").strip()
        if password != users[name]:
            return "密码错误"
        else:
            return "恭喜你，登陆成功"
    return "欢迎登陆"

# 定义注册函数 
def reg():
    f = open('user.txt','a+')
    name = raw_input("请输入用户名：").strip()
    if len(name)==0:
        return "用户名为空，请重新输入"
    else:
        password = raw_input("请输入密码：").strip()
        if len(password) <6:
            return "密码太短，请重新输入："
        else:
            repass = raw_input("请再次输入密码：").strip()
        if len(password)==0 or password != repass:
            return "密码输入有误"
        else:
            f.write("%s:%s\n" %(name,password))
            f.close()
            return "恭喜你注册成功"

# 定义入口函数
def start():
    action = raw_input("请输入reg/login ").strip()
    if action == "login":
        res = login()
    else:
        res = reg()
    return res

# 调用函数
result = start()
print result
