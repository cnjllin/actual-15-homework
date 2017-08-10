#!/usr/bin/env python
#_*_coding:utf-8_*_
# 写一个注册函数和一个登陆函数

# 读文件
def read_file():
    user_dict={}
    with open('user.txt') as f:
        for line in f:
            tmp=line.split(':')
            user_dict[tmp[0]]=tmp[1].split()[0]
    return user_dict
        
# 写文件
def write_file(user_dict):
    with open('user.txt','w') as f:
        for k,v in user_dict.items():
            data="%s:%s\n"%(k,v)
            f.write(data)
        return '注册成功'

# 读黑名单文件    
def read_lock_file():
    lock_list=[]
    with open('lock.txt') as f:
        for line in f:
            lock_list.append(line.split('\n')[0])
    return lock_list

# 写入黑名单文件
def write_lock_file(user):
    with open('lock.txt','a+') as f:
            f.writelines("%s\n"%user)
            return '账户加入黑名单'
# 注册
def register():
    user=raw_input('输入你的用户名：')
    # 用户名为空退出
    if len(user)==0:
        return '用户名不能为空'
    
    # 判断用户是否加入了黑名单
    lock_list=read_lock_file()
    #print lock_list
    if user in lock_list:
        return  '该用户已加入黑名单'
    
    # 判断用户名是否存在
    user_dict=read_file()
    user_list=[]
    pwd_list=[]
    for k,v in user_dict.items():
        user_list.append(k)
        pwd_list.append(v)
    #print pwd_list    
    if user in user_list:
        return '用户已存在'
    else:
        pwd=raw_input('输入密码：')
        # 用户名不能小于6位
        if len(pwd)<6:
            return '密码不能小于6位'
        else:
            # 把用户名和密码写入文件
            user_list.append(user)
            pwd_list.append(pwd)
            #print user_list
            new_user_dict={}
            for i in range(len(user_list)):
                new_user_dict[user_list[i]]=pwd_list[i]
            #print new_user_dict
            write_file(new_user_dict)
            return '注册成功'


#a=register()
#print a            
            
# 登录
def login():
    user=raw_input('输入你的用户名：')
    
    # 用户名为空退出
    if len(user)==0:
        return '用户名不能为空'
    
    # 判断用户是否在黑名单
    lock_list=read_lock_file()
    #print lock_list
    if user in lock_list:
        return  '该用户已加入黑名单'
    
    #判断用户名是否存在，存在输入密码，不存在退出
    user_dict=read_file()
    user_list=[]
    pwd_list=[]
    for k,v in user_dict.items():
        user_list.append(k)
        pwd_list.append(v)
    #print pwd_list    
    if user not in user_list:
        return '用户不存在'
    else:
        count=0
        while True:
            count+=1
            pwd=raw_input('输入密码:')
            
            # 密码输入三次锁定，加入黑名单，用户文件同时删除对应用户名和密码
            if count>=3:
                write_lock_file(user)
                user_dict.pop(user)
                write_file(user_dict)
                return '加入黑名单'
            
            # 密码输入长度不能小于6位
            if len(pwd)<6:
                print '密码长度不能小于6位'
                continue 
            
            # 判断密码是否正确
            if pwd==pwd_list[user_list.index(user)]:
                return '登录成功'    
            else:
                print '密码错误'
                continue
    
# 登录测试
#a=login()
#print a




