#!/usr/bin/python
# --*-- coding:UTF-8 --*--
str='i love huahua hello world i am fine huahua i am in the world'
my_list=str.split(' ')
my_dict=dict()
for v in my_list:
    if v in my_dict:
        my_dict[v]+=1
    else:
        my_dict[v]=1
print sorted(my_dict.items(),key=lambda k:k[1] ,reverse=True)[:5]
