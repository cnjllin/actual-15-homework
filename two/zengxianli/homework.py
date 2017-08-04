
#coding:utf-8

#打开日志文件，以列表的形式储存，每一行为一个字符串为列表中的一个元素，列表名为data
with open('access.log') as f:
       data = f.readlines()

data1=[] #新建列表，用于存放IP地址
data2=[] #新建列表，用于存放IP地址
tmp={}   #新建字典用于存放IP地址及出现次数，字典的格式为tmp{IP:次数}


for i,ip in enumerate(data):
        data1.append(ip.split(" ")[-3].split(":")[0]) #将列表data中的每个元素（字符串）转换成列表，并提取新列表中的倒数第三个元素（IP地址），存入data2中
        data[i]=ip.split(" ")[0] #将列表data中的每个元素（字符串）转换成列表，并提取新列表中的第一个元素（IP地址），更换掉原data的元素


data1.remove(data1[-1])
data=data+data1 #将data和data2合并成新的列表，并重命名为data，即新列表data中每一个元素为日志中出现的每一个IP地址
data2=data      #将新列表data复制一份，并将副本命名为data2
data=list(set(data)) #将data2去重


#通过遍历列data和data2,得到data中每个IP地址出现的次数i,并将IP地址和次数i重定义为字典tmp，即tmp的格式为｛IP：i｝
for ip in data:
    i=0
    for ip1 in data2:
        if ip==ip1:
           i=i+1
        else:
            continue
    tmp[ip]=i

#将字典tmp中的每一个value值（即上述的次数i）提取出来放进新的列表a中，将a进行倒序排序
a=sorted(tmp.values())
a.reverse()

#遍历列表a倒序后每一个元素，比较遍历字典tmp，由a中的元素（即字典tmp的对应的value值）推出字典tmp中相应的key值（即IP地址），并打印出来
print "统计出现次数最多的前10个IP分别是："
for i in range(0,10):
    for k,v in tmp.items():
        if v==a[i]:
            print "IP:%s 出现的次数为：%s次" % (k,tmp.pop(k))
            break
        else:
            continue

