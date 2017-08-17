#!/bin/env python
# -*- coding:utf-8 -*-

class User(object):
    ''' 用户类 '''
    def __init__(self, name, passwd, rule = 1): 
        ''' 初始化当前用户  '''
        self.name =  name
        self.passwd = passwd
        self.rule = rule

    def user_reg(self):
        ''' 将当前用户写入文件 '''
        with open('user.txt','a+') as f : 
            f.write(str(self.name) + ':' + str(self.passwd) + '\n')

    def user_del(self, username) :
        '''当前用户rule=0为管理员，可以删除其他用户'''
        if self.rule == 0 : 
            users = dict()
            with open('user.txt','w+') as f : 
                users = { line.split(':')[0] : line.split(':')[1].rstrip() for line in f } 
            del users[username]
            with open('user.txt','a+') as f : 
                for k,v in users.items() :
                    f.write(str(k) + ':' + str(v) + '\n')

    def user_get(self):
        ''' 用户存在 返回密码  否则 False '''
        with open('user.txt','r') as f : 
            for line in f:
                if self.name == line.split(':')[0] :
                    #res = True
                    res = line.split(':')[1].rstrip()
                    break
            else :
                res = False
        return res
