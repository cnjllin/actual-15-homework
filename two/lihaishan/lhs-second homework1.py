
""" 需求：读取access.txt（从群共享下载）日志文件，找出重复次数前10的IP地址，打印地址和重复次数
思路分析：打开文件access
          用spilit函数建立ip列表
          将ip与ip计数组成列表
          冒泡排序：比较列表内相邻两元素大小，如果第一个元素比第二个元素大则交换两个元素的为准
          反转
          打印ip重复次数前10的IP地址和重复次数"""

#encoding=utf-8
file_list=open("C:\\Users\\xxx\\Desktop\\access.txt")
#读取文档
a=[i.split(" ") [0] for i in file_list]
#建立ip列表
b=[(x,a.count(x)) for x in a ]
#把ip与ip计数组成列表
num_=0
kong_list=[ ]
for  m in b:
    if m not in kong_list:
        kong_list.append(m)
#去重复数据  c=kong_list.append(m) for m in b if m not in kong_list？
num=len(kong_list)-1
for o in range(num):
    for w in range(0,num-o):
        if kong_list[w][1]>kong_list[w+1][1]:
            kong_list[w],kong_list[w+1]=kong_list[w+1],kong_list[w]
#冒泡排序
kong_list.reverse()
#列表反转
while num_<10:
    num_+=1
    print "%s，重复次数为%s" %(kong_list[num_-1][0],kong_list[num_-1][1])
#打印ip重复次数前10的IP地址和重复次数





