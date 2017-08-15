# -*- coding: utf-8 -*-
# 创建后续代码需要的列表和字典
ip = []
ip_dict = {}
# 将日志文件按行读取，并组成列表
file = open('F:\\access.txt')
log_list = file.readlines()
file.close()
    # 分割出IP，并将所有IP添加到l_list列表
for i in log_list:
    l_list = i.split()
    ip.append(l_list[0])
# 将IP地址和出现次数添加到字典中
for i in ip:
    ip_dict[i] = ip_dict.get(i,0) + 1
# 反转dict，形成dict2
dict2 = {}
for k,v in ip_dict.iteritems():
    dict2.setdefault(v,[])
    dict2[v].append(k)
# 找出出现次数前10的IP地址，并将结果输出到html文件
n = 1
with open('F:\\test.html','w+') as f:
    f.write('<table border="1">\n''<tr>\n''<td>排名</td>\n''<td>出现次数</td>\n''<td>IP</td>\n''</tr>\n')
    for i in range(10):
        x = max(dict2.keys())
        f.write(('<tr>\n''<td>%d</td>\n''<td>%d</td>\n''<td>%s</td>\n''</tr>') %(n,x,",".join(dict2[x])))
        n = n + 1
        dict2.pop(x)
