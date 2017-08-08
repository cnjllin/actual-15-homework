#!/usr/bin/python
# --*-- coding:UTF-8 --*--
str="who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forg    otten past you can’t go on well in lifeuntil you let go of your past failures and heartaches"
my_list=str.split(' ')
my_dict=dict()
for v in my_list:
    if v in my_dict:
        my_dict[v]+=1
    else:
        my_dict[v]=1
print my_dict
