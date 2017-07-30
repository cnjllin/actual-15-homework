#!/usr/bin/python
#coding:utf-8
num1 = 50
count = 1
while count <= 3:
	if count == 3:
		print "你还有最后一次机会"
	num2 = int(raw_input("输入数字: "))
	print type(num2)
	if num2 == num1:
		print "恭喜你，答对了"
		break
	elif num2 > num1:
		print "%s,数字大了,剩%s次机会"%(num2,3-count)
	else:
		print "%s,数字小了,剩%s次机会"%(num2,3-count)
	count+=1
else:
	print "game over,3Q"
print "bye bye"
