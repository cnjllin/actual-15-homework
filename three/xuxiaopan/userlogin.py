#coding:utf-8

def Login(username,passowrd):
    """
    用户登录
    :param username:用户输入用户名 
    :param passowrd: 用户输入密码
    :return: 返回成功或者失败
    """
    f = open('db.txt', 'r')
    for line in f:
        line_list = line.strip().split('|')
        if line_list[0] == username and line_list[1] == passowrd:
            return True
    return False

def Register(username,password):
    """
    用户注册
    :param username: 用户名
    :param password: 密码
    :return: 默认返回None
    """
    f = open('db.txt', 'a')
    temp = '\n' + username + '|' + password
    f.write(temp)
    f.close()

def main():
    t = input("1,登录，2，注册:\n")
    if t == '1':
        user = input('username:')
        pwd = input('password:')
        r = Login(user, pwd)
        if r:
            print('OK')
        else:
            print('No')
    elif t == '2':
        user = input('Username:')
        pwd = input('Password:')
        Register(user, pwd)
        print('OK')
main()
