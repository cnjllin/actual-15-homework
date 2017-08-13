#!/usr/bin/env python
#encoding:utf-8
#changhuawei 513314416@qq.com
#201708011439
def logtop(file_path,top=10):
#print "--------top{}---------".format(top) 
    #打开文件读取，空格分隔遍历到空字典，切分IP列，通过det方法计数，默认0，然后遍历字典，
    #以value 为key排行，倒叙
	with open(file_path) as f:
	    dic = {}
	    logtopn = []
	    for line in f:
	        arr = line.split(' ')
	        ip = arr[0]
	        dic[(ip)] = dic.get((ip),0) + 1
	    for i in sorted(dic.items(),key = lambda x:x[1],reverse=True)[:top]:
	        add = "{} {}".format(i[0],i[1])
                # print add
                logtopn.append(add)
        return logtopn
file_path = "/root/15/02/access.txt"           
# print logtop(file_path,top=10)
logtop_list = logtop(file_path,top=10)

data = ''
tables = '<table style="height: 100px;" border="5" cellspacing="0" bordercolor="	#000000" cellpadding="8">'
tbody = '<tr>\n<td>IP</td>\n<td>counts</td>\n</tr>'
for line in logtop_list:
	data += "<tr>\n <td>{}</td>\n<td>{}</td>\n</tr>\n".format(line.split()[0],line.split()[1])
html = tables + tbody + data +'\n</table>'
# print html
with open('topn.html','wb') as f:
	f.write(html)
# logtop(file_path,top=10)