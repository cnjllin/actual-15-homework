#!/usr/bin/python
# --*-- coding:UTF-8 --*--
my_list=[1,2,4,15,9,12,111,23,144]
time=0
my_list1=[]
while time < len(my_list)+time:
    max=0
    for n in my_list:
        if n > max :
            max=n
    my_list.remove(max)
    my_list1.insert(len(my_list1),max)
    time+=1
my_list1.reverse()
print my_list1
        
