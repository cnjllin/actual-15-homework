#! /usr/bin/env python
#coding:utf-8

#初始化数据
user = []

#判断用户名是否存在
def judge_user(username):
    with open("abc.txt",'r') as f:
        for x in f:
            user.append(x.strip().split(":")[0])
        if username in user:
            return 1
        else:
            return 0
