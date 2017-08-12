#!/usr/bin/python
#coding:utf-8
def data():
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
    return sorted(last,reverse=True)[:10]

def index(data):
    html = "<html>"
    html += "<head> <meta charset='utf-8'> <style> td{ text-align:center;width:180px;}table{border:1px solid #e5e5e5;}"
    html +="td{border:1px solid #e5e5e5;}</style> </head><body><table><caption>IP Top Ten </caption><thead><tr>"
    html +="<td>IP :</td><td>出现次数:</td></tr></thead><tbody>"
    for i in data:
        html += "<tr><td>%s</td><td>%s</td></tr>"%(i[1],i[0])
    html += "</tbody></table></body></html>"
    with open('index.html','a+')as f:
        f.write(html)
if __name__ == '__main__':
    data = data()
    index(data)

