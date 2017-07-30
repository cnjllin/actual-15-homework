num=50
count = 0
while count < 3:
	count += 1
	guess = True
        try:
		Guess_num = int(raw_input("Please Your Number:"))
		if Guess_num > num:
			print "This is too Big!!!"
		elif Guess_num < num:
			print "This is too small!!!"
		else:
			print "Success!!"
			break;
	except Exception:
            print "Please Input Numer:"	
	
	
