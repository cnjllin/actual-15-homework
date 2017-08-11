#!/usr/bin/env_python
#coding:utf-8
import sys,getpass
fo = open("usercf.txt")
users = {}
content = fo.readlines()
fo.close()

for user in content:
    name = user.rstrip("\n").split(":")[0]
    users[name]=user.rstrip("\n").split(":")[1]

name1 = raw_input("Please input your name:")
if not name1.strip():
     print 'name is null please input check'
     sys.exit()
elif name1 == name:
    print "Wlecome python user {}".format(name)
else:
    print "The input name is incorrect. Please re-enter it"
    sys.exit()

total = 3
count = 0
while count < 3:
    total -= 1
#    password = raw_input("Please input your password:") 
    password = getpass.getpass('password:')
    if password == users[name] and len(password) == 6:
       print "wlecome python world %s" % (name)
       break
    elif len(password) == 0:
       print "password null input error, Please re-enter the %d input opportunities" % (total)
    elif len(password) > 6:
       print "password biger input error, Please re-enter the %d input opportunities" % (total)
    elif len(password) < 6:
       print "password samller input error, Please re-enter the %d input opportunities" % (total)
    count += 1
else:
    print "password is lock %s please call administrator" % (name)

