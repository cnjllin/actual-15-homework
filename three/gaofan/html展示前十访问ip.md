	 #!/usr/bin/env python
	 #coding:utf-8
	 # 打印出ip访问量前十
	 with open('access.txt') as f:
	     data=f.readlines()
	 info={}
	 for i in data:
	     arr=i.split(' ')
	     ip=arr[0]
	     url=arr[6]
	     status=arr[8]
	     info[(ip,url,status)]=info.get((ip,url,status),0)+1
	 info_list=[(v,k[0],k[1],k[2]) for k,v in info.items()]
	 topten= sorted(info_list,key=lambda x:x[0],reverse=True)[:10]
     # 利用Html展示前十
	 from flask import Flask
	 app=Flask(__name__)
	 @app.route('/gaofan')
	 def index():
	     table = '<html><head><title>IP访问量前十</title></head><body><table border="1"> <tr><th>times</th><th>ip</th><th>url</th><th>status</th></tr>'
	     for i in  topten:
	         table += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % i
	     table += '</table></html>'
	     return table
	 if __name__=='__main__':
	     app.run(host='0.0.0.0',port=9999,debug=True)
* 测试结果：  
	![](https://github.com/51reboot/actual-15-homework/blob/master/three/gaofan/topten-times.png)
