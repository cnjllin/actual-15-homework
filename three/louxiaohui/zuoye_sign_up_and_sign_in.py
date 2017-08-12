#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

def check_if_user_exist(username):
    flag = 0
    with open ("user_info","a+") as f:
        for line in f:
            user = line.strip().split(' ')[0]
            if username == user:
                flag = 1
            else:
                flag = 0
        return flag

def user_sign_up():
    username = raw_input("pls input username:")
    if check_if_user_exist(username) == 1:
        print "user is already exist"
    else:
        password = raw_input("pls input passwd:")
        if username == password:
            print "username cannot be the same as password,please input again"
        else:
            with open ("user_info","a+") as f:
                print username,password
                f.write('%s %s\n' %(username,password))   
                print "The user %s has been signed up" % username

# define print info function
def warn_print(content):
    print "\033[0;31;1m%s\033[0m" % content
def info_print(content):
    print "\033[0;32;1m%s\033[0m" % content


# the user info is stored to users list as follows
# users = [{'passwd': '666', 'name': '666'}, {'passwd': '668', 'name': '668'}]
users = []
for i,e in enumerate(open('./user_info','rU')):
    real_username=e.split(' ')[0].strip('\n')
    real_password=e.split(' ')[1].strip('\n')
    string_user_info_dict = {'name': real_username, 'passwd': real_password}
    #users.append({'name': real_username, 'passwd': real_password})
    users.append(string_user_info_dict)
# dict_tmp is a dictionary storing the user_name key and its index of the list
dict_tmp = {}
# index indicate the index of users list
# user indicate the content corresponding to the index
# enumerate is a built-in function of list
for index,user in enumerate(users):
    dict_tmp[user['name']] = index

def user_sign_in():
    # input username
    username = raw_input("pls input username: ").strip()
    if username in dict_tmp:
        for i in range(3):
            # define a dictionary storing the user information including age
            # job,age,name,passwd
            input_password = raw_input("please input your password: ").strip()
            # get the real password from users list
            real_password = users[dict_tmp[username]].get('passwd','default')
            if input_password == real_password:
                # user_info is a dictionary storing detail information of the user
                user_info = users[dict_tmp[username]]
                name = user_info['name']
                content = 'welcome to CMDB system,' + str(name) + '.Hope you have a good time here.'
                info_print(content)
                break
            else:
                total_times = 2-i
                if total_times == 0:
                    content = "the password you input is wrong,you have input wrongly more than 3 time,bye bye."
                    warn_print(content)
                else:
                    content = 'the password you input is wrong,please input again,you have ' + str(total_times) + ' times to try.'
                    warn_print(content)
    else:
        print "the user you input does not exist"

def sign_up_and_sign_in():
    task = raw_input("1 for sign up \n2 for sign in \nplease select:").strip()
    try:
        task = int(task)
    except ValueError,e:
        print "illegal input"
    else:
        if task == 1:
            user_sign_up()
        elif task == 2:
            user_sign_in()
        else:
            print "illegal input number"      

sign_up_and_sign_in()
