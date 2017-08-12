#/usr/local/bin/python3
#coding:utf-8

def register():
    username = raw_input("请输入用户名:")
    if username == '':
        print  "您输入的用户为空"
    else:
        password = raw_input("请输入您的密码: ")
        if password == '':
            print "您输入的密码为空"
        else:
            password_two = raw_input("请您再次输入的密码: ")
            if password == password_two:
                File = open('user.txt','a+')
                File.write('%s:%s\n' % (username,password))
                File.close()
                print "恭喜你,%s用户注册成功" % username
            else:
                print "密码不匹配"

def login():
	user = raw_input("请输入您的用户名: ")
	users = {}
	with open('user.txt','r') as file:
		for line in file.readlines():
			users[line.strip().split(":")[0]] = line.strip().split(":")[1]
	if users.has_key(user):
		pwd = raw_input("请输入您的密码: ")
		if pwd == users[user]:
			print "恭喜您%s成功登录" % user
		else:
			print "您的密码不正确"
	else:
		print "对不起，你输入的%s用户不存在" % user

def start():	
	action = raw_input("请输入 login or register :").strip()
	if action == "register":
		register()
	if action == "login":
		login()
	else:
		print "input is null"
start()
