#!/usr/bin/python
#coding:utf-8
ip = []
ip_dict = {}
with open('access.log.bak') as f:    #打开日志文件
	file = f.readlines()     		#readlines()日志变为列表
	for i in file:				#遍历列表,以str字符串输出
		client_ip = i.split(' ')	#split()函数用' '空格分隔,将字符串转换位列表
		ip.append(client_ip[0])		#把下标0的数据即ip地址，追加到ip空列表
for x in ip:
	ip_dict[x] = ip_dict.get(x,0)+1		#.get()函数，ip_dict字典里没有这个ip，就赋值为0，有则加1

#print ip_dict
ip_count = []
for i in ip_dict.items():			#将字典转换为套着元组的列表
	ip_count.append(i)
#print ip_count
#用冒泡排序，排出次数大小。
for i in range(len(ip_count)):
	for i in range(len(ip_count)-1):
		if ip_count[i][1] > ip_count[i+1][1]:
			ip_count[i],ip_count[i+1] = ip_count[i+1],ip_count[i]
#print ip_count
ip_count.reverse()
#print ip_count
for x in range(10):
	print "ip", ip_count[x][0] ,"is appear" ,ip_count[x][1] ,"次"
	
