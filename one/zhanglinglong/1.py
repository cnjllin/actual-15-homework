#/usr/bin/python
#coding:utf-8
# 输入错误，回车前可以清除
import readline
name = raw_input("请输入用户名：").strip()
if name == "zll":
    count = 0    
    while count <= 3:
        passwd = raw_input("请输入密码：")
        passwd = passwd.strip()
        # 如果密码正确，打印欢迎信息
        if passwd == "ilikeit":
            print "欢迎%s登录" %name
            break
        # 如果密码少于6位，直接退出
        if len(passwd) <6:
            print "密码位数必须超过6位"
            break
        # 如果密码输入错误，提示错误，并且最多可以输入3次，超过3次后退出
        if count < 3:
            print "密码错误，你还有%s次机会" %(3 - count)
            count +=1
        else:
            print "输入次数过多"
            break
else:
    print "账号%s不存在" %name
