# -*- coding: utf-8 -*-

f = "C:\Users\Administrator\Documents\Tencent Files\865521104\FileRecv\ccess.txt"

'''第一个循环，获取IP列表'''
op = file(f)
li = []
for i in op:
    li.append(i.split(" ")[0])
op.close()


'''第二个循环，把第一次循环获得的列表去重，'''

li2=[]
for x in li:
    if x in li2:
        continue
    else:
        li2.append(x)

'''第三个循环，统计第一次循环的IP列表中的重复数量'''

li3 = []
for a in li2:
    li3.append((a,li.count(a)))


'''第四个循环，使用冒泡排序，或插入排序实现排序功能'''

'''
for i in range(len(li3)-1):
    for j in range(i+1,len(li3)):
        if li3[i][1]>li3[j][1]:
            temp = li3[i]
            li3[i] = li3[j]
            li3[j] = temp
'''

for i in range(0,len(li3)):
    for j in range(i+1,len(li3)):
        if li3[i][1]>li3[j][1]:
            li3[i],li3[j] = li3[j],li3[i]

'''第五个循环，格式化输入打印'''

li4 = li3[-10:]
li4.reverse()

for i in li4:
    print "%s,%+10s" % (i[0],i[1])


