#/usr/bin/python
#coding=utf-8

#定义一个空列表存储获取到的IP
ip_list = []
#定义一个空dict获取IP:对应相同次数
temp_dict = {}
with open('access.txt','a+') as f:
    for line in f:
        #print line
        ip_list.append(line.split()[0])
    #print ip_list
    for ip in ip_list:
    	if ip in temp_dict:
    	    temp_dict[ip]+=1
    	else:
    		temp_dict[ip]=1
 	#print temp_dict
#定义temp_list,因为dict没有顺序，所以将dict转成list对出现次数进行排序
temp_list=[]
for i in temp_dict:
	#print i
	#print temp_dict[i]
	temp_list.append([i,temp_dict[i]])
#print temp_list
#冒泡排序，循环temp_list中数据，如果第0个索引值小于第1个索引值，交换位置，依次取出最大值
for k in range(10):
	for j in range(len(temp_list)-1):
		if temp_list[j][1]>temp_list[j+1][1]:
			temp_list[j],temp_list[j+1]=temp_list[j+1],temp_list[j]
#print temp_list[-10:] 倒着取最后10个
for r in temp_list[-10:]:
	print 'IP:%s,访问次数是:%s'%(r[0],r[1]) 
