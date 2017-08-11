#!/usr/bin/python
# --*-- conding:utf-8 --*--
import sys,getpass
f = open('usercf.txt','a+')
name = raw_input("Please input your name:")
if not name.strip():
   print 'name is null please input check'
   sys.exit()
elif name == name and name.isalpha():
   print "Wlecome python user {}".format(name)
else:
    print "The input name is incorrect. Please re-enter it"
    sys.exit()  
#try:
#    password = int(password)
#except Exception, e:
#    print "Password input not int"
total = 3
count = 0
while count < 3:
    total -= 1
#    password = raw_input("Please input your password:")
    password = getpass.getpass('password:')
    if password == password and len(password) == 6:
       f.write("%s:%s\n"% (name,password))
       f.close()
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
    
