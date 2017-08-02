#!/usr/bin/env python
#_*_coding:utf-8_*_
#作业：实现用户名密码登陆验证
#1：判断用户名密码是否正确，正确则打印欢迎信息，错误则输出具体错误原因信息
#2：用户可以连续输入三次密码。超过三次则锁定用户
#3：密码位数必须超过6位
#@count 统计输入密码次数
#@name：用户名
#@password：用户密码
print '测试：用户名：lk，密码：123456'
print '密码输错三次锁定'
while True: 
    name=raw_input('\033[32m请输入用户名:\033[0m')  #用户输入用户名
    if name=='lk':              #判断
        for i in range(3):       #只能输入3次
            print '\033[31m你还有%s次机会输入密码\033[0m'%(3-i)
            password=raw_input('\033[32m请输入密码:\033[0m')
            if password=='123456':
                print '\033[5;32m登录成功\033[0m '
                print '\033[5;32m欢迎%s\033[0m'%name
                break
            elif len(password)<6:
                print '\033[31m请输入6位以上密码\033[0m'
            elif i==2:
                print '\033[5;30;45m密码已锁定，请联系管理员\033[0m'
            else:
                print '\033[31m密码错误\033[0m'
        break               
    elif name=='exit':
        print '\033[32m欢迎下次登录\033[0m'
        break
    else:
        print '\033[31m对不起，%s不存在,请重新输入\033[0m'%name
        print '\033[1;30;41m输入exit退出程序\033[0m'
