#!/bin/env python
# -*- encoding:utf-8 -*-

file_path = '/root/access.txt'
ips = {}
with open(file_path,"r") as f :
    for line in f :
        ip = line.split()[0]
        ips[ip] = ips.get(ip,0) + 1

#ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)

#插入排序法排序
ip_tops = []
num = 0
for ip,count in ips.items() :
    if len(ip_tops) == 0 :
        ip_tops.append([ip,count])
    else :
        n = len(ip_tops) / 2
        if ip_tops[n][1] < count :
            start = 0
            end = n
        else :
            start = n + 1
            end =  len(ip_tops)
        for i in range(start,end) :
            num += 1
            if ip_tops[i][1] < count :
                ip_tops.insert(i,[ip,count])
                break
        else :
            num += 1
            #ip_tops.append([ip,count])
            ip_tops.insert(end,[ip,count])

        if len(ip_tops) > 10 :
            ip_tops = ip_tops[:10]

print "排序循环执行了%s次" % (num)




print "============= IP TOP10 信息 ============="
for ip in ip_tops :
    print "IP: %-20s 访问次数: %8s" % ( ip[0] , str(ip[1])+"次" )
