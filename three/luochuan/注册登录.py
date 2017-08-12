# -*- coding: utf-8 -*-
def register():
    f = open('E:\\PYTHON-TEST\\zhuce.log', 'a+')     #打开文件并写入
    n = 0
    list = []
    while n <= 3:
        name = raw_input('please input your name: ').strip()         #写入注册用户名
        password = raw_input('please input your password: ').strip()  #写入注册密码
        if len(name) == 0:
            return '用户名不能为空'
            n += 1
            # continue
        elif len(name) != 0 and len(password) == 0:
            return '密码不能为空'
            n += 1
        else:
            f.write('%s:%s\n' % (name, password))      #写入用户名密码，并换行
            f.close()
            return '%s注册成功' % name
            break
    else:
        return '错误次数超过3次'



def login():
    # -*- coding: utf-8 -*-
    with open('E:\\PYTHON-TEST\\zhuce.log', 'r')as f:     #读取注册文件
        user = raw_input('please input your usrname:')      #输入用户名
        dict = {}

        for line in f.readlines():
            dict[line.strip().split(":")[0]] = line.strip().split(":")[1]       #生成用户名和密码对应的字典

        for username in dict:                                       #在字典中遍历用户名
            if user == username:                                    #判断用户名是否存在于字典中
                password = dict[user]                               #找到对应的密码
                passwd = raw_input('please input your password:')
                if passwd == password:                            #判断密码是否正确
                    return 'welcome %s' % username
                    break
                else:
                    return 'your password is not correct'
                    break

            else:
                return ' '
                break


def a():
    choice = raw_input(" register/login :").strip()     #选择登录或者注册
    if choice == 'login':
        return login()                                  #选择登录就调用登录，选择注册则调用注册
    elif choice == 'register':
        return register()
    else:
        return "exit"
r = a()
print  r
