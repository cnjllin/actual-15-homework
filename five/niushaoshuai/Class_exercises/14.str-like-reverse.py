#!/usr/bin/python
# --*-- coding=UTF-8 --*--
my_str="reboot"
my_list=[]
for n in my_str:
    my_list.insert(0,n)
    
my_str1="".join(my_list)
print "{} after reverse is {}".format(my_str,my_str1)
