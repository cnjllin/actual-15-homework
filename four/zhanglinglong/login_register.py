#/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/login/',methods=["GET","POST"])
def login():
    #如果前端获取的方法是POST，则接受数据
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print username,password
        #打开用户文件，将用户名存入一个列表，用户名和密码存入一个字典
        f = open('user.txt')
        l = []
        k = {}
        for i in f.readlines():
            i =i.strip('\n')
            a = i.split(':')[0]
            b = i.split(':')[1]
            k[a] = b
            l.append(a)
        #判断用户名是否存在
        if username not in l:
            return "用户名不存在"
            exit()
        else:
            #判断密码是否正确
            if password == k.get(username):
                return "欢迎%s登录" %username
            else:
                return "登录密码错误"
        f.close()
    return render_template("login.html")


@app.route('/register/',methods=["GET","POST"])
def register():
    #如果前端获取的方法是POST，则接受数据
    if request.method=='POST':
        username = request.form.get('username')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        print username,new_password,confirm_password
        m = open('user.txt','a+')
        #判断密码是否为空
        if len(username) == 0:
            return "用户名不能为空"
            exit()
        #打开用户文件，将用户名存入一个列表，检查用户名是否被注册
        l = []
        for i in m.readlines():
            a = i.split(':')[0]
            l.append(a)
        if username in l:
            return "该账户已被注册"
            exit()
        #判断密码是否为空
        if len(new_password) == 0:
            return "密码不能为空"
        #判断两次输入密码是否相同
        if confirm_password == new_password:
            m.write('%s:%s\n' %(username,new_password))
            return "注册成功，您的账号为:%s,密码为:%s,请妥善保管" %(username,new_password)
            exit()
        else:
            return "密码不匹配"
        m.close()
    return render_template("register.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
