#!/usr/bin/python
#encoding: utf-8
#name:renwei
#email:1059014651@qq.com
#time:201707292230
name = "baihui"
passwd = "7654321"
count = 0
time  = 3
username = raw_input("请输入您的用户名: ")
if username == name:
   while count <3:
      userpasswd = raw_input("请输入您的密码: ")
      if userpasswd == passwd:
         print "欢迎您登陆!"
         break
      else:
         time -=1
         conut +=1
         if len(userpasswd)<6:
            print "密码错误并且位数小于6位数，请重新输入密码，还有()次数机会".format(time)
         else:
            print "密码错误，请重新输入密码，还有()次数机会".format(time)
    else:
        print "对不起，3次机会用完，您的账户 {} 被锁定".format(username)
else:
    print "用户名 {} 错误,请重新登录!".format(username)
