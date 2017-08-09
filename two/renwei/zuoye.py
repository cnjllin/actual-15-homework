#!/usr/bin/env python
#encoding:utf-8
#定义文件路径
file_path = "/root/access.txt"
#获取排行数
top = int(raw_input('请输入您需要统计排行数:'))
print "--------排名前{}IP的信息---------".format(top) 
#打开文件读取，空格分隔遍历到空字典，切分IP列，通过det方法计数，默认0，然后遍历字典，以value 为key排行，倒叙
with open(file_path) as f:
    dic = {}
    for line in f:
        arr = line.split(' ')
        ip = arr[0]
        dic[(ip)] = dic.get((ip),0) + 1
    for i in sorted(dic.items(),key = lambda x:x[-1],reverse=True)[:top]:
         print "IP: {}  次数:{}".format(i[0],i[-1])

