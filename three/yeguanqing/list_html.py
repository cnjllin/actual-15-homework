#/usr/bin/env python
#coding:utf-8

'''
将nginx日志通过python脚本处理取出TOP10的IP地址和访问次数通过html页面的形式展现出来。
'''

import time

start = time.clock()

# 定义一个空字典
nginxip = {}

# 打开一个文件以readlines方式进行读取所有行
with open('access.txt') as f:
    logs = f.readlines()

# 循环日志文件以空格为分隔符截取位置为0及IP这个元素
for line in logs:
    ip = line.split()[0]

    # 判断ip出现的次数分别以计数的方式写入字典里
    if ip in nginxip:
        nginxip[ip] += 1
    else:
        nginxip[ip] = 1

# 定义一个新列表，使用sorted进行降序排列，使用key排序，截取前十个IP
list = sorted(nginxip.iteritems(),key=lambda x:x[1],reverse=True)[:10]

#定义一个html文件，根据html的编排格式写到html文件，然后将k/v的值分别循环写入已经编排好的html边框里面
f = open('list2.html','a+')
f.write("<html><table whith='400' border='1' cellpadding='1'' cellspacing='1'>")
f.write("<title>reboot_homework</title>")
f.write("<th style='border:solid 1px'>IP Address</th><th style='border:solid 1px'>Num</th>")
# 遍历list列表，enumerate会将该数据对象组合为一个索引序列，同时列出数据和数据下标
for k,v in list:
    f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (k,v))
    print "访问IP和次数：%s --> %s" %(k,v)

f.write("</table></html>")
f.close()
end = time.clock()
print "统计运行时间: %f s" % (end - start)
