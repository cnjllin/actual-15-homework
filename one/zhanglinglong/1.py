#/usr/bin/python
#coding:utf-8
import readline
name = raw_input("请输入用户名：")
if name == "zll":
    count = 0    
    while count <= 3:
        passwd = raw_input("请输入密码：")
        if passwd == "ilikeit":
            break
        else:
	    if len(passwd) <6:
                print "密码位数必须超过6位"
            else: 
                if count < 3:
                    print "密码错误，你还有%s次机会" %(3 - count)
                    count +=1
                else:
                    print "输入次数过多"
                    exit()
    print "欢迎%s登录" %name
else:
    print "账号%s不存在" %name
