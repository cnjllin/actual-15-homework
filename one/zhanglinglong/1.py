#/usr/bin/python
#coding:utf-8
#输入错误，回车前可以清楚
import readline
name = raw_input("请输入用户名：")
if name == "zll":
    count = 0    
    while count <= 3:
        passwd = raw_input("请输入密码：")
        #如果密码正确，打印欢迎信息
        if passwd == "ilikeit":
            print "欢迎%s登录" %name
        #密码少于6位，直接退出
        if len(passwd) <6:
            print "密码位数必须超过6位"
            break
        #密码最多可以输入3次
        if count < 3:
            print "密码错误，你还有%s次机会" %(3 - count)
            count +=1
        else:
            print "输入次数过多"
            break
else:
    print "账号%s不存在" %name
