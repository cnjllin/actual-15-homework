#!/usr/bin/python
#-*-coding:utf-8-*-
#读取日志文件的函数,并且打印出来ip
def Read_log(File):
    with open(File) as f:
        Dict={}
        for line in f:
            if line == '\n':
                continue
            temp = line.split()
            ip = temp[0]
            Dict[(ip)] = Dict.get((ip),0)+1
    return Dict
#定义一个排序函数,通过冒泡排序实现前十个访问日志信息，ip,url
def Sort_log(File):
    List = Read_log(File).items()
    length = len(List)
    for j in range(length-1):
        for k in range(length-j-1):
            if List[k][1] > List[k+1][1]:
                List[k],List[k+1] = List[k+1],List[k]
        if j >= 10:
            if List[-j][1] != List[-j-1][1]:
                sort_length = j
                break
    with open('status.html','w') as f:
    	join = "<table border='1'><tr><td>ip</td><td>count</td></tr>"
    	for (ip),count in List[:-sort_length-1:-1]:
            join +="<tr><td>%s</td><td>%s</td></tr>"%(ip,count)
    	join +='</table>'
        f.write(join)
        return 'ok'
print Sort_log('access.log')
