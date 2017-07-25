#!/usr/bin/env python
#-*- coding:utf-8 -*-


user = 'liruizhong'
passwd = 'reboot@123'
count = 0

while True:
    user_name = raw_input("Please input your name:")
    if user_name == user:
        while count < 3:
            user_passwd = raw_input("Please input your passwd:")
            if len(user_passwd) <= 6:
                count += 1
                if count == 3:
                    print "\033[31mThree password errors, account locking\033[0m"
                    break 
                print "\033[33mThe password number must exceed 6\033[0m"
                continue
            if user_passwd == passwd:
                print "\033[32mLogin successful\033[0m"
                break
            else:
                count += 1
                if count == 3:
                    print "\033[31mThree password errors, account locking\033[0m"
                    break 
                print "\033[31mSorry,The password you entered is incorrect. Please enter again\033[0m"
        break
    else:
        print "\033[33mSorry,The user you entered does not exist.Please enter again\033[0m"

