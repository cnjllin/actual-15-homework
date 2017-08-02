#!/usr/bin/python
#coding:utf-8

'''
   需求：打印出nginx访问日志中访问次数前十的ip以及对应的访问次数
   思路分析：
	    1，打开log并提取log中所有的Ip到列表
	    2, 对列表中所有的IP出现的次数进行计数，用字典关联ip和它访问的次数，比如a={'x.x.x.x':'2333'}
	    3，打印出前十，则需要排序，这里需要考虑两点
 	        a,字典是无序的，怎么排序？
		b,如果有不同的ip访问次数相同，怎么办？
	        c,用什么方法排序？
		解决办法：转换成列表，用冒泡法排序
	    4，打印出排序后的列表的前十，至此完成需求	       
'''

# 打开并读取日志文件   
with open('access.txt') as f:
    data=f.readlines()

# 提取log中所有ip到列表
access_ip=[]
for line in data:
    access_ip.append(line.split(" ")[0])

# 对所有出现的ip进行计数，用字典关联ip和其访问次数
access_times={}
for ip in list(set(access_ip)):
    access_times[ip]=access_ip.count(ip)
'''print access_times'''

# 此处将字典转换为列表进行排序
access_times_list=access_times.items()

# 开始按照访问次数冒泡排序
l=len(access_times_list)-1
while l > 0:
    for i in range(l):
	if access_times_list[i][1] > access_times_list[i+1][1]:
	    access_times_list[i],access_times_list[i+1]=access_times_list[i+1],access_times_list[i]
    l=l-1

# 取出排序后列表的前十
times_top_ten= access_times_list[-10:][::-1]
'''print times_top_ten'''

# 打印出访问次数前十 
for i in times_top_ten:
    print '''The \033[0;31;40m%d\033[0mst of visit is:\033[0;31;40m%s\033[0m ,IP_Address:\
\033[0;31;40m%s\033[0m''' % (times_top_ten.index(i)+1,i[1],i[0])
    print "\033[0;32;40m*\033[0m" *52
