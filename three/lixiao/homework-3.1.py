#!/usr/bin/python
#coding:utf-8
import time
start = time.clock()
ip_num = []

with open('/python/access.log') as fo:
    data = fo.readlines()
    for n in data:
        ip_num.append(n.split(' ')[0])
    
    num = {}

    for k in ip_num:
        if k in num:
            num[k] += 1
        else:
            num[k] = 1

    num_list = []
    for j in num:
        num_list.append([j,num[j]])
 
    for i in range(len(num_list)):
        for y in range(len(num_list)-1):
            if num_list[y][1]<num_list[y+1][1]:
                num_list[y],num_list[y+1]=num_list[y+1],num_list[y]
#style='border:solrd 1px'

with open("/python/count.html","a+") as f:
    f.write("<html><title>nginx IP count</title>")
    f.write("<table  style=borderColor=#000000 cellSpacing=0 width=300 align=center bgColor=#ffffff border=1><tr><td>IP地址</td> <td>count</td></tr>")
    for z in num_list[:10]:
        #print "%s  %s" %(z[0],z[1])
        f.write("<tr style='border:solrd 1px'><td>%s</td> <td>%s</td></tr>" %(z[0],z[1]))
    f.write("<table></html>")
end = time.clock()
print 'Running time：%s S' %(end-start)

