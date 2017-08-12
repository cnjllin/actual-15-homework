#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
# ==========================================
#      FileName: login_register.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-08-11
# ==========================================
"""


import sys


def directory():
    # The directory information
    print "\033[33m******************************\033[0m"
    print "\033[33m*    Welcome to my website   *\033[0m"
    print "\033[33m*    Registration 1          *\033[0m"
    print "\033[33m*    Login input  2          *\033[0m"
    print "\033[33m*    Exit input   3          *\033[0m"
    print "\033[33m******************************\033[0m"
    usage = raw_input("\033[32mPlease select the operation you want:\033[0m").strip()
    return usage

def judge_user(username):
    # Determine whether the user exists
    with open('./user_file','r') as f:
        user = []
        for l in f:
            user.append(l.strip().split(':')[0])
        if username in user:
            return 1
        else:
            return 0

def register():
    # User registration function
    user_name = raw_input("\033[32mPlease enter the username:\033[0m").strip()
    ret = judge_user(user_name)
    if ret == 0:
        passwd_first = raw_input("\033[32mPlease enter your password:\033[0m").strip()
        passwd_second = raw_input("\033[32mEnter password again:\033[0m").strip()
        if passwd_first == passwd_second:
            with open('./user_file','a') as f:
                f.write("{0}:{1}\n".format(user_name,passwd_first))
                print "\033[33mRegistration success\033[0m"
        else:
            print "\033[31mThe two input passwords do not match!\033[0m"
        sys.exit(0)
    else:
        print "\033[31mUsers already exist\033[0m"
        sys.exit(0)

def login():
    # User login function
    user_name = raw_input("\033[32mPlease enter the username:\033[0m").strip()
    ret = judge_user(user_name)
    if ret == 1:
        passwd = raw_input("\033[32mPlease enter your password:\033[0m").strip()
        dict1 = {}
        with open('./user_file','r') as f:
            for i in f:
                k,v = i.strip().split(':')
                dict1.update({k:v})
        if passwd == dict1[user_name]:
            print "\033[33mLogin successfully\033[0m"
        else:
            print "\033[31mPassword mistake\033[0m"
        sys.exit(0)
    else:
        print "\033[31mUsers don't exist\033[0m"
        sys.exit(0)


if __name__ == '__main__':
    usage = directory()
    if int(usage) == 1:
        register()
    elif int(usage) == 2:
        login()
    elif int(usage) == 3:
        sys.exit(0)
    else:
        print "\033[32mPlease re-enter!\033[0m"
