#!/usr/bin/python
#coding:utf-8

# 需求：打印access.log中ip出现频率top 10

ip_list = []
count = 0
my_dict = {}

#打开文件
with open("access.log") as f:
    data = f.readlines()
#提取其中的IP地址
for x in  data:
    ip_list.append(x.split(' ')[0])
#将IP地址和重读次数做成字典
for ip in ip_list:
    if ip not in my_dict:
        count = 1
        my_dict[ip] = count
    else:
        my_dict[ip] +=1
#冒泡排序将IP重复次数排序
my_list=my_dict.items()
for j in range(len(my_list)):
    for i in range(len(my_list)-1):
        if my_list[i][1] > my_list[i+1][1]:
            my_list[i],my_list[i+1] = my_list[i+1],my_list[i]

my_list_sort = my_list[-10:][::-1]
#格式化打印结果,生成HTML表格
f = open('tongji_1.html', 'a+')
f.write("<html><table style='border:solid 1px' bgcolor= #E8FFF5 >")
f.write("<th style='color:red' style='border:solid 5px'>IP</th><th style='color:red' style='border:solid 5px'>重复次数</th>")
for a in my_list_sort:
    f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' %(a[0],a[1]))
f.write("</table></html>")
f.close()
















