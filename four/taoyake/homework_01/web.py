#coding:utf-8
from flask import Flask,render_template,request,redirect
import user
app = Flask(__name__)



@app.route('/login',methods=['GET','POST'])
def login():
    # 第一步：获取用户名和密码数据
    # 判断请求方式
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    password = params.get('password')  

    # 第二步：登录验证，成功返回页面，失败给出提示
    if user.UserLogin(username, password):
        print '登录成功'
        return redirect('/userlist')
    else:
        print '登录失败'
        return render_template('login.html', username=username, error=u'用户名或密码错误')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/userlist')
def userlist():
    userlist = []
    with open('userinfo.txt') as f:
        for l in f:
            userlist.append(l.split(':'))
        return render_template('userlist.html',userxxx=userlist)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if len(user.strip()) == 0 or len(pwd.strip()) == 0:
            return "用户名或者密码为空"
        with open('userinfo.txt','a') as f:
            f.write(user+':'+pwd+'\n')
            return redirect('/userlist')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8999,debug=True)
