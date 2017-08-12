#!/usr/bin/env python 
# _*_ coding: utf-8 _*_ 
# File Name: user_login.py
# Author: luofeng
# Mail: 18210085737@139.com 
# Blog: https://www.liyanlan.com 

import sys

def regis():
	count = 0
	username = raw_input("please input your name: ").strip()
	# Check the length of the username
	if len(username) == 0:
   		print "\033[31mError: User names are not allowed to be empty.\033[0m"
   		sys.exit(-1)

	# 
	while True:
   		count = count + 1
		# Check the number of times the user enters the password
   		if count > 3:
   			print "\033[31mError: false.\033[0m"
   			break

   		passwd = raw_input("please input your password: ").strip()
		# Check the length of the user's password
   		if len(passwd) != 0 and len(passwd) < 6:
   			print "\033[31mError: User passwords cannot be empty and less than 6 digits.\033[0m"
   			break
   		else:
   			res_passwd = raw_input("Please re-enter your password: ").strip()
			# Verify that the two passwords are consistent  
   			if res_passwd != passwd:
   				print "\033[31mError: Two passwords are different.\033[0m"
   			else:
   				print "\033[32m%s reigs is success.\033[0m" %(username)
 				with open('user.txt', 'w') as f:
					f.write("%s:%s\n" %(username, res_passwd))
					break

def login():
	users = {}
	count = 0
	retry_count = 3

	with open('user.txt','r') as f:
		result = f.readlines()

	# get user and passwd
	for x in result:
		login_user = x.strip("\n").split(':')[0]
		users[login_user] = x.strip("\n").split(':')[1]

	# chekc user is exist
	username = raw_input('please input your username: ').strip()
	if username not  in users:
		print "\033[31mError: {0} is not exist.\033[0m".format(username)
		sys.exit(-1)

	while True:
		count = count + 1
		retry_count = retry_count - 1
		if count > 3:
			print "\033[31mError: Login exception, user has been locked.\033[0m"
			break

		password = raw_input("please input your password: ").strip()
		if password == users[username]:
			print "\033[32m{0} login is success.\033[0m".format(username)
			break
		else:
			print "\033[35mError: login password is error, And then there's the {0} opportunity\033[0m".format(retry_count)

def start():
	action = raw_input('\033[32mplease input regis/login: \033[0m').strip()
	if action == "login":
		result = login()
		return result
	elif action == "regis":
		result = regis()
		return result
	else:
		print "\033[31mError: Please input regis or login.\033[0m"

if __name__ == "__main__":
	start()
