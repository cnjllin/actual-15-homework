#!/usr/bin/env python
#_*_coding:utf-8_*_
# date 2017.8.2
# mail:651002081@qq.com
def topip():
    my_dict={}
    my_list_sort=[]
    with open('access.txt') as f:
        for line in f:
            tem=line.split(' ')
            tup=tem[0]
            my_dict[tup]=my_dict.get(tup,0)+1
    my_list_sort=my_dict.items()
    for i in range(len(my_list_sort)-1):
        for j in range(len(my_list_sort)-1-i):
            if my_list_sort[j][1]>my_list_sort[j+1][1]:
                my_list_sort[j],my_list_sort[j+1]=my_list_sort[j+1],my_list_sort[j]
    return my_list_sort

def my_html(my_list_sort): 
    my_html='<table border=1>'
    my_html+='<tr><td>num</td><td>ip</td><td>count</td></tr>'
    for i in range(10):
        tmm=my_list_sort.pop()
        my_html+='<tr><td>%s</td><td>%s</td><td>%s<td></tr>'%((i+1),tmm[0],tmm[1])
    my_html+='</table>'
    return my_html

def my_index(my_html):
    with open('index.html','w') as f:
        f.write(my_html)
    return 'okkkkkk'

def my():
   my_list_sort1=topip()
   my_html1=my_html(my_list_sort1)
   my_index(my_html1)
   return 'ok'

my() 
