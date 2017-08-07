#!/usr/bin/python
# -*- coding:utf-8 -*-
# description:Analyse a nginx access log for the top 10 ip addresses and display the result in the form of html.

import time
import re
start = time.time()

# create a dictionary named dict to store the key:ip and the value:access times.
dict = {}

# opening a file with the mode 'rU' will open a file for reading in universal newline mode
# traverse the log file to ouput index and content
for index,line in enumerate(open('./access.txt','rU')):
    ip = line.split(' ')[0]
    if ip in dict:
        dict[ip]+=1
    else:
        dict[ip]=1

# sort by the access time of ip
sort_dict = sorted(dict.items(), key=lambda l:l[1],reverse=True)[:30]
# output top 10 access ip to top_10_ip.html
f = open("top_10_ip.html",'w+')
# define the title and table style of the web page
f.writelines('<html>\n<title>\ntop_10_access_ip\n</title>\n<body>\n<table style="height:100px;" border="1" cellspacing="0" bordercolor="#000000" cellpadding="8">\n')
f.write('<tr><th>IP</th><th>access times</th></tr>\n')
# print top 10 access ip by access times
for item in sort_dict:
    f.write('<tr><td>%s</td><td>%s</td></tr>' %(item[0],item[1]))
    print("IP:%-15s  Access Times: %s"%(item[0],item[1]))
# close file and add some element to the web page
f.writelines('</table>\n</body>\n</html>\n')
f.close()
end = time.time()
interval = end -start
print "Execute time::%0.3fs" % interval

