#!/usr/bin/env python
#coding:utf-8


from flask import Flask,request,render_template,redirect
from util import _reg,_login,_select_all,_select_name,_delete,_update
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

# 首页
@app.route('/')
@app.route('/index/')
def index():
    username = 'changhuawei'
    return render_template("index.html",username=username)
# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    user = {}
    res_err = {'code':0,'msg':''}
    if request.method == 'POST': 
        data = {k:v[0] for k,v in dict(request.form).items()}
        # 判断用户密码为空
        if data['username'] == '' or data['password'] == '':
            res_err['code'] = 1
            res_err['msg'] = 'name or passwd null'
            return render_template('reg.html',err=res_err)
        elif _select_name(data):
            res = _select_name(data)
            if res != None:
                res_err['code'] = 2
                res_err['msg'] = 'name is exit'   
                return render_template('reg.html',err=res_err)
        else:
                _reg(data)
                return redirect('/login/')       
    return render_template('reg.html',err=res_err)
# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    res_err = {'code':0,'msg':''}
    if request.method == 'POST': 
        data = {k:v[0] for k,v in dict(request.form).items()}
        # 判断用户密码是否空
        if data['username'] == '' or data['password'] == '':
            res_err['code'] = 1
            res_err['msg'] = 'name or passwd null'
            return render_template('login.html',err=res_err)
        # 判断用户和密码并返回信息，根据角色跳转不通的页面
        else:
         # _login(data):
            fileds = ['id','username','password','role','email']
            user = _login(data)
            # print user
            if user == None:
                res_err['cord'] = 2
                res_err['msg'] = 'name or passwd err'
                return render_template('login.html',err=res_err)
            ss = dict(zip(fileds,user))
            if data['username'] == ss['username'] and data['password'] == ss['password']:
                if ss['role'] == 0:
                    res = _select_all()
                    # print res
                    return render_template('user_list.html',result=res)
                else:
                    res = _select_name(data)
                    # print res
                    return render_template('user_info.html',result=res)
            res_err['cord'] = 2
            res_err['msg'] = 'name or passwd err' 
    return render_template('login.html',err=res_err)

@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        print data
        res_user = _update(data)
        res = _select_all()
        print res
        return render_template('user_list.html',result = res)
    else:
        data = {}
        uid = request.args.get('id')
        data['id'] = uid
        res = _select_name(data)
        print res 
        return render_template('update.html',result = res)



@app.route('/delete/')
def delete():
    data = {}
    uid = request.args.get('id')
    data['id'] = uid
    # print data
    _delete(data)
    res = _select_all()
    # print res
    return render_template('user_list.html',result = res)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True )

