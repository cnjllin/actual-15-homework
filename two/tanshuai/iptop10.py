#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/7/31日21点39分

import time
start = time.clock()

# 源日志文件
log_files = 'access.txt'
# 定义一个字典，用于存放统计后的数据
rt_dict = {}
# 以读取方式打开文件
log_files = open(log_files, 'r')

# 读取文件：
while True:     # 使用while True来循环读取文件
    # 每次循环读取一行文件内容
    line = log_files.readline()
    # 判断读取信息为空则跳出循环(严格的access日志一般不会有空行哈,所以这里直接了断break)
    if not line:
        break
    # 获取ip信息
    line_info = line.split() # 默认使用空格分割
    ip = line_info[0]
    # 这里如何判断ip是否在存在dict中呢？使用not in dict
    if ip not in rt_dict:
        # 如果没有在dict里，就算这个IP出现了一次，并存入dict
        rt_dict[ip] = 1
    else:
        # 如果dict里存在这个ip，则把这个ip出现的次数加一次
        rt_dict[ip] += 1
# 循环统计完成后，关闭文件
log_files.close()
# print rt_dict

# 2、转换成list，方便排序
rt_list = rt_dict.items()
# print rt_list

# 3、排序出topn访问信息
# 方法一：【使用冒泡排序】
# 指定循环多少次（可以理解为指定取多少个最大值）
print "=========IP TOP10 信息========="
for j in range(1, 11):
    # 这里for循环整个列表，每循环一次找出列表max值
    for i in range(0, len(rt_list) - 1):
        if rt_list[i][1] > rt_list[i + 1][1]:
            rt_list[i], rt_list[i + 1] = rt_list[i + 1], rt_list[i]
    # 格式化输出结果
    print "IP:[%-15s] 出现了[%s]次."% (rt_list[-j][0],rt_list[-j][1])
# print rt_list[-1:-11:-1]

# 方法二：【使用key,value反转,使用sorted函数排序】
# print "=========IP TOP10 信息========="
# rt_list = []
# for k,v,in rt_dict.items():
#     rt_list.append((v,k))
# for i in range(1,11):
#     ip = sorted(rt_list)[-i]
#     print "IP:[%-15s] 出现了[%s]次."% (ip[1],ip[0])

end = time.clock()
print "程序执行用时: %f s" % (end - start)

'''
本次作业知识点总结：
1. 循环读取文件 while True
2. dict 存储数据
3. split() 默认空格分割
4. for 配合range指定循环次数
5. if 判断,交换元素位置
'''