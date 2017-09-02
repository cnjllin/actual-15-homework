#coding:utf-8
#Author:Tailoryang
from flask import Flask,request,render_template,redirect,session
from user import add,select_one,check_role,select_all,update_user,delete_user
import utils
app = Flask(__name__)

# 首页面
@app.route('/')
@app.route('/index')
def index():
    # 判断用户名是否存在，存在直接进入用户列表
    if  'username' in session:
        return redirect('/user')
    else:
        return render_template('index.html')

# 登陆
@app.route('/login',methods=['post','get'])
def login():
    if request.method=='POST':
        user={i:"".join(dict(request.form)[i]) for i in dict(request.form)}
        # 在 user 模块查找用户
        result = select_one(user['username'])
        # 判断返回值是否为元组，不为元组则放回错误页面
        if isinstance(result,tuple):
            session['username'] = user['username']
            return redirect('/user')
        else:
            render_template('error.html',result=result)
    return render_template('index.html')

# 注册
@app.route('/reg',methods=['post','get'])
def reg():
    if request.method == 'POST':
        user = {i: "".join(dict(request.form)[i]) for i in dict(request.form) if i !='repwd' }
        # 在 user 模块添加客户
        result = add(user)
        # 判断返回值是否为SQL语句影响的行数，不为int则SQL执行失败返回错误页
        if isinstance(result,int):
            session['username'] = user['username']
            return redirect('/user')
        else:
            return render_template('error.html',result=result)
    return render_template('index.html')

#判断用户是否存在
@app.route('/checkuser',methods=['post'])
def checkuser():
    username = request.form.get('username')
    user = select_one(username)
    if isinstance(user,tuple):
        result = '1'
    else:
        result = '0'
    return result
# 用户列表
@app.route('/user/')
def user():
    username = session['username']
    role =check_role(username,)
    field = ['id','username','password','role','phone','job']
    # 根据 role 的值放回结果
    if role[0] == 1:
        data = select_all()
    else:
        data = select_one(username)
    if isinstance(data,tuple) or isinstance(data,list):
        if isinstance(data,tuple):
            result = [dict((v, row[k]) for k, v in enumerate(field)) for row in [data]]
        else:
            result = [dict((v,row[k]) for k,v in enumerate(field)) for row in data]
        return render_template('user.html',result=result,enumerate=enumerate,role=role[0])
    else:
        return render_template('error.html',result =data)

# 更新用户信息
@app.route('/update', methods=['post'])
def update():
    # 获取用户信息并删除重复信息
    user = {i:"".join(dict(request.form)[i]) for i in dict(request.form) if i != 'oldpwd' and i != 'repwd'}
    result = update_user(user)
    # 判断返回值是否为SQL语句影响的行数，不为int则SQL执行失败返回错误页
    if isinstance(result, int):
        return redirect('/user')
    else:
        return render_template('error.html', result=result)

# 删除用户信息
@app.route('/del',methods=['post'])
def delete():
    id = request.form.get('id')
    result = delete_user(id)
    if isinstance(result,int):
        return '1'
    else:
        return render_template('error.html',result=result)

# 退出登录
@app.route('/logut')
def logut():
    session.pop('username', None)
    return redirect('/index')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run('127.0.0.1',port=5000,debug=True)


