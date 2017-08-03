#!/usr/bin/python
# -*- coding:utf-8 -*-
# description:Analyse a nginx access log for the top 10 ip addresses by traffic
# log_example: 1477659822.520 930938 123.42.130.36 TCP_MISS/206 66277 GET http://mvvideo10.meitudata.com/57a6d9da14310908.mp4?avthumb/mp4/s/140x94/an/1  - DIRECT/123.218.34.203 video/mp4 "http://admin.meitumv.com:8080/medias?filter_type=uid&search_keyword=1071373222" "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0" -

import time
start = time.time()
# create a dictionary named dict to store the key:ip and the value:traffic.
dict = {}

# opening a file with the mode 'rU' will open a file for reading in universal newline mode
# traverse the log file to ouput traffic of each ip
for index,line in enumerate(open('./test.file','rU')):
    ip = line.split()[2]
    traffic = int(line.split()[4])
    if ip in dict:
        dict[ip]+=traffic
    else:
        dict[ip]=traffic

# sort by the access time of ip
sort_dict = sorted(dict.items(), key=lambda l:l[1],reverse=True)[:10]
# print top 10 access ip by access times
for item in sort_dict:
    print("IP:%-15s  Traffic(B): %s"%(item[0],item[1]))
end = time.time()
interval = end -start
print "Execute time::%0.3fs" % interval
