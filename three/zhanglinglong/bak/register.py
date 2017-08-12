#!/usr/bin/python
#coding:utf-8
# 输入错误，回车前可以清除
import readline
f = open('user.txt','a+')
name = raw_input("请输入注册用户名：").strip()
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
#判断注册密码，是否为空，输入密码和确认密码是否匹配，最多可输入3次，超过则提示并退出
count =0
while count < 3:
    passwd = raw_input("请输入注册密码：").strip()
    passd_re = raw_input("重新输入注册密码：").strip()
    #判断注册密码是否为空
    if len(passwd) == 0:
        print "密码不能为空"
        count +=1
    #判断两次输入密码是否匹配，如果匹配则提示注册成功，如果不匹配，提示不匹配并退出
    if passd_re == passwd:
        print "注册成功，您的账号为:%s,密码为:%s,请妥善保管" %(name,passwd)
        f.write('%s:%s\n' %(name,passwd))
        exit()
    else:
        print "密码不匹配"
        count +=1
print "输入次数过错"
f.close()
