#!/usr/bin/python
# --*-- coding:UTF-8 --*--
import userconf

def GetUser():
    f = open(userconf.USER_FILE, 'r')
    message = f.readlines()
    f.close()
    user_info=dict()
    for  line in message:
        mu = line.strip(' \n').split(':')[0]
        mp = line.strip(' \n').split(':')[1]
        user_info[mu]=mp
    return user_info

def checkout_user_pass(u, p):
    user=GetUser()
    if u in user.keys():
        if user[u] == p :
            return True

        else:
            return False
   
    else:
            return False

def checkout_user_exist(u):
    user=GetUser()
    if  u in user.keys():
        return True
    else:
        return False
if __name__ == '__main__':
#    print checkout_user_pass('niushaoshuai1','123456')
#    print checkout_user_exist('niushaoshuai12')
    print checkout_user_pass('owen8','123')
