from flask import Flask
from flask import render_templae
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return render_templae('index.html')

@app.route('/search')
def search():
	kw = request.args.get('kw')
	count = request.args.get('count')
	cursor.execute("select * from images where `name` like '%{}%'".format(kw))
	data = crusor.fetchmany(int(count))
	return render_template('index.html',images=data)
	
if __name__ == '__main__':
	conn = Mysqldb.connect(
		host='mysql.litianqiang.com',
        	port=7150,
        	user='test11',
        	passwd='123456',
        	db='test11',
        	charset='utf8',
	)
	crusor = db.cursor()
	app.run(debug=True)
