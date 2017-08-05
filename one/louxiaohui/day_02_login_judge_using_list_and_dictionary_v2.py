#!/usr/bin/python
# -*- coding:utf-8 -*-

users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},{'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},{'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}]

username = raw_input("please input your username: ").strip()
dict_tmp = {}

# index indicate the index of users list
# user indicate the content corresponding to the index
# enumerate is a built-in function of list
for index,user in enumerate(users):
    # dict_tmp is a dictionary storing the user_name key and its index of the list
    dict_tmp[user['name']] = index

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
            print "welcome to CMDB system,%(name)s.Your job is %(job)s,age is %(age)s,hope you have a good time here." % user_info
            break
        else:
            total_times = 2-i
            if total_times == 0:
                print "the password you input is wrong,you have input wrongly more than 3 time,bye bye."
            else:
                print "the password you input is wrong,please input again,you have %s times to try." % total_times
else:
    print "the user you input does not exist"
