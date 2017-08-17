#!/usr/bin/env python
#_*_coding:utf-8_*_
# 写一个注册函数和一个登陆函数

# 读文件
def read_file():
    user_dict={}
    with open('user.txt') as f:
        for line in f:
            tmp=line.split(':')
            user_list=[]
            user_list.append(tmp[1])
            user_list.append(tmp[2])
            user_list.append(tmp[3].split('\n')[0])
            user_dict[tmp[0]]=user_list
    return user_dict


# 写文件
def write_file(user_dict):
    with open('user.txt','a+') as f:
        for k,v in user_dict.items():
            data="%s:%s:%s:%s\n"%(k,v[0],v[1],v[2])
            f.write(data)
        return '1'




# 注册
def register(user,pwd):
    user_dict=read_file()
    user_list=[]
    for k,v in user_dict.items():
        user_list.append(k)
    #print pwd_list    
    if user in user_list or len(pwd)<6:
        return '1'
    else:
        return '0'           
            
# 登录
def login(user,pwd):
    user_dict=read_file()
    user_list=[]
    pwd_list=[]
    for k,v in user_dict.items():
        user_list.append(k)
        pwd_list.append(v[0])
    #print pwd_list    
    if user not in user_list or pwd not in pwd_list:
        return '1'
    if user=='admin' and pwd=='admin':
        return '0'
    elif user in user_list and pwd== pwd_list[user_list.index(user)]:
        return '2'
    




