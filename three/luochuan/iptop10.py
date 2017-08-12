# -*- coding: utf-8 -*-
#作业要求:找出日志文件里的前十的IP,并进行排序,并生成html表格




def top10():
    f = open("E:\\actual-15-homework\\two\luochuan\\access.log", "r")  # 读文件
    lines = f.readlines()
    list_ip = []
    dict = {}
    n = 0

    for i in lines:
        ip = i.split(' ')[0]  # 获取IP,并生成IP的队列
        list_ip.append(ip)

    for i in list_ip:  # 通过LIST来生成字典,并统计IP出现次数
        if i in list_ip:
            n += 1
            dict[i] = n
        else:
            dict[i] = 1

    dic = sorted(dict.items(), key=lambda d: d[1], reverse=True)  # 将生成的字典转变为LIST,并通过VALUE来排序
    return dic
    # for i in range(0, 10):
    #     return '%s ----> %s' % (dic[i][0], dic[i][1])  # 打印出前十的IP以及出现次数
with open(E:\\actual-15-homework\\three\\luochuan\\ip10.html','w') as f:         #循环追加前十个ip地址和对应的次数,同html一起追加到文件中
        join = '<table style=height:100px border=2 ellspacing=0 bordercolor=#000000 cellpadding=8<tr><td>IP</td><td>访问次数</td></tr>'
        #join = "<table border='2'><tr><td>IP</td><td>访问次数</td></tr>"
    	for (ip),count in List[:-sort_length-1:-1]:
            join +="<tr><td>%s</td><td>%s</td></tr>"%(ip,count)
    	    join +='</table>'
        f.write(join)
        return 'success'    #追加成功，返回一个success.
print Sort_log('access.log')
