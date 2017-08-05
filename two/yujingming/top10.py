#usr/bin/python
#coding=utf-8

#获取排行数
top = int(raw_input('请输入统计排行数:'))
print "--------top{}---------".format(top) 
#打开文件读取，空格分隔遍历到空字典，切分IP列，通过get方法计数，默认0，
#然后遍历字典，以value 为key排行，倒序
with open('access.txt') as f:
    dic = {}
    for line in f:
        arr = line.split(' ')
        ip = arr[0]
        dic[(ip)] = dic.get((ip),0) + 1

    def getOrderKey(x):
    	return x[1]
    for i in sorted(dic.items(),key =getOrderKey,reverse=True)[:top]:
    #for i in sorted(dic.items(),key = lambda x:x[-1],reverse=True)[:top]:
        print "IP: {}  Count:{}".format(i[0],i[-1])


'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#1st version(Not work):
iplist= []
with open('access.txt') as f:
	for line in f:
		ip =line.split(' ')
		iplist.append(ip[0])
#		print iplist.count(ip[0])   

dic= {}
for l in iplist:
	dic[1]=dic.get(1,0) + 1
for k,v in sorted(dic.items(),key=lambda x:x[1],reverse=True)[:10]:

	print "IP: {},Count:{}".format(k,v)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''