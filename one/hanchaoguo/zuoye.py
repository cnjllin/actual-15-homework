#!/usr/bin/python
#coding:utf-8
user = 'han'
passwd = '123456789'
count = 0
name = raw_input('pls input username:')
if name ==  user:
    while count < 3:    
        pw = raw_input('pls input password:')
        if len(pw) < 6:
            count +=1 
            print '\033[31m this password  must be greater than 6 \033[0m'
            print '\033[33m You have %s more chances \033[0m' %(3 - count)
        else: 
            if pw == passwd:
                print '\033[32m welcome %s \033[0m' %user
                break
            else:
                count +=1
                print '\033[31m password  error \033[0m'
                print '\033[33m You have %s more chances \033[0m ' %(3 - count)
    else:
        print '\033[31m Your account has been locked \033[0m '
else:       
    print '\033[31m name is error \033[0m'
    
