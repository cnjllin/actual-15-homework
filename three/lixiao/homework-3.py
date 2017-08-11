#!/usr/bin/python
#coding:utf-8

def login():
    name = []
    res = {}
    with open('/python/user.txt') as files:
        data = files.readlines()
        for n in data:
            name.append(n.split(':'))
        for i in range(len(name)):
            res[name[i][0]]=name[i][1].strip()

    while True:
        login_name = raw_input('please input login username: ')
        if login_name not in res:
            print "user not is exist!"
            continue
        else:
            login_pwd = raw_input('please input login passwd: ')
            if login_pwd != res[login_name]:
                print 'pwd is wrong'
            else:
                print "sucess"
                break
def reg():
    fo = open('/python/user.txt','a+')
    while True:
        name = raw_input('请输入用户名: ').strip()
        if name == "":
            print "sorry,用户名不能为空！"
       
        if name != "":
            passwd = raw_input('请输入密码: ').strip()
            re_passwd = raw_input('请再次输入密码：').strip()
            if passwd != re_passwd or len(passwd) == 0:
                print "输入的密码不一致！请重新输入"
            else:
                fo.write('%s:%s''\n' %(name,passwd))
                print "恭喜，注册成功"
                break
    fo.close

def null():
    print "please input reg or login! Think you"

def start():
    action  = raw_input('pelase input reg or login: ').strip()
    if action == 'reg':
        res = reg()
    elif action == 'login':
        res = login()
    else:
        res = null()
    return res 
result = start()
#print result
