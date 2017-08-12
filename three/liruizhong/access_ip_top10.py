#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
# ==========================================
#      FileName: access_ip_top10.py 
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-08-11
# ==========================================
"""

# 将获取topn的日志处理代码封装成函数
def get_topn(topn=10):
    d = {}
    with open('access.txt','r') as f:
        for i in f:
            line_info = i.split(' ')
            (ip,url,status) = line_info[0],line_info[6],line_info[8]
            if (ip,url,status) not in d:
                d[(ip,url,status)] = 1
            else:
                d[(ip,url,status)] += 1
        list1 = sorted(d.items(),key=lambda item:item[1])
        return list1[-1:-(topn+1):-1]

# 拼接HTML
def html():
    log_list = get_topn(topn=10)
    head = '<html>\n<head>\n<meta charset="UTF-8">\n<title>IPTOP10</title>\n</head>\n'
    body = head + '<body>\n<table border="1px">\n'
    thead = body + '<thead>\n<tr>\n<th>IP地址</th>\n<th>URL</th>\n<th>Status</th>\n<th>次数</th>\n</tr>\n</thead>\n'
    tbody = thead + '<tbody>\n'
    for log in log_list:
        tbody += '<tr>\n<td>{0}</td>\n<td>{1}</td>\n<td>{2}</td>\n<td>{3}</td>\n</tr>\n'.format(log[0][0],log[0][1],log[0][2],log[1])
    tbody = tbody + '</tbody>\n'
    html_text = tbody + '</table>\n</body>\n</html>'
    return html_text

# 将拼接的字符串写入html文件
def write_html():
    html_text = html()
    with open('log_info.html','w+') as f:
        f.write(html_text)


if __name__ == '__main__':
    write_html()
