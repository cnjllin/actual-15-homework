#!/usr/bin/python
#coding:utf-8
# 输入错误，回车前可以清除
import readline
f = open('user.txt')
name = raw_input("请输入登录用户名：").strip()
l = []
k = {}
for i in f.readlines():
    i =i.strip('\n')
    #将用户信息条，按照:来切片，获取用户名
    a = i.split(':')[0]
    b = i.split(':')[1]
    k[a] = b
    #将用户名追加到列表中
    l.append(a)
#print k
#print l
if name not in l:
    print "用户名不存在"
    exit()
else:
    passwd = raw_input("请输入登录密码：").strip()
    if passwd == k.get(name):
        print "欢迎%s登录" %name
    else:
        print "登录密码错误"
f.close()
