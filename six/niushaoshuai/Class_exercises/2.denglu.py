#!/usr/bin/python
#-*-coding: UTF-8
name = raw_input("please input your name: ")
nm="牛少帅"
pwd="nss"
if name==nm :
    pass01 = raw_input("please input your password: ")
    if pass01==pwd:
        print "welcom {}".format(name)
    else:
        print "input a error password!"
else:
    print "user is not exist!"
    exit(1)
