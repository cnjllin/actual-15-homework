#!/usr/bin/python
#coding:utf-8
#将IP、URL、status按次数排数取前十
#写入一个HTML文件
f = open('log.html','a+')
#HTML文件开头
f.write("<html><table style='border:solid 1px'>")
f.write('<tr><td style="border:solid 1px">IP</td><td style="border:solid 1px">url</td><td style="border:solid 1px">status</td><td tyle="border:solid 1px">出现次数</td>/tr>')
from collections import defaultdict
#打开文件
fo = open('access.txt')
a = []
b = {}
#将需要的元素写入一个列表中
for i in fo.readlines():
        a.append( (i.split(' ')[0],i.split(' ')[6],i.split(' ')[8]))
b = defaultdict(int)
#字典中计数
for j in a:
        b[j] += 1
c = {}
#key和value转换
for k,v in b.items():
	c.setdefault(v,[])
	c[v].append(k)
#取key的最大值，循环10次
count = 0
while count < 10:
	key = max(c.keys())
	for x in c[key]:
		y = list(x)
		#HTML文件表格里的内容
        	f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (y[0],y[1],y[2],key))
	#删除Key
	c.pop(key)
	count = count + 1
#html结尾
f.write("</table></html>")
#关闭文件
f.close()
