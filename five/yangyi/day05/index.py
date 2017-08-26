from flask import Flask ,request,render_template,redirect,session
import DB
app = Flask(__name__)

# 首页面
@app.route('/')
def index():
    return render_template("login.html")

'''
用户登录
1.用户名存在向前端放回1否则放回0
2.用户名密码验证成功前往index页
'''
# 用户登录模块
@app.route('/login',methods=['post','get'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        session['username'] =username
        sql = 'SELECT * FROM user WHERE username = "%s" AND password = "%s"'%(username,password)
        try:
            resp = DB.execute(sql,'select')
            if resp:
                return redirect('/user/')
            else:
                error=u'用户名密码不一致'
                return render_template("login.html", error=error)
        except Exception as error:
            return render_template("login.html",error = error)
    return render_template('login.html')

#用户注册模块
@app.route('/register',methods=['post'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        session['username'] = username
        if username =='admin':
            sql = 'INSERT INTO user(username,password,role) values("%s","%s",%d)'%(username,password,1)
        else:
            sql = 'INSERT INTO user(username,password) values("%s","%s")'%(username,password)
        try:
            resp = DB.execute(sql,'insert')
            if resp:
                return redirect('/user/')

        except Exception as error:
            return render_template("login.html", error = error)
    return render_template('login.html')
#用户中心
@app.route('/user/',methods=['post','get'])
def user():
    username = session['username']
    sql = 'SELECT  role FROM user WHERE username = "%s" ;'%username
    role = DB.execute(sql,'select')[0][0]
    if role :
        sqlb='SELECT * FROM user ;'
    elif not role:
        sqlb = 'SELECT * FROM user WHERE username ="%s";'%username
    result = DB.execute(sqlb,'select')
    return render_template('user.html',result=result,role=role, enumerate=enumerate)

#判断用户是否存在
@app.route('/checkuser',methods=['post'])
def checkuser():
    username = request.form.get('username')
    sql ='SELECT * FROM user WHERE username = "%s"'%username
    user = DB.execute(sql,'select')
    if user:
        result = '1'
    else:
        result = '0'
    return result
#删除用户
@app.route('/del',methods=['post'])
def delete():
    id = int(request.form.get('id'))
    sql = 'DELETE FROM user WHERE id = %d'%id
    result = DB.execute(sql,'delete')
    return result
#添加用户
@app.route('/add',methods=['post','get'])
def add():
    if request.method=='POST':
        username = request.form.get('username')
    return render_template('add.html')
#更新用户
@app.route('/update',methods=['post'])
def update():
    id = request.form.get('id')
    password = request.form.get('pwd')
    sex = request.form.get('sex')
    age = request.form.get('age')
    phone = request.form.get('phone')
    email = request.form.get('email')
    sql = 'UPDATE user SET password = "%s",sex=%s,age=%s,phone="%s",email="%s" WHERE id =%s;'%(password,sex,age,phone,email,id)
    result = DB.execute(sql, 'delete')
    if result > '0':
        return redirect('/user/')
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run('127.0.0.1',port=5000,debug=True)

