#!/usr/bin/python
# -*- coding:utf-8 -*-

users = [
{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},
{'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},
{'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}
]

username = raw_input("pls input username: ").strip()

for userinfo in users:
    real_username = userinfo['name']
    real_password = userinfo['passwd']
    if username == real_username:
        password = raw_input("pls input your password: ").strip()
        if password == real_password:
            print "login successfully"
            break
        else:
            print "wrong password"
    else:
        pass
