#/usr/bin/python
#coding:utf-8
'''
作业要求：
读取access.txt，找出重复次数前10的IP地址，打印地址和重复次数
'''
#定义一个html文件的开头，将后面排序结构追加到html文件的下面
fo = open('log.html','a+')
#HTML文件开头
fo.write("<h1>访问量前10的ip</h1>")
fo.write("<html><table style='border:solid 1px'>")
#定义一个表格，一行2列，两列 内容为ip和出现次数
fo.write('<tr><td style="border:solid 1px">IP</td><td style="border:solid 1px">出现次数</td></tr>')

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
        k[i] = 1
    #如果添加的ip在新字典中存在，并将之前的values值+1
    else:
        k[i] +=1
'''
将词典按照ip次数进行排序
'''
#定义一个空字典
m = {}
for a,b in k.items():
    #将k字典中的k值（ip出现次数）作为新字典的key，并且设置key的默认值为一个空列表
    m.setdefault(b,[])
    #将k字典中的key追加到m字典b的key值的空列表里（将出现次数为b的ip追加到m字典b值的空列表里）
    m[b].append(a)
#循环10次，每次取m字典中key值的最大值的key和values写入到html文件中
count = 0
while count < 10:
    #取m字典中key的最大值（出现次数）
    time = max(m.keys())
    ip = m.get(time)
    #将取出次数最大的ip和次数写入到html的表格中
    fo.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' %(ip,time))
    #删除字典中刚刚取出的items
    m.pop(time)
    count +=1
#关闭日志文件和写完的html文件
f.close()
fo.close()
