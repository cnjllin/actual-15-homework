#!/usr/bin/python
#-*-coding:utf-8-*-
#date:2017-08-10
#author:taoyake

#读取nginx日志文件,并且用一个新字典统计出来ip以及访问的次数
def Read_log(File):
    with open(File) as f:
        Dict={}
        for line in f:
            if line == '\n':
                continue
            temp = line.split()
            ip = temp[0]
            Dict[(ip)] = Dict.get((ip),0)+1
    return Dict            #return这个字典

#定义一个排序函数,通过冒泡排序实现前十个访问日志信息，ip,和count次数
def Sort_log(File):
    List = Read_log(File).items()
    length = len(List)
    for j in range(length-1):
        for k in range(length-j-1):
            if List[k][1] > List[k+1][1]:
                List[k],List[k+1] = List[k+1],List[k]
        if j >= 10:    
            if List[-j][1] != List[-j-1][1]:   #判断假如倒数第十个次数跟倒数第十一次数个不相等
                sort_length = j                #赋值sort_length为j
                break
    with open('status.html','w') as f:         #循环追加前十个ip地址和对应的次数,同html一起追加到文件中
        join = "<table style=height:100px border=2 ellspacing=0 bordercolor=#000000 cellpadding=8<tr><td>IP</td><td>访问次数</td></tr>"
        #join = "<table border='2'><tr><td>IP</td><td>访问次数</td></tr>"
    	for (ip),count in List[:-sort_length-1:-1]:
            join +="<tr><td>%s</td><td>%s</td></tr>"%(ip,count)
    	join +='</table>'
        f.write(join)
        return 'success'    #追加成功，返回一个success.
print Sort_log('access.log')
