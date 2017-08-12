#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File Name: analyze_logs.py
# Author: luofeng
# Mail: 18210085737@139.com 
# Blog: https://www.liyanlan.com 

import time
start = time.clock()
count = {}

# 遍历文件，把文件内容存储到字典中，并统计相同元素出现的次数
def get_cip(filename):
	with open(filename) as f:
		for line in f.readlines():
			cip = line.strip().split(' ')[0]
			count[cip] = count.get(cip,0) + 1

	# 字典反转，即把key/value ==> value/key的形式
	res = {}
	for k,v in count.items():
		res.setdefault(v,[])
		res[v].append(k)

	# 对统计出的元素进行排序，获取前10元素，并通过html表格的形式展示.
	counts = 0
	with open('/home/work/www.liyanlan.com/program/top_10.html','w+') as f:
		f.write("<html><title>top ip</title>\n")
		f.write("<table width='400' border='1' cellspacing='1' cellpadding='1' style='text-align:center;margin:0 auto'>\n")
		f.write("<tr><td>CIP</td><td>TOTAL</td></tr>\n")
		# 字典元素反转后，相同元素出现的次数即为res.keys(). 通过max()方法获取最大值，使用while循环遍历10次, 并结合pop()方法把前一次取出来的值从字典中删除掉. 
		while counts < 10:
			key = max(res.keys())
			for word in res[key]:
				f.write("<tr><td>{0}</td><td>{1}</td></tr>\n".format(word,key))
				res.pop(key)
				counts = counts + 1
		f.write("</table></html>")

	end = time.clock()
	print 'excute time is %0.4f' %(end-start)
get_cip('access.txt')
