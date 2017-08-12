#!/usr/bin/python
#coding:utf-8
# 当使用raw_input输入错误的时候，回车前可以清除
import readline

#定义登录的函数，需要传入name和passwd的参数
def login(name,passwd):
    f = open('user.txt')
    #name = raw_input("请输入登录用户名：").strip()
    l = []
    k = {}
    for i in f.readlines():
        i =i.strip('\n')
        #将用户信息条，按照:来切片，获取用户名
        a = i.split(':')[0]
        b = i.split(':')[1]
        #将文件中每行按照{用户名:密码}的格式存入新字典中
        k[a] = b
        #将用户名追加到列表中，形成用户名的集合
        l.append(a)
    #判断用户输入的是否在列表里
    if name not in l:
        print "用户名不存在"
        exit()
    #如果用户名正确，判断输入的密码是否正确
    else:
        if passwd == k.get(name):
            print "欢迎%s登录" %name
        else:
            print "登录密码错误"
    f.close()

#定义注册的函数，需要传入name，passwd，passwd_re的三个参数
def reg(name,passwd,passd_re):
    f = open('user.txt','a+')
    #name = raw_input("请输入注册用户名：").strip()
    #判断注册用户名是否为空
    if len(name) == 0:
       print "用户名不能为空"
       exit()
    #定义一个空列表，将用户文件的用户名追加到一列表中，用新注册用户是否在列表中来判断注册用户名是否已存在，确保用户名的唯一性
    l = []
    for i in f.readlines():
        #将用户信息条，按照:来切片，获取用户名
        a = i.split(':')[0]
        #将用户名追加到列表中
        l.append(a)
    #判断新注册用户名是否已经存在
    if name in l:
        print "该账户已被注册"
        exit()
    #判断注册密码，是否为空，输入密码和确认密码是否匹配
    #passwd = raw_input("请输入注册密码：").strip()
    #passd_re = raw_input("重新输入注册密码：").strip()
    #判断注册密码是否为空
    if len(passwd) == 0:
        print "密码不能为空"
    #判断两次输入密码是否匹配，如果匹配则提示注册成功
    if passd_re == passwd:
        print "注册成功，您的账号为:%s,密码为:%s,请妥善保管" %(name,passwd)
        f.write('%s:%s\n' %(name,passwd))
        exit()
    #如果两次输入密码不匹配，提示密码不匹配
    else:
            print "密码不匹配"
    f.close()

#通过用户输入，选择不同的目的调用不同的接口
x = int(raw_input("请选择：1-登录，2-注册 ").strip())
#如果x=1，调用登录接口，并向接口传入name和passwd的参数
if x == 1:
    name = raw_input("请输入登录用户名：").strip()
    passwd = raw_input("请输入登录密码：").strip()
    login(name,passwd)
#如果x=2,调用注册接口，并向接口传入name,passwd,passwd_re三个参数
if x == 2:
    name = raw_input("请输入注册用户名：").strip()
    passwd = raw_input("请输入注册密码：").strip()
    passd_re = raw_input("重新输入注册密码：").strip()
    reg(name,passwd,passd_re)
