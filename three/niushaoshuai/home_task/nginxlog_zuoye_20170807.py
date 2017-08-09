#!/usr/bin/python
# --*-- coding:UTF-8 --*--

#生成ip为元素的列表。
my_list=list()
f=open('/home/niushaoshuai/access.txt','r')
for line in f.readlines():
    my_list.append(line.split(' ')[0])
f.close()

#生成{ip:times}为元素的字典。
my_key=dict()
for ip in my_list:
    my_key[ip]=my_key.get(ip,0)+1
    
#对{ip:times}字典翻转
od=dict()
for k,v in my_key.items():
    od.setdefault(v,[])
    od[v].append(k)

#对字典进行排序，取出前十。
f=open('tongji.html','a+')
f.write("<html><table  border=1 >")
f.write("<tr><th>次数</th><th>单词</th></tr>")
pd=dict()
for t in range(10):
    m_key=max(od.keys())
    pd[m_key]=od[m_key]
    for pk in od.pop(m_key):
        f.write('<tr><td>%s</td><td>%s</td></tr>' % (m_key,pk))
f.write("</table></html>")
f.close()
