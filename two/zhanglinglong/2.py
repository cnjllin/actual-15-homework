#/usr/bin/python
#coding:utf-8
'''
作业要求：
读取access.txt，找出重复次数前10的IP地址，打印地址和重复次数
'''
#打开日志文件
f = open('access.txt')
'''
从日志文件中，获取所有访问ip地址，组成一个ip列表的集合
'''
#定义一个空列表
ip_list = []
#依次读取日志文件的每行(读取后是个列表)
for i in f.readlines():
    #将读取的每行的字符串按照空格进行切片，获取到ip
    c = i.split(' ')[0]
    #将获取的ip,添加到定义的空列表中，组成ip的集合
    ip_list.append(c)
'''
将ip列表，进行分组计数，并将ip以及ip出现的次数，组成一个词典
'''
#定义一个空字典
k = {}
#依次从ip列表中读取ip（for循环）
for i in ip_list:
#    print i
    #如果添加的ip在新字典中没有，则添加，并计数1
    if i not in k:
        count = 1
        k[i] = count
    #如果添加的ip在新字典中存在，并将之前的values值+1
    else:
        k[i] +=1
'''
将词典按照ip次数进行排序
'''
q = sorted(k.items(),key=lambda item:item[1],reverse=True)[0:10]
for x in q:
    y = (list(x))
    print "ip:%s，访问次数：%s" %(y[0],y[1])
