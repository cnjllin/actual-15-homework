#!/usr/bin/python
# --*-- coding:UTF-8 --*--

f = open('user_message.db', 'r')
message = f.readlines()
user=dict()
for  line in message:
    mu = line.split(':')[0]
    mp = line.split(':')[1].strip(' \n')
    user[mu]=mp
f.close()

def checkout_user_pass(u, p):
    if u in user.keys():
        if user[u] == p:
            return True
        else:
            return False
    else:
        return False

def checkout_user_exist(u):
    if  u in user.keys():
        return True
    else:
        return False
if __name__ == '__main__':
    print checkout_user_pass('niushaoshuai1','123456')
    print checkout_user_exist('niushaoshuai12')
