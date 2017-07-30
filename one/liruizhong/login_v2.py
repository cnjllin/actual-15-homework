#!/usr/bin/env python
#-*- coding:utf-8 -*-

user_list = []

def judge_locked(user):
    with open('./lock_user','r') as f:
        for l in f:
            line = l.strip()
            user_list.append(line)
        if user in user_list:
            return 1
        else:
            return 0 

def lock_user(user):
    with open('./lock_user','a') as f:
        if judge_locked(user) == 0:
            f.write(user+'\n')
            return
        else:
            return

def judge_user(user):
    with open('./user_file','r') as f:
        dict1 = {}
        for l in f:
            k,w = l.strip().split(':')
            dict1[k] = w
    if user not in dict1.keys():
        print "\033[31mUsers don't exist\033[0m"
    else:
        count = 0
        while count < 3:
            user_passwd = raw_input("\033[32mPlease input your passwd:\033[0m").strip()
            if len(user_passwd) > 6:
                if dict1[user] == user_passwd :
                    print "\033[32mLogin successful\033[0m"
                    break
                else:
                    count += 1
                    if count == 3:
                        lock_user(user)
                        print "\033[31mThree password errors, account locking\033[0m"
                        break
                    print "\033[31The password is wrong\033[0m"
                    
            else:
                count +=1
                if count == 3:
                    lock_user(user)
                    print "\033[31mThree password errors, account locking\033[0m"
                    break
                print "\033[33mThe password number must be greater than 6\033[0m"
    return

if __name__ == '__main__':
    user_name = raw_input("\033[32mPlease input your name:\033[0m").strip()
    if judge_locked(user_name) == 1:
        print "\033[31mThe %s user is locked\033[0m" % (user_name)
    else:
        judge_user(user_name)

