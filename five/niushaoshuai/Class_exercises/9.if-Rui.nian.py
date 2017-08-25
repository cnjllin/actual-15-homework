#/usr/bin/python
# --*-- coding:UTF-8 --*--
while 1:
    Year=int(raw_input("please input a year: "))
    if Year%100==0 and Year%400==0 :
        break
    elif Year%100 != 0 and Year%4==0 :
        break
    else:
        print "{} is not Rui.nian".format(Year)
        continue
