#!/usr/bin/env python
# encoding: utf-8

f_list=[]
with open('access.txt','r') as f:
    for line in f.readlines():
        f_list.append(line.split(' ')[0])

f_dict={}
for ip in f_list:
    f_dict[ip]=f_dict.get(ip,0)+1


new_dict={}
for k,v in f_dict.items():
    new_dict.setdefault(v,[])
    new_dict[v].append(k)


h = open('acount.html','a+')
h.write('<table style="border:1px solid black;cellspacing=0">')
h.write('<tr style="border:1px solid black"><th>ip</th><th>count</th></tr>')
h_dict={}
for i in range(10):
    k = max(new_dict.keys())
    h_dict[k] = new_dict[k]
    for v in new_dict.pop(k):
        h.write('<tr style="border:1px solid black"><td style="border:1px solid black">%s</td><td style="border:1px solid black">%s</td></tr>'%(k,v))
h.write('</table>')
h.close()






