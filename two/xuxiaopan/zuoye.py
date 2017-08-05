#!/usr/bin/env python
#-*-coding:utf-8 _*_
def nginxlog(nginxFile):
    iplog = { }
    with open(nginxFile) as f:
        for line in f:
            ip = line.split(" ",1)[0]
            if 6<=len(ip) <= 15:
                iplog[ip] = iplog.get(ip,0) + 1
    return iplog
nginxIp = { }
nginxIpBySort = { }
nginxIp = nginxlog("./access.txt")
nginxIpBySort = sorted(nginxIp.iteritems(),key = lambda d:d[1] ,reverse = True)
for i in nginxIpBySort[0:10] :
    print i

