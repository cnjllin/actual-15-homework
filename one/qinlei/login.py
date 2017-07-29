#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# by greatestray

import os,sys,crypt

def get_uarray(user_file):
    ''' 返回用户名列表 '''    

    with open(user_file,"r") as f:
        user_file_content = f.readlines()
        uarray = [x.split(":")[0] for x in user_file_content ]
        return uarray


def get_passwd(passwd_file,user_name):
    ''' 返回密码列表 '''    

    with open(passwd_file, "r") as f:
        passwd_file_content = f.readlines()

        for i in passwd_file_content:

            user = i.split(":")[0]
            passwd = i.split(":")[1]
            if user_name == user:
                return passwd
               

def test_passwd(passwd,input_passwd):
    ''' 返回密码校验 '''
    
    sys_passwd = passwd.split("$")[-1]
    salt = '$6' + '$' + passwd.split("$")[-2] + '$'
    enct = crypt.crypt(input_passwd,salt)
    if enct.split("$")[-1] == sys_passwd:
        return True

'''
def add_user(user_name):
    useradd = "useradd %s" %user_name
    os.system(useradd)

def del_user(user_name):
    userdel = "userdel -r %s" %user_name
    os.system(userdel)

def lock_user(user_name):
    lusermod = "usermod -L %s" %user_name
    os.system(usermod)    

def ulock_user(user_name):
    ulock = "usermod -U %s" %user_nme
    os.system(ulock)
'''

if __name__=="__main__":

    passwd_file="/etc/shadow"
    user_file="/etc/passwd"

    count = 0


    user_name = raw_input("Pls enter your user name:")
    passwd = get_passwd(passwd_file, user_name)

    
    if user_name in get_uarray(user_file):

        if passwd.split("$")[0] == "!":
            print "%s is lock." % user_name 
            sys.exit()
        else:
            while count <3:
                input_passwd = raw_input("Pls enter your passwd:")
                if test_passwd(passwd,input_passwd):
                    print "sucessful"
                    sys.exit()
                else:
                    print "passwd error"
                    count += 1
            else:
                cmd = "usermod -L %s" %user_name
                #print "cmd", cmd
                os.system(cmd)
                sys.exit()
                    
    else:
        yn = raw_input("%s 不存在,不添加就退出？y:" %user_name)
        #useradd() 
        if yn == "y":
            adduser = "useradd %s" % user_name
            os.system(adduser)
            new_passwd = raw_input("Pls input your passwd:")
            if len(new_passwd) > 6:
                passwd_cmd = "echo %s | passwd --stdin %s" %(new_passwd, user_name)
                os.system(passwd_cmd)
            else:
                print "密码不能小于6位"

        else:
            print "bye"
            sys.exit()




