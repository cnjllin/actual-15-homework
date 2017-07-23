name = raw_input('input your name: ').strip()
if name == 'liuyang':
	count = 0
	while count<3:
		passwd = raw_input('input your passwd: ')
		if passwd == '123456':
			print'User %s login sucessfully !'%(name)
			break
		else:
			print 'Wrong passwd,please input again !'
		 	count +=1
		print 'passwd wrong three times,the count %s is locked !'%(name)
else:
	print "User %s not exists,please confirm !"%(name)
