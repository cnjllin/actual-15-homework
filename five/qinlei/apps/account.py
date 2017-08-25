#coding:utf-8
from flask import render_template,request,session,redirect
from apps import app,views
import db,datetime

@app.route('/adduser', methods=['GET','POST'])
def adduser():
    msg = ""
    if request.method == "POST":

        '''data：post提交的用户与密码字典'''
        user_dic = dict((k, v[0]) for k, v in dict(request.form).items())
        '''sql_user:数据库用户列表'''
        sql_user = [x['username'] for x in db.query('users', app.config.get('FIELDS'))]

        if user_dic['username'] in sql_user:
            msg = u"用户已经存在"
        else:
            user_dic['create_time']=datetime.datetime.now()
            t_dict = ["%s='%s'" % (k, v) for k, v in user_dic.items()]
            db.adduser('users', t_dict)
            msg = u"添加用户成功"
            return redirect('index')
    else:
        return render_template('account/adduser.html', msg=msg)

@app.route('/search', methods=['GET','POST'])
def search():
    role = session.get('role')
    user = db.query('users', app.config.get('FIELDS'))
    return render_template('account/search.html', user=user )


@app.route('/delete/', methods=['POST','GET'])
def delete():
    if request.method == "GET":
        id = int(request.args.get('id'))
    db.delete('users', id)

    return render_template('account/search.html')

@app.route('/edit/', methods=['POST','GET'])
def edit():

    id = ""

    if request.method == "POST":
        id = int(request.args.get('id'))
        user_dic = dict((k, v[0]) for k, v in dict(request.form).items())
        new_data = dict((k, v) for k, v in user_dic.items() if v)
        t_dict = ["%s='%s'" % (k, v) for k, v in new_data.items()]
        #print t_dict
        db.update('users', t_dict, id)
    else:
        id = int(request.args.get('id'))
        user = db.query('users', app.config.get('FIELDS'), id)

        return render_template('account/edit.html', user=user)
    return render_template('account/edit.html')


