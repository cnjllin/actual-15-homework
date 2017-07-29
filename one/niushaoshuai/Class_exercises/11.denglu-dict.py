#!/usr/bin/python
# --*-- UTF-8 --*--
users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'}, {'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},{'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}]
def if_user_exist(name):
    for L in users:
        if L['name']==name:
            return 'ok'

if __name__ == '__main__':
    user_name = raw_input("please input your name: ")
    if if_user_exist(user_name) :
        user_pass = raw_input("please input your password: ")
        for L in users:
                if L['name']==user_name:
                    if L['passwd'] == user_pass:
                        print "login ok ,you message is {}".format(L)
                        break
                    else:
                        print "input a error password!"
                        pass
    else:
        print "user is not exist!"
        exit(1)

