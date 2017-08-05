# -*- coding: utf-8 -*-
'''
作业:找出日志文件内出现频率前10的IP，并且显示该IP一共出现多少次。
思路：
1.将日志文件按行读取成列表
2.使用split分割出IP，并将所有IP添加到另一个列表中
3.将IP地址和该地址出现的次数添加到字典，k是地址，v是次数，不添加重复的IP，并要准确保留IP和次数的对应关系
4.将字典里的k和v（也就是IP和次数）分别转换成2个列表，要确保每一对k和v在各自的列表里序号相同
5.找出v列表（次数）中的最大值，并根据该元素的序号找出k列表中对应的元素，打印信息
6.分别在k和v列表中删除上一步找出元素
7.将第5步和第6步循环10次，即得出出现频率TOP10的IP地址和次数
'''
import time    # 前2行和最后2行代码均用于测试程序运行时间
start = time.clock()
# 创建后续代码需要的列表和字典
ip = []
count_list = []
ip_list = []
# 将日志文件按行读取，并组成列表
with open('F:\\access.txt') as file:
    log_list = file.readlines()
    # 分割出IP，并将所有IP添加到l_list列表
    for i in log_list:
        l_list = i.split()
        ip.append(l_list[0])
    # 将IP地址和出现次数添加到字典中，不添加重复的IP
    for i in ip:
        if i not in ip_list:
            # 确保IP和次数对应关系没错
            ip_list.append(i)
            count_list.append(ip.count(i))
    end = time.clock()
    print "程序运行时间: %f s" % (end - start)
'''
    n = 1
    for i in range(10):
        # 得到count_list列表的最大值（次数），并根据序号找到另一个列表中的IP地址
        x = max(count_list)
        y = count_list.index(x)
        z = ip_list[y]
        print "出现频率第%s多的IP是：%s 共出现%d次" %(n,z,x)
        n = n + 1
        # 在对应列表中删除之前找到元素，便于找出频率第二高的IP和次数
        count_list.remove(x)
        ip_list.remove(z)
end = time.clock()
print "程序运行时间: %f s" % (end - start)
'''