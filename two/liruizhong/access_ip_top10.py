#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
作业：    打印出nginx访问日志中，访问次数前十的IP以及对应的访问次数
思路分析：  1、打开log文件，并按行读取
          2、对读取的每一行进行分割，切片，获取到访问IP
          3、将获取的IP作为字典的key,存入到字典中
          4、出现重复的IP，则将此IP的value进行加1操作
          5、将这样的字典key,value 以value进行排序
          6、取出后十对，即是访问次数前十的IP
'''

import time

d = {}
start = time.clock()
# 打开并读取日志文件
with open('access.txt','r') as f:
    for i in f:
        # 获取每行的访问IP
        ip = i.split(' ')[0]
        # 进行判断，如果访问IP没有在字典的key中，则对字典进行添加
        if ip not in d.keys():
            d.update({ip:1})
        # 如果已经在字典的key中，则对相应的key对应的value进行加1
        else:
            count = d[ip] + 1
            d[ip] = count
    # 对字典以value 进行排序，生成一个列表
    list1 = sorted(d.items(),key=lambda item:item[1])
    # 遍历列表，取出访问次数前十的IP及次数
    for i in range(1,11):
        access_ip = list1[-i][0]
        access_count = list1[-i][1]
        print "\033[32m%-15s\033[0m was visited \033[33m%s\033[0m times" % (access_ip,access_count)
    print list1

end = time.clock()
# 打印出程序运行的时间
print("The function run time is : \033[32m%.03f\033[0m seconds" %(end-start))
