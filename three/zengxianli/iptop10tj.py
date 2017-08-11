#coding: utf-8

log_files  = 'access.txt'
# 定义一个字典，用于存放统计后的数据
rt_dict = {}
# 以读取方式打开文件
log_files = open(log_files, 'r')

# 读取文件：
while True:     # 使用while True来循环读取文件
    # 每次循环读取一行文件内容
    line = log_files.readline()
    # 判断读取信息为空则跳出循环(严格的access日志一般不会有空行哈,所以这里直接了断break)
    if not line:
        break
    # 获取ip信息
    line_info = line.split() # 默认使用空格分割
    ip = line_info[0]
    # 这里如何判断ip是否在存在dict中呢？使用not in dict
    if ip not in rt_dict:
        # 如果没有在dict里，就算这个IP出现了一次，并存入dict
        rt_dict[ip] = 1
    else:
        # 如果dict里存在这个ip，则把这个ip出现的次数加一次
        rt_dict[ip] += 1
# 循环统计完成后，关闭文件
log_files.close()
#print rt_dict

# 2、排序并打印进HTML文件

res={}

for k,v in rt_dict.items():
    res.setdefault(v,[])
    res[v].append(k)


count=0
f=open('tongji.html','a+')
f.write("<html>")
f.write("<table style='height:30px;' border='3' cellspacing='3' cellpadding='3'>")
f.write("<tr><td>出现次数</td><td>IP地址</td></tr>")
while count<10:
    key=max(res.keys())
    for word in res[key]:
        f.write("<tr><td>%s</td><td>%s</td></tr>" % (key,word))
    res.pop(key)
    count=count+1
f.write("</table></html>") 
f.close() 
