# -*- coding: utf-8 -*-
#作业要求:找出日志文件里的前十的IP,并进行排序



f = open("E:\\actual-15-homework\\two\luochuan\\access.log","r")   #读文件
lines = f.readlines()
list_ip =[]
dict = {}
n = 0

for i in lines:
    ip = i.split(' ')[0]    #获取IP,并生成IP的队列
    list_ip.append(ip)

for i in list_ip:        #通过LIST来生成字典,并统计IP出现次数
    if i in list_ip:
        n += 1
        dict[i] = n
    else:
        dict[i]=1

dic = sorted(dict.items(), key=lambda d:d[1], reverse = True)   #将生成的字典转变为LIST,并通过VALUE来排序
for i in range(0,10):
    print '%s ----> %s'%(dic[i][0],dic[i][1])     #打印出前十的IP以及出现次数


