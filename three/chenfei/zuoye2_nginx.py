#!/usr/bin/python
#coding:utf-8
def nginxIpCounter(nginxFile):
    ipCounter = { }
    with open(nginxFile) as f:
        for line in f:
            ip = line.split(" ",1)[0]
            if 6<=len(ip) <= 15:
                ipCounter[ip] = ipCounter.get(ip,0) + 1
    return ipCounter
nginxIp = { }
nginxIpBySort = { }
nginxIp = nginxIpCounter("/root/access.txt")
nginxIpBySort = sorted(nginxIp.iteritems(),key = lambda d:d[1] ,reverse = True)[:10]
for i,j in nginxIpBySort:
    print "%s => %d"%(i,j)

with open('/root/actual-15-homework/three/chenfei/iptop10.html','w') as f:
    f.write('<html>\n\n<title>\nNgnix日志IP前10\n</title>\n<h><style="color:red"> IP </h>\n<body>\n\n<table border=1 >\n<table style border=1 >\n')
    f.write('<tr><th>IP</th><th>数量</th></tr>')
    for i in nginxIpBySort:
        f.write('<tr><td>%s</td><td>%d</td></tr>\n' % (i[0],i[1]))
    f.write('</table>\n</body>\n</html>\n')
print "" 
