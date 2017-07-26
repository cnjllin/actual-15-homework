#!/usr/bin/python
#-!-  coding: UTF-8

def if_user_locked(u):
    locked_user=open('user_locked.txt')
    for name in locked_user.readlines():
        name=name.strip('\n')
        if u == name:
            return 'locked'
def if_login_ok(u,p):    
    user_message=open('user_messages.txt')
    for line in user_message.readlines():
        user,passdb1=line.strip(' ').split()
        if u==user and p==passdb1:
            return 'True'
        else:
            return 'False'

if __name__ == '__main__':
    count=0
    times=0
    while times< 3:
        user_name=raw_input("please input your username: ")
        user_pass=raw_input("please input your password: ")
        count=count+1
        times=times+1
        user_status=if_user_locked(user_name)
        if user_status=='locked':
            print "user {} is locked".format(user_name)
            exit(1)
        if len(user_pass)<=6 :
            print "password is too simple"
            print "you have {} times left".format(3-times)
        else :
            if  if_login_ok(user_name,user_pass)!='True':
                print "账号或密码不正确."
                print "you have {} times left".format(3-times)
            else:
                print "login ok,welcom {}".format(user_name)
                break

    else:
        user_locked=open('user_locked.txt','a')
        user_locked.write(user_name)
        user_locked.write("\n")
        user_locked.close()
        print "你的机会用完了,用户已被锁定 "    
