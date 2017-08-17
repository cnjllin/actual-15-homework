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

# 读黑名单文件    
#def read_lock_file():
#    lock_list=[]
#    with open('lock.txt') as f:
#        for line in f:
#            lock_list.append(line.split('\n')[0])
#    return lock_list

# 写入黑名单文件
#def write_lock_file(user):
#    with open('lock.txt','a+') as f:
#            f.writelines("%s\n"%user)
#            return '账户加入黑名单'



# 注册
def register(user,pwd):
    #user=raw_input('输入你的用户名：').strip()
    # 用户名为空退出
    #if len(user)==0:
    #    return '用户名不能为空'
    
    # 判断用户是否加入了黑名单
    #lock_list=read_lock_file()
    #print lock_list
    #if user in lock_list:
    #    return  '该用户已加入黑名单'
    
    # 判断用户名是否存在
    user_dict=read_file()
    user_list=[]
    for k,v in user_dict.items():
        user_list.append(k)
    #print pwd_list    
    if user in user_list or len(pwd)<6:
        return '1'
    #else:
    #    pwd=raw_input('输入密码：')
        # 用户名不能小于6位
    #if len(pwd)<6:
    #    return '1'
    else:
            # 把用户名和密码写入文件
        #user_list.append(user)
        #pwd_list.append(pwd)
            #print user_list
        #new_user_dict={}
        #new_list=[]
        #new_user_list.append(pwd)
        #new_user_list.append(mail)
        #new_user_list.append(phone)
        #ne_user_dict=[user]=new_user_list
        #user_login.write_file(new_user_dict)
        return '0'


#a=register()
#print a            
            
# 登录
def login(user,pwd):
   # user=raw_input('输入你的用户名：').strip()
    
    # 用户名为空退出
    #if len(user)==0:
    #    return '用户名不能为空'
    
    # 判断用户是否在黑名单
    #lock_list=read_lock_file()
    #print lock_list
    #if user in lock_list:
    #    return  '该用户已加入黑名单'
    
    #判断用户名是否存在，存在输入密码，不存在退出
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
    
# 登录测试
#a=login()
#print a

#def start():
#    a=raw_input('register/login')
#    if a=='register':
#        return register()
#    elif a=='login':
#        return login()
#    else:
#        return '输入有误'
    
#a=start()
#print a




