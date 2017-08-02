name = raw_input('input your name: ').strip()
if name == 'liuyang':
	passwd = raw_input('input your passwd: ')
	if passwd == '123456':
		print'User %s Login sucessfully'%(name)
	else:
		print 'Wrong passwd,please input again'
else:
	print "User %s not exists,please conform"%(name)
