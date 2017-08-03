#!/usr/bin/python
#encoding:utf-8
users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': 'wd'},
 {'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'kk'},
 {'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'pc'}]

username = raw_input("please you name: ").strip()
userpass = raw_input("please you pass:").strip()
for i in users:
    if username in i['name']:
        if userpass in i['passwd']:
            print "ok"
            break
        else:
            print "err"
            break
else:
    print "err"
