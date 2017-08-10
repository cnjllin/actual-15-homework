#/usr/bin/python
#coding=utf-8

import time
start = time.clock()

# 定义一个空列表存储获取到的IP
ip_list = []
# 定义一个空dict获取IP:对应相同次数
temp_dict = {}
with open('/home/yang.liu/python/day2/access.txt','a+') as f:
    for line in f:
        #print line
        ip_list.append(line.split()[0])
    #print ip_list
    for ip in ip_list:
    	if ip in temp_dict:
    	    temp_dict[ip]+=1
    	else:
    		temp_dict[ip]=1
#修改 定义一个v:k，反转k:v，并将相同访问的次数IP生成一个list
reverse_res = {}
for  k in temp_dict:
    #print k
    if temp_dict[k] in reverse_res:
        reverse_res[temp_dict[k]].append(k)
    else:
        reverse_res[temp_dict[k]]= [k]
#print reverse_res

#汇总访问前10成html表单
f = open('nginx.html','a+')
f.write('<table style="height: 100px" border="1" cellspacing="3" bordercolor="#000000">')
f.write('<tr><td>IP</td><td>访问次数</td></tr>')

#将所有的IP访问次数重新生成一个list,排序获取前10
key_list = []
for i in reverse_res:
    key_list.append(i)
key_list.sort()
#print key_list

count = 0
while count<10:
    count += 1
    key = key_list.pop()
    #print val
    for j in reverse_res[key]:
        f.write('<tr><td>%s</td><td>%s</td></tr>'%(j,key))
        print 'IP-->%s-->访问%s次'%(j,key)

f.write("</table>")
f.close()

end = time.clock()
print "程序执行用时: %f s" % (end - start)



