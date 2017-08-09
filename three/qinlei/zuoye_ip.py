# -*- coding: utf-8 -*-

op = "C:\Users\Administrator\Documents\Tencent Files\865521104\FileRecv\ccess.txt"

with open(op, "r") as f:

    iplist = [x.split(" ")[0] for x in f ] #  取IP

    a = ( (i,iplist.count(i)) for i in {x for x in iplist} ) #去重并统计重复数量

    c = sorted(a, key=lambda x:x[1], reverse=True)[:10] #排序取前10个

with open('count.html',"a+") as fi:
    tables_start = "<table border='1'>"
    d = "<tr><td></td><td></td></tr>\n"
    tables_end = "</table>"
    for i in c:
        d += "<tr><td>%s</td><td>%s</td></tr>\n" % (i[0],i[1])

    fi.write("%s%s%s"%(tables_start,d,tables_end))
