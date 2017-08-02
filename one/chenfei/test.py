count = 0
total = 3
while count < 3:
   total -= 1
   num = raw_input ("please youer want to number:")
   print type(num)
   num = int(num)
   if num == 50:
       print "your input is ok"
       break
   elif num > 50:
       print "your num is biger %d" % total
   elif num < 50:
       print "your num is smaller %d" % total
   count += 1
else:
       print "please is number worry"

