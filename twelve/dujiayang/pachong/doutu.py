import requests
import re
import MysqlDb

db = MysqlDB.connet(
	host='mysql.litianqiang.com',
	port=7150,
	user='test11',
	passwd='123456',
	db='test11',
	charset='utf8',
)

crusor = db.cursor()	

def getImageList():
	res = requests.get('http://www.doutula.com/photo/list/')
	html = res.text
	reg = r'data-original="(.*?)".*?alt="(.*?)"'
	reg = re.compile(reg,re,S)
	imagesList = re.findall(reg,html)
	print len(imageList)
	for i in imageList:
		cursor.execute('insert into image(`name`,imageUrl) values('{}'.'{}')"'.format(i[1],i[0]))
		db.commit()

for i in range(1,1084):
	print i
	getImageList()

db.close()
