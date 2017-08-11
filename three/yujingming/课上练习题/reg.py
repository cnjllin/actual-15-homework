#!/usr/bin/env python
# If name=tangseng & password=88888888, print login welcom info.
# v2.0  Yujingming 20170726

f =open('data.txt','a+')
while True: 
	name = raw_input("Please input the name:").strip()
	if len(name) == 0:
		print "User not exist, please input again:"
		break #
	else:
		password = raw_input("Please input the pwd:").strip()
		repass = raw_input("Please input the pwd:").strip()
		if len(password)==0 or password !=repass:
			print "pwd wrong"
			continue #
		else:
			f.write("%s:%s\n" % (name,password))
			f.close()
			print "Fine!sign up success"
			break
