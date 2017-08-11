#!/usr/bin/python
#coding:utf-8

#注册函数
def zhuce():
    with open('a.txt','a+') as f:
        date = f.read()
        user = raw_input('请输入一个名字:')
        if len(user.strip()) == 0:
            print "用户名不能为空"
            exit()
        if user in date:
            print "用户名已存在"
            exit()
        else:
            passwd = raw_input('输入一个密码:')
            if len(passwd.strip()) == 0:
                print "密码不能为空"
                exit()
            else:
               f.write("%s:%s\n" %(user,passwd))
    return "欢迎注册" 
    
#登录函数
def login():

    dict_1 = {}
    with open('a.txt') as f:
        for n in f:
            dict_1[n.split(":")[0]] = n.split(":")[1]
        name = raw_input('请输入你的用户名:')
        if len(name.strip()) == 0:
            print "用户名不能为空"
            exit()
        else:
            if name in dict_1:
                passwd = raw_input('请输入你的密码:')
                if dict_1[name].strip() == passwd:
                    print "welocme"
                else:
                    print "passwd error"
            else:
                print "no such the user of %s" %(name)
     
    return "欢迎登录"
    
#入口函数    
def start():
    a = raw_input('pls input you chose (zhuce|login):')
    if len(a.strip())==0:
        print "不能为空"
    if a == "zhuce":
        res = zhuce()
    elif a == "login":
        res = login()    
    else:
        print "只能选择zhuce|login"
    return res
p = start()
print p



