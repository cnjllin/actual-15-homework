#!/usr/bin/python
# --*-- coding:UTF-8 --*--
list1=[1,2,3,4,23,12,34,67,34,23,576,56,99,34]
list2=[3,4,5,7,99,5,56,45,67,34,22,43,23,89]
list1_1=list(set(list1))
list2_2=list(set(list2))
list3=[]
for L in list1_1:
    if L in list2_2:
        list3.append(L)
print "{} or {} is {}".format(list1,list2,list3)
