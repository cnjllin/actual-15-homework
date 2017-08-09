# *************************************************************************
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File Name: analyze_logs.py
# Author: luofeng
# Mail: 18210085737@139.com 
# Blog: https://www.liyanlan.com 
# ************************************************************************

count = {}

with open('access.txt') as f:
	for line in f.readlines():
		client_ip = line.strip().split(' ')[0]
		if client_ip in count:
			count[client_ip]+=1
		else:
			count[client_ip]=1

top_ip = sorted(count.items(),key=lambda item:item[1],reverse=True)[:10]

for x in top_ip:
	print "Client IP: %s, Num of Request is %s" %(x[0], x[1])
