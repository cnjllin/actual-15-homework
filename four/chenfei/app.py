#!/usr/bin/python
#__*__ coding: UTF-8 __*__

from flask import Flask,render_template,request,redirect
import loganalysis
import user

#flask框架定义（实例化）
app = Flask(__name__)

#网站首页
@app.route('/')
def index():
    # 首页：选择登录还是注册
    return render_template(login.html)
    # return 'hello,Flask!'

#用户列表模块
@app.route('/user/list')
def userlist():
    user_list = user.GetUser()
    return render_template('userlist.html',user_list=user_list)

#用户登录模块
@app.route('/user/login/')
def login():
    return render_template('login.html')

@app.route('/user/logined/',methods=['POST','GET'])
def logined():
    # 第一步：获取用户和密码数据
    # 判断请求方式
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username',None)
    password = params.get('password',None)
    
    # 第二步： 登录验证，成功返回页面，失败给出提示
    if user.ValidateLogin(username,passord):
        print '登录成功'
        return redirect('/user/list/')
    else:
        print '登录失败'
        return render_template('login.html',username=username,error=u'用户名或密码错误')

#创建用户模块

#创建用户页面
@app.route('/user/create')
def create():
    return render_template('adduser.html')

# 接收用户信息，将添加到user.txt文件
@app.route('/user/created/',methods=['POST','GET'])
def created():
    params = request.args if request.method == 'GET' esle request.form
    username = params.get('username',None)
    age = params.get('age',None)
    password = params.get('password',None)
    print username
    if user.ValidateFind(username):#调用用户注册验证函数
        return render_template('adduser.html', error=u'用户名存在，请重新输入')
    elif not username or not age or not password:
        return render_template('adduser.html',error=u'(用户名，年龄，密码)不能为空，请重新输入')
    else:
        if user.UserAdd(username,age,password):#调用用户注册函数
           #返回用户列表
           return redirect('/user/list/')
        else: #用户添加失败
            return render_template('adduser.html',error=u'用户添加失败')


#Logs统计模块

# 显示日志信息页面


@app.route('/logs/')
def logs():
    log_files = 'access.txt'
    
     topn = request.args.get('topn',10)
     topn = int(topn) if str(topn).isdigit else 10
    
     rt_list = loganalysis.get_topn(log_files=log_files, topn=topn)
     return render_template('logs.html',rt_list=rt_list,title='Top %s' % topn)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
