#!/usr/bin/env python
#-*- coding:utf-8 -*-

def judge_register_user(name,phone,passwd):
    user_name = name
    user_phone = phone
    user_passwd = passwd

    if user_name == "":
        error = "The user name cannot be empty"
        return error
    else:
        user_list = []
        with open('./user_file','r') as f:
            for line in f:
                l = line.strip().split(' ')[0]
                user_list.append(l)
        if user_name in user_list:
            error = "User already exists"
            return error
    if user_phone == "":
        error = "The phone number can't be empty"
        return error
    if len(user_phone) != 11:
        error = "Cell phone number error"
        return error
    if user_passwd == "":
        error = "The password cannot be empty"
        return error
    if len(user_passwd) <= 6:
        error = "The password number must be greater than 6 digits"
        return error
    else:
        error = ""
        return error

def judge_login_user(name,passwd):
    user_name = name
    user_passwd = passwd
    user_list = []
    with open('./user_file','r') as f:
        for line in f:
            user,num,passwd = line.strip().split(' ')
            user_list.append({'user':user,'num':num,'passwd':passwd})
    for i in user_list:
        if user_name == i['user']:
            if user_passwd == i['passwd']:
                ret = "Login successful"
            else:
                ret = "The password is wrong"
            return  ret
        else:
            continue
    ret = "Users don't exist,Please register first"
    return ret
