#!/usr/bin/env python
#_*_coding:utf-8_*_
# date 2017.8.2
# mail:651002081@qq.com
# 取日志文件前10的ip，和对应次数

# 导入模块
import time
# 开始时间
a=time.time()
# 定义一个空字典
my_dict={}
# 定义一个空列表
my_list_sort=[]

# 打开文件
with open('access.txt') as f:
    # 遍历文件每一行
    for line in f:
        # 把每一行转为一个临时列表
        tem=line.split(' ')
        # 把临时列表的第0个元素在放入一个临时列表里
        tup=tem[0]
        # 把列表里的ip当做key，出现次数为value放入到空字典里
        my_dict[tup]=my_dict.get(tup,0)+1

# 对字典冒泡排序
my_list_sort=my_dict.items()
for i in range(len(my_list_sort)-1):
    for j in range(len(my_list_sort)-1-i):
        if my_list_sort[j][1]>my_list_sort[j+1][1]:
            my_list_sort[j],my_list_sort[j+1]=my_list_sort[j+1],my_list_sort[j]

# 打印输出
for i in range(10):
    tmm=my_list_sort.pop()
    print '访问次数第%s的ip:%s,访问次数:%s'%((i+1),tmm[0],tmm[1])

# 结束时间
b=time.time()
print'使用时间:%s'%(b-a)
