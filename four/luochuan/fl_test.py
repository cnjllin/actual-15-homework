# -*- coding: utf-8 -*-
from flask import Flask,request,render_template

app = Flask(__name__)


# @app.route('/submit/')
# def submit():
#     return render_template("submit.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if len(user) == 0 or len(pwd) == 0:
            return "用户名或者密码为空"
    with open('userinfo.txt','a') as f:
        f.write(user+':'+pwd+'\n')
    return redirect('/userlist')


@app.route('/login/', methods=['GET'])
def submit():
     return render_template('submit.html')

@app.route('/login/', methods=['POST'])
def login():
    with open('E:\\fl_test\\zhuce.log', 'r')as f:
        user = request.form.get('username','')
        passwd = request.form.get('password','')
        dict = {}
        Username = []

        for line in f.readlines():
            dict[line.strip().split(":")[0]] = line.strip().split(":")[1]

        for i in dict:
            Username.append(i)

        if user in Username:
            if passwd == dict.get(user):
                choice = '1'
            else:
                choice = '0'
        else:
            choice = '2'
    return render_template('login.html', choice=choice,user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
