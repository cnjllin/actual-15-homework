""" 需求：读取access.txt（从群共享下载）日志文件，找出重复次数前10的IP地址，打印地址和重复次数
思路分析：打开文件access
          用spilit函数建立ip列表
          将ip与ip计数组成字典，并去重
          组合ip地址与计数组合成列表
          打印ip重复次数前10的IP地址和重复次数"""

#encoding=utf-8
file_list=open("C:\\Users\\xxx\\Desktop\\access.txt")
#读取文档
file=file_list.readlines()
a=[i.split(" ")[0] for i in file]
#将文档ip地址组成列表
b={}
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
#将ip与重复次数组成字典
c={}
for k,v in b.items():
    c.setdefault(v,[])
    c[v].append(k)
#去重
w=[]
o=[]
num=0
for p in range(0,10):
    o.append(max(c.keys()))
    w.append(c.pop(max(c.keys())))
#将IP地址与ip重复次数分别放在空列表w,o内
for u in zip(o,w):
    num+=1
    print "重复第%s多的ip地址是：%s.重复次数为%s"%(num,u[1],u[0])
#组合列表元素，并打印ip重复次数前10的IP地址和重复次数










