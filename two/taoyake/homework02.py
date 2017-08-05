#coding=utf8
from collections import Counter
ip_list=[ ]
with open('access.log','r') as f_log:
    for i in f_log.readlines():
        ip_list.append(i.split(" ")[0])
ip_list = sorted(dict(Counter(ip_list)).items(), key=lambda x: x[1], reverse=True)[0:10]
for i in ip_list:
    print i[0],'访问次数为：%s' %i[1]
