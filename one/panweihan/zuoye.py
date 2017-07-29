# -*- coding: utf-8 -*-
username = "panweihan" #定义两个变量，作为用户名和密码
password = "123456"
n = 3
#判断用户名是否正确，如果用户名输入错误，一直提示用户输入
while True:
    login = False
    if n == 0:
        print "你的账户已经被锁定，请联系管理员！"
        break
    name = raw_input("请输入用户名：").strip()
    #如果用户名正确，继续判断密码是否正确
    if name == username:
        #只允许用户输入3次密码，根据不同的情况会显示不同的告警信息：
        #情况1：密码正确；
        #情况2：密码长度不足6位
        #情况3：密码错误,提醒用户剩余次数，当剩余次数为0的时候不再进行同样的提醒”
        for i in range(3):
            pwd = raw_input("请输入密码：")
            n = n - 1
            if pwd == password:
                login = True
                print"欢迎来到%s的世界"%name
                break
            elif len(pwd) < 6 :
                print"密码长度不能小于6位，请再次输入。注意，你只有3次机会！！！"
            elif len(pwd) >= 6 and n > 0:
                print"密码错误，你还有%s次机会，连续错误3次将被锁定"%n
    else:
        print"用户名错误，请重新输入"
    #用户名密码都正确，跳出while循环
    if login == True:
        break


