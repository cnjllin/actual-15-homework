#/bin/env python
#coding=utf-8

'''
统计nginx访问日志，打印top10 IP ,url ,访问次数
'''

from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/nginxtop10')

def res():
	temp_dict = {}
	with open('access.txt','a+') as f:
		for log in f:
			temp = log.split()
			tup = (temp[0],temp[6],temp[8])
			temp_dict[tup] = temp_dict.get(tup,0)+1
	res_list=temp_dict.items()
	res_list = sorted(res_list,key=lambda x:x[1],reverse=True)
	#循环
	i = 0
	html_str = '<table border="1px">'
	html_str +='<tr><td>TOP10</td><td>IP</td><td>URL</td><td>status</td><td>count</td></tr>'
	for j in res_list[:10]:
		i = i+1
		html_str += '<tr><td>No%s</td> <td>%s</td><td>%s</td><td>%s</td><td>%s</td>'%(i,j[0][0],j[0][1],j[0][2],j[1])
	html_str+='</table>'
	html_f = open('/home/yang.liu/python/day4/templates/nginxtop10.html','a+')
	html_f.write(html_str)
	html_f.close()

	return render_template('nginxtop10.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9999,debug=True)

