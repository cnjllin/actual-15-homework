#coding:utf-8

from flask import render_template,request,redirect,session,flash,url_for
from apps import app,db,models
import datetime

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/overview')
def overview():

    return render_template('base.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    mess_error = ''
    if request.method == "POST":

        username = request.form.get('username', None)
        password = request.form.get('password', None)

        user = models.Users.query.filter_by(username=username).first()

        if user is not None and password == user.password:
            session['logged_in'] = True
            return redirect('overview')

        else:
            mess_error = u"用户名或密码错误"

    return render_template('login.html', mess_error=mess_error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/chuser')
def chuser():

    return render_template('usermanager.html')

@app.route('/adduser', methods = ['GET', 'POST'])
def adduser():
    err_msg = ""
    if request.method == "POST":
        username = request.form.get('username', None)
        password1 = request.form.get('password1', None)
        password2 = request.form.get('password2', None)
        sex = request.form.get('sex', None)
        age = request.form.get('age', None)
        phone = request.form.get('phone', None)
        email = request.form.get('email', None)
        role = request.form.get('role', None)

        user = models.Users.query.filter_by(username=username).first()

        if user is None:
            user = models.Users(username=username, password=password1,age=age,phone=phone, email=email,date=datetime.datetime.now())
            db.session.add(user)
            db.session.commit()
        else:
            err_msg = u"%s已经存在" , user.username

    return render_template('adduser.html',err_msg=err_msg)

@app.route('/search', methods=['POST', 'GET'])
def search():
    err_msg = ""

    user = models.Users.query.all()

    #for i in user:
    #    print i.id, i.username, i.sex, i.age, i.phone, i.email, i.role, i.date

    return render_template('search.html',user=user)