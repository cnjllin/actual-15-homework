#!/usr/bin/python
#coding:utf-8

'''
   需求：打印出nginx访问日志中访问次数前十的ip以及对应的访问次数
   思路分析：
	    1，打开log并提取log中所有的Ip到列表
	    2, 对列表中所有的IP出现的次数进行计数，直接调用collections.Counter函数
	    3，打印出排序后的列表的前十，至此完成需求	       
'''
# 从Collections集合模块中引入集合类Counter
import collections

# 打开并读取日志文件   
with open('/root/gaofan/access.txt') as f:
    data=f.readlines() 

# 提取log中所有ip到列表
access_ip=[]
for line in data:
    access_ip.append(line.split(" ")[0])

# Counter()可以打印出list中每个元素出现的次数,Counter().most_common(10)可以打印出list中出现次数前十的元素
times_top_ten=collections.Counter(access_ip).most_common(10)
# print times_top_ten

# 格式化输出结果
for i in times_top_ten:
    print '''The \033[0;31;40m%d\033[0mst of visit is:\033[0;31;40m%s\033[0m ,IP_Address:\
\033[0;31;40m%s\033[0m''' % (times_top_ten.index(i)+1,i[1],i[0])
    print "\033[0;32;40m*\033[0m" *52 
