# /usr/bin/env python
# coding:utf-8
User_Name = raw_input("请输入你的用户名：")
n = 3
#判断用户名是否为wj
if User_Name == 'wj':
    while n > 0:
        Passwd = raw_input("请输入你的密码：")
#判断密码长度是否大于等于6位
        if len(Passwd) >= 6:
            if Passwd == '123456':
                print "欢迎回来，%s" % User_Name
            else:
                n = n - 1
                if n == 0:
                    print "三次机会用完了，再见"
                    break
                print '密码错误，请重试,还剩余 %s次' % n


        else:
            print "密码需要六位以上，请重试"
            continue
else:
    print "用户不存在"
