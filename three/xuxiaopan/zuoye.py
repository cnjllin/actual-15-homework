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
f = open('table.html', 'a+')
table= '<table style="height:100px;" border="5" cellspacing="0" bordercolor="#000000" cellpadding="8"> <td>数量</td><td>ip</td>'
for i in nginxIpBySort[0:10] :
    table += '<tr><td>%s</td><td>%s</td></tr>\n' % (i[0], i[1])
end_table = '</table>'
f.write('%s %s'   % (table,end_table))
f.close


