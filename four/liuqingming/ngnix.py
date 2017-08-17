#!/bin/env python
# -*- encoding:utf-8 -*-

#import day2_homewk4
#print day2_homewk4.ip_tops

from day2_homewk4 import ip_tops #导入模块中的列表
print ip_tops

with open('templates/IP_top10.html','w') as f:
    f.write('<html>\n<head>\n<meta charset="utf-8">\n<title>\nNgnix日志IP前10\n</title>\n</head>\n<h><style="color:red"> IP </h>\n<body>\n\n<table border=1 >\n<table style border=1 >\n')
    f.write('<tr><th>IP</th><th>URL</th><th>STATUS</th><th>数量</th></tr>')
    for i in ip_tops:
        f.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%d</td></tr>\n' % (i[0][0],i[0][1],i[0][2],i[1]))
    f.write('</table>\n</body>\n</html>\n')
print ""
