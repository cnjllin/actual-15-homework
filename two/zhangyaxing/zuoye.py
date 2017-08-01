#!/usr/bin/env python
# encoding: utf-8

# 建立空列表
lines = []
# 读取日志文件
with open('/Users/zhangyaxing/Desktop/access.txt','r+') as f:
    # 遍历日志每一行
    for line in f.readlines():
        # 每一行转为字符串
        line_str = str(line)
        # 每一行处理之后存为line_list
        line_list = line_str.split(' ')
        # 将每一行处理后的结果取ip地址存入lines
        lines.append(line_list[0])

# 建立空数组存放ip的次数
ip_count = {}
# 遍历lines数组
for ip in set(lines):
    # 将IP的次数放入字典中
    ip_count[lines.count(ip)]=ip
# 取出字典中ip出现次数的前十
for i in reversed(sorted(ip_count.keys())[-10:]):
    # 打印字典中ip出现次数的前十
    print 'ip%s出现了%d次'%(ip_count[i],i)
