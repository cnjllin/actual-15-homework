#!/bin/user/python
#coding:utf-8
def sign():
    f = open('/root/actual-15-homework/three/chenfei/config/user.txt','a+')
    while True:
        name = raw_input("请输入姓名:").strip()
        if len(name)==0:
             print "用户名不能为空，请重新输入"
             break;
        else:
	    password = raw_input("请输入密码:").strip()
	    repass = raw_input("请再次输入密码:").strip()
            if len(password)==0 or password !=repass:
	            print"密码输入有误"
                    continue;
	    else:
		    f.write("%s:%s\n"%(name,password))
		    f.close()
		    print "恭喜你，注册成功"
                    break;
