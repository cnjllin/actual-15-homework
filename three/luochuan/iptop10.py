# -*- coding: utf-8 -*-
#作业要求:找出日志文件里的前十的IP,并进行排序,并生成html表格
f = open("E:\\actual-15-homework\\two\luochuan\\access.log", "r")  # 读文件
lines = f.readlines()
list_ip =[]
dict = {}
n = 0
sort_list = []

for i in lines:
    ip = i.split(' ')[0]  # 获取IP,并生成IP的队列
    list_ip.append(ip)

for i in list_ip:  # 通过LIST来生成字典,并统计IP出现次数
    if i in list_ip:
        n += 1
        dict[i] = n
    else:
        dict[i] = 1

dic = sorted(dict.items(), key=lambda d: d[1], reverse=True)
for i in range(0, 10):
     sort_list.append(dic[i])

with open("E:\\actual-15-homework\\three\\luochuan\\ip10.html", "a+") as f:
    f.truncate()                                                                        #每次打开文件后清空内容

with open("E:\\actual-15-homework\\three\\luochuan\\ip10.html", "a+") as f:
    Title = '<title>\nTOP 10 IP\n</title>\n<h1 style="color:red">TOP 10 IP</h1>\n'      #拼接开头
    title = '<<table style="height:100px;" border="1" cellspacing="0" bordercolor="#000000" cellpadding="8"<tr><td>IP</td><td>count</td></tr>'   #拼接标题
    html = ''
    f.write(Title)  #写入开头
    f.write(title)  #写入标题
    for i in sort_list:
        html += '<tr><td>%s</td><td>%d</td></tr>\n'%(i[0],i[1])  #写入IP以及访问次数
    f.write(html)
    f.write('</body>\n')
print 'finish'






