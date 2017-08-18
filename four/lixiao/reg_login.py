#!/usr/bin/python
#coding:utf-8

from flask import Flask,request,render_template
app = Flask(__name__)

##first module
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('login.html')


@app.route('/rega/',methods=['GET','POST'])
def reg():
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    re_passwd = request.form.get('re_passwd')
     
    with open('/python/homework/user.txt','a+') as fo:
        if len(username.strip()) == 0: 
            return "sorry,用户名不能为空！"
         
        elif passwd != re_passwd or len(passwd) == 0:
                return "密码不一致或者密码为空！请重新输入"
        else:
                fo.write('%s:%s \n' %(username,passwd))
                return "注册成功"
    

#######login module
def check_login(username,passwd):
    name = []
    res = {}
    with open('/python/homework/user.txt') as files:
        data = files.readlines()
    for n in data:
        sti = n.strip('\n').split(':')
        res[sti[0]] = sti[1].strip()
        name.append(sti[0].strip())

    if username not in name:
        return "user not is exist!"
    else:
        if passwd != res[username]:
            return 'pwd is wrong'
        else:
            return "sucess"

@app.route('/login/',methods=['GET','POST'])
def login():
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    return check_login(username,passwd)


@app.route('/reg/',methods=['GET','POST'])
def biaoge():
  return render_template('reg.html')


if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8888,debug=True)
