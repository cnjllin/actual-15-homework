#/usr/bin/python
#coding=utf-8
# 感觉执行时间比较长，而且前十的取值，有BUG，后续数值跟第十个相同的情况下，应该也要取出。不会写(⊙﹏⊙)b

#定义一个空列表存储获取到的IP
ip_list = []
#定义一个空dict获取IP:对应相同次数
ip_dict = {}
#定义一个空list存储IP出现的次数
ip_count = []

#读取文件，切割文件，取出IP地址
with open('/Users/wj/Desktop/access.txt','r') as ip_file:
    log_list = ip_file.readlines()
    #用一个临时空列表，给ip_list增加ip
    for i in log_list:
        temp_list = i.split()
        ip_list.append(temp_list[0])
        #print ip_list
    #用循环，判断是否存在字典，不存在则添加
    for i in ip_list:
        if i not in ip_dict:
            ip_dict[i] = ip_list.count(i)
            #print ip_dict
    ip_list = ip_dict.keys()

    #循环取出次数

    for i in ip_list:
        ip_count.append(ip_dict.get(i))
        #print ip_count
    Count = 1
    #通过次数以及IP对应关系，取出前十
    for i in range(10):
        x = max(ip_count)
        y = ip_count.index(x)
        z = ip_list[y]
        ip_count.remove(x)
        ip_list.remove(z)

        print "Ip出现频率第%s多的IP地址是：%s 出现了%s次" %(Count,z,x)
        Count += 1