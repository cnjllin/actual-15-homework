#!/usr/bin/python
#conding:utf-8
from flask import render_template,url_for,redirect,request
from sqlalchemy_test import *

db.create_all()
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user_pass = request.form.get('user_pass')
        result = user_login(user_name,user_pass)
        if result == "Welcome!":
            user_info = User.query.filter(User.user_name == user_name).first()
            global id_num_init
            id_num_init = user_info.id_num
            user_all = User.query.all()
            length = range(len(user_all))
            return render_template('after_login.html',user_info=user_info,
                                  user_attr=user_attr,user_all=user_all,length=length)
        else:
            return render_template("login.html",result=result)
    return render_template("login.html")


@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        user_dict = dict(request.form)
        result = user_reg(user_dict)
        if result == "sign up successfully!":
            return redirect('/login/')
        else:
            return render_template("reg.html",
                                   result=result)
    return render_template("reg.html")

@app.route('/update/',methods=['GET','POST'])
def user_up():
    id_num = request.args.get('id_num')
    user_info1 = user_query(id_num)
    if request.method == "POST":
        user_dict = dict(request.form)
        result = update_user(id_num,user_dict)
        if result == "update successfully!":
            user_info = User.query.filter(User.id_num == id_num_init).first()
            user_all = User.query.all()
            length = range(len(user_all))
            return render_template('after_login.html',user_info=user_info,
                                   user_attr=user_attr,user_all=user_all,
                                   length=length)
        else:
            return render_template('update.html',user_info=user_info1,
                                   id_num=id_num,result=result)
    return render_template('update.html',user_info=user_info1,id_num=id_num)

@app.route('/delete/')
def delete():
    id_num = request.args.get('id_num')
    user_delete(id_num)
    user_info = User.query.filter(User.id_num == id_num_init).first()
    user_all = User.query.all()
    length = range(len(user_all))
    return render_template('after_login.html',user_info=user_info,user_attr=user_attr,
                           user_all=user_all,length=length)

if __name__=='__main__':
    app.run(host='0.0.0.0')
