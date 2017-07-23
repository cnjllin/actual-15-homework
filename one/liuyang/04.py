#/usr/bin/python
#coding=utf-8
import sys
compare_num = 50
count = 0
while count<=3:
	input_num = raw_input('input a number: ')
	try:
		num = int(num)
	except Exception,e:
		print '输入非法'
		sys.exit()
	time = 3-count
	if input_num > compare_num:
		print '输入的数字太大,还有%s次机会'%(time)
	elif input_num < compare_num:
		print '输入的数字太小,还有%s次机会'%(time)
	else:
		print '输入数字正确'
		break
	count +=1
