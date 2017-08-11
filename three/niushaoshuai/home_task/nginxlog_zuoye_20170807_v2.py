#!/usr/bin/python
# --*-- coding:UTF-8 --*--

#生成ip,geturl,status为元素的列表。
my_list=list()
my_str=str()
f=open('/home/niushaoshuai/access.txt','r')
for line in f.readlines():
    my_str=line.split(' ')[0]+":"+line.split(' ')[6]+":"+line.split(' ')[8]
    my_list.append(my_str)
f.close()

#生成{ip:times}为元素的字典。
my_key=dict()
for ips in my_list:
    my_key[ips]=my_key.get(ips,0)+1

#对{ips:times}字典翻转
od=dict()
for k,v in my_key.items():
    od.setdefault(v,[])
    od[v].append(k)

#对字典进行排序，取出前十。
f=open('tongji.html','a+')
f.write("<html><head><title>访问统计</title></head><table  border=1 >")
f.write("<tr><th>Times</th><th>IP</th><th>Url</th><th>Status</th></tr>")
for t in range(10):
    m_key=max(od.keys())
    for pk in od.pop(m_key):
         i=pk.split(':')[0]
         u=pk.split(':')[1]
         p=pk.split(':')[2]
         f.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (m_key,i,u,p))
f.write("</table></html>")
f.close()

