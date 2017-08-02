#!/usr/bin/env python
# coding: utf-8

dict1 = {'username': 'reboot', 'password': '12345678'}
x = raw_input("UserName:")
i = 0
if x == dict1['username']:
    while i < 3:
        p = raw_input("Password:")
        if  len(str(p)) < 6:
             print('密码少于6位')
             i += 1
        elif p == dict1['password']:
            print ("登录成功")
            break
        elif p != dict1['password']:
            print ("密码错误")
            i += 1
    print ("用户已锁定")

else:
     print ('用户不存在')

