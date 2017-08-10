#!/usr/bin/python
#coding:utf-8
ips_list = {}

#读文件
def dict_1():
    with open("/server/scripts/python/access.txt",'r') as f:
     
         #遍历文件，生成key为ip,value为次数的字典
         for n in f.read().split("\n"):
             ips_list[n.split(" - - ")[0]]=ips_list.get(n.split(" - - ")[0],0)+1    
    #排序，并取出前十


def html():
    p = sorted(ips_list.items(),key=lambda d:d[1])
    m = open('top10.html','a+')
    m.write('<html><table style="height:100px;" border="1" cellspacing="0" bordercolor="#000000" cellpadding="8">')
    m.write("<tr><td>IP</td><td>Numbers</td></tr>")
    for n in range(10):
        m.write('<tr><td>%s</td><td>%s</td></tr>'%(p[(-n-1)][0],p[(-n-1)][1]))
    m.write('</table></html>')
    m.close()

dict_1()
html()



