count = 0
while count<3:
	count=count+1	
	name = raw_input("please your name:")
	pwd = raw_input("please your passwd:")
	passwd = '123456'

	if name == 'tangbo' and pwd == passwd:
		print "Wellcome To Success" 
		break
	else:
		print "Sorry,not check!" 
	
