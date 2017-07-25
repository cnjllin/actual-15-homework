#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# by greatestray

import os,sys,crypt

def op_file(user_file):
    with open(user_file,"r") as f:
        user_file_content = f.readlines()
        squares = [x.split(":")[0] for x in user_file_content ]
        return squares


def get_passwd(passwd_file,user_name):
    
    with open(passwd_file, "r") as f:
        passwd_file_content = f.readlines()

        for i in passwd_file_content:

            user = i.split(":")[0]
            passwd = i.split(":")[1]
            if user_name == user:
                return passwd
               

def test_passwd(passwd,input_passwd):
    
    sys_passwd = passwd.split("$")[-1]
    salt = '$6' + '$' + passwd.split("$")[-2] + '$'
    enct = crypt.crypt(input_passwd,salt)
    if enct.split("$")[-1] == sys_passwd:
        return True


if __name__=="__main__":

    passwd_file="/etc/shadow"
    user_file="/etc/passwd"

    count = 0
  
    user_name = raw_input("Pls enter your user name:")
    passwd = get_passwd(passwd_file, "yutian")

    if user_name in op_file(user_file):

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
        yn = raw_input("%s not exits,:" %user_name)
        #useradd() 
        if yn == "y":
            adduser = "useradd %s" % user_name
            os.system("adduser")
            
        else
            print "bye"
            sys.exit()




