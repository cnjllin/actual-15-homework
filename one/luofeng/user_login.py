#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Description: judge user login 

import sys
retry_count = 3
count = 0
username = "luofeng"
password = "123456"

user = raw_input("please input your username: ").strip()  # 判断用户是否在黑名单中，如果在黑名单提示后就推出整个程序.
with open('black_list.txt', 'r') as lock_read:
    for lock in lock_read:
        lock_user = lock.strip()
        if lock_user == user:
            print "\033[31mError, %s The user has been locked in the blacklist.\033[0m" % (user)
            sys.exit(1)
        else:
            continue

while True:
    if user == username:    # 用户名正确，提示输入密码
        passwd = raw_input("please input your password: ").strip()
        count = count + 1
        retry_count = retry_count - 1
        if len(passwd) != 6:    # 判断密码的长度是否匹配6位，不匹配就提示用户输入，并减少密码重试的次数.
            print "\033[31mError: The password does not match six lengths and there are %d retries.\033[0m" % (retry_count)
            if count == 3:   # 判断用户输入密码重试的次数，如果满足三次，则提示非法操作，用户将被锁定.
                print "\033[31mError: Very operation, the user will be locked.\033[0m"
                with open('black_list.txt', 'a+') as lock:
                    lock.write(user)
                    lock.write("\n")
                    break
        else:
            if passwd == password:
                print "\033[32mhello ,%s login success.\033[0m" % (user)
                break
            else:
                print "\033[31mError: Password error, You have %d more chances，please re-enter.\033[0m" % (retry_count)
                if count == 3:
                    print "\033[35mError: Login once, the user is locked.\033[0m"
                    with open('black_list.txt', 'a+') as lock:
                        lock.write(user)
                        lock.write("\n")
                        break
    else:
        print "\033[31mError: %s Users don't exist, plase retry input username.\033[0m" % (user)
        user = raw_input("please input your username: ").strip()
