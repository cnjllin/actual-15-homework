#encoding=utf-8
""" 需求：读取access.txt（从群共享下载）日志文件，找出重复次数前10的IP地址，打印地址和重复次数
思路分析：打开文件access
          用spilit函数建立ip列表
          将ip与ip计数组成字典，并去重
          组合ip地址与计数组合成列表
          打印ip重复次数前10的IP地址和重复次数"""

file_list=open("C:\\Users\\xxx\\Desktop\\access.txt")
#读取文档
file=file_list.readlines()
file_list.close()
a=[i.split(" ")[0] for i in file]
#将文档ip地址组成列表
k=[i.split(" ")[6] for i in file]
u=[i.split(" ")[8] for i in file]
b={}
for i in file:
    e=i.split(" ")
    ip,url,status=e[0],e[6],e[8]
    b[(ip,url,status)]=b.get((ip,url,status),0)+1

c={}
for k,v in b.items():
    c.setdefault(v,[])
    c[v].append(k)
w=[]
o=[]
num=0
f=open('C:\\Users\\xxx\\Desktop\\lhs.html','a+')
f.write("<html><h4>常用ip地址</h4><table border=1 style='border:solid 1px'>")
f.write("<th p style='background-color:rgb(0,255,255)' style='border:solid 1px'>访问次数</th><th p style='background-color:rgb(0,255,255)' style='border:solid 1px'>ip地址</th><th p style='background-color:rgb(0,255,255)' style='border:solid 1px'>url</th><th p style='background-color:rgb(0,255,255)' style='border:solid 1px'>status</th>")
for p in range(0,10):
    o.append(max(c.keys()))
    w.append(c.pop(max(c.keys())))

#将IP地址与ip重复次数分别放在空列表w,o内
for u in zip(o,w):
    num+=1
    f.write('<tr p style="background-color:rgb(0,255,255)" style="border:solid 1px"><td>%s</td> <td p style="background-color:rgb(0,255,255)" style="border:solid 1px">%s</td><td>%s</td><td>%s</td></tr>'%(u[0],u[1][0][0],u[1][0][1],u[1][0][2]))
f.write("</table></html>")
f.close()
    #print "重复第%s多的ip地址是：%s.重复次数为%s"%(num,u[1],u[0])
#组合列表元素，并打印ip重复次数前10的IP地址和重复次数“”“