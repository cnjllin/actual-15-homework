#!/usr/bin/python
#coding:utf-8


#统计top10 ip 函数
def dict_1():
    with open("/server/scripts/python/access.txt",'r') as f:
         ips_list = {}
         users = [] 
         #遍历文件，生成key为ip,value为次数的字典
         for n in f.read().split("\n"):
             ips_list[n.split(" - - ")[0]]=ips_list.get(n.split(" - - ")[0],0)+1    

    p = sorted(ips_list.items(),key=lambda d:d[1])
    for n in range(10):
        users.append(p[(-n-1)])
    usera = users
    return  usera
   
