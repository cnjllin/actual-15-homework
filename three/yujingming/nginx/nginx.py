#usr/bin/env python
#coding: utf-8
'''
#获取排行数
top = int(raw_input('请输入统计排行数:'))
print "--------top{}---------".format(top) 
#打开文件读取，空格分隔遍历到空字典，切分IP列，通过get方法计数，默认0，
#然后遍历字典，以value 为key排行，倒序
'''

with open('access.txt') as f:
    dic = {}
    for line in f:
        arr = line.split(' ')
        ip = arr[0]
        dic[(ip)] = dic.get((ip),0) + 1

    def getOrderKey(x):
    	return x[1]
    top10 = sorted(dic.items(),key =getOrderKey,reverse=True)[:10]	
    for i in top10:
    #for i in sorted(dic.items(),key = lambda x:x[-1],reverse=True)[:top]:
        print "IP: {}  Count:{}".format(i[0],i[-1])

with open('nginx.html','w') as f:
    f.write('<html>\n\n<title>\n日志IP前10\n</title>\n<h><style="color:red">TOP 10 IP List</h>\n<body>\n\n<table border=1 >\n<table style border=1 >\n')
    f.write('<tr><th>IP</th><th>No </th></tr>')
    for i in top10:
        f.write('<tr><td>%s</td><td>%d</td></tr>\n' % (i[0],i[1]))
    f.write('</table>\n</body>\n</html>\n')
print "Top10 IP list has insert to the html,please check"
