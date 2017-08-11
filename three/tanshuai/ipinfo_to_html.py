# coding: utf-8
import sys

'''第一步：将日志处理代码封装成一个函数
'''
def get_topn(log_files, topn=10):
	# 定义一个字典，作为数据存储池
	rt_dict = {}

	# 第一步：读取文件
	log_files = open(log_files, 'r')
	while True:
		# 每次循环读取一行日志
		lien = log_files.readline()
		if not lien:
			break
		# 获取ip
		line_info = lien.split()
		(ip,url,status) = line_info[0],line_info[6],line_info[8]
		# 结果存入dict
		if (ip,url,status) not in rt_dict:
			rt_dict[(ip,url,status)] = 1
		else:
			rt_dict[(ip,url,status)] += 1
	log_files.close()

	# 第二步：转换list，方便排序
	rt_list = rt_dict.items()

	# 第三步：排序统计出top10 ip信息
	for j in range(0, topn):
		for i in range(0, len(rt_list) - 1):
			if rt_list[i][1] > rt_list[i + 1][1]:
				rt_list[i], rt_list[i + 1] = rt_list[i + 1], rt_list[i]
	return rt_list[-1: -(topn + 1):-1]

log_files = 'access.txt'
log_list = get_topn(log_files,topn=200)
# print log_list




'''第二步：拼接HTML
'''
head = '<html>\n<head>\n<meta charset="UTF-8">\n<title>IPTOP10</title>\n</head>\n'
body = head + '<body>\n<table border="1px">\n'
thead = body + '<thead>\n<tr>\n<th>IP地址</th>\n<th>URL</th>\n<th>Status</th>\n<th>次数</th>\n</tr>\n</thead>\n'
tbody = thead + '<tbody>\n'
for log in log_list:
    tbody += '<tr>\n<td>{0}</td>\n<td>{1}</td>\n<td>{2}</td>\n<td>{3}</td>\n</tr>\n'.format(log[0][0],log[0][1],log[0][2],log[1])
tbody = tbody + '</tbody>\n'
html_text = tbody + '</table>\n</body>\n</html>'
# print html_text



'''将凭借的字符串写入html文件
'''
with open('log_info.html', 'w+') as f:
	f.write(html_text)



