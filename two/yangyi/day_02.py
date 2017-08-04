#!/usr/bin/python
#coding:utf-8
statistics={}
last=[]
with open(r'access.txt',"r") as f :
    # for循环日志文件的每一行
    for i in f:
    # 判断字典中是否存在此ip 存在 value +=1 不存在 key = ip value =1
        if str(i).split(" ")[0] in statistics:
            statistics[str(i).split(" ")[0]] +=1
	else:
	    statistics.setdefault(str(i).split(" ")[0],1)	
# for循环字典反转key 与value的值并 append 至列表
for k,v in statistics.items():
    last.append((v,k))
print'#####'*3,'TOP10IP',"#####"*3
# 取出所有ip中出现次数最高的10个并输出
for k ,v in sorted(last,reverse=True)[:10]:
    print'IP:%s  出现次数: %s'%(k[1],k[0])

