# -*- coding:utf-8 -*-
from app import app
from flask import g,session,render_template,request,url_for,redirect
from util import chaxun, insert,delete,select,update,cha_uid,insert_article,search_art
from code import gene_code
import sys,os
app.config['SECRET_KEY'] = os.urandom(24)
reload(sys)
sys.setdefaultencoding('utf-8')
from functools import wraps
import passwd_hash
import cStringIO,StringIO

def login_required(func) :
    @wraps(func)
    def wrapper(*args,**kwargs) :
        if session.get('uid') :
           return func(*args,**kwargs)
        else :
            return redirect(url_for('login'))
    
    return wrapper

@app.context_processor   
def mycontext_processor() :
    uid = session.get('uid')
    print uid
    if uid :
        userinfo1 = cha_uid(uid)
        if userinfo1 :
            return {'userinfo1':userinfo1}
    return {}
            

@app.route('/userlist/',methods = ['GET','POST'])
@login_required
def userlist():
    userinfos = chaxun()
    #列表推导式过滤掉普通用户只显示本人
    userinfos = [ userinfo for userinfo in userinfos if session.get('role') == 0 or (session.get('role') != 0 and session.get('uid')== userinfo.get('uid')) ]
    return render_template('userlist.html',users = userinfos)

@app.route('/dele/',methods=['GET','POST'])
def dele():
    session_uid = session.get('uid')
    uid = request.args.get('id')  #type uid <type 'unicode'> session_uid <type 'int'>
    result = delete(uid)
    #print "uid %s session_uid %s" % (uid,session_uid)
    #print "type uid %s session_uid %s" % (str(type(uid)),str(type(session_uid)))
    if int(uid.encode("utf-8")) == session_uid :
        print "del %s" % session.get('uid')
        del session['uid']  #不删除判断login_required报错
    print "del %s" % session.get('uid')
    return redirect(url_for('userlist'))

@app.route('/upd/',methods=['GET','POST'])
def upd():
    if request.method == 'GET':
        uid = request.args.get('id')
        userinfo = cha_uid(uid)
        print "upd" ,userinfo
        return render_template('upd.html',n = userinfo)
    else :
        users = request.form.to_dict()
        #users = { k:v[0] for k,v in dict(request.form).items() }  等价与上面的
        users = { k:v.replace("管理员","0").replace('普通用户','1') for k,v in users.items() }
        if len(users.get('passwd')) < 90 :
            users = passwd_hash.set_password(users) #修改的密码重新加密
        print "upd :" ,users
        update(users)
        return redirect(url_for('userlist'))

@app.route('/code',methods=['GET','POST'])
def code():
    code_str,code_img = gene_code()
    session['code'] = code_str.lower()
    print gene_code()
    buf = cStringIO.StringIO()
    #code_img.save(buf,'jpeg')
    code_img.save(buf,'png')
    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET' :
        #code_str = gene_code()
        #session['code'] = code_str.lower()
        return render_template('login.html')
    else :
        users = request.form.to_dict()
        userinfo = select(users)
        if userinfo :
            print "+++" *10
            print "users:",users,type(users)
            if passwd_hash.check_password(userinfo,users) :
                if users.get('code').lower() ==  session.get('code') :
                    #del session['code']  render_template不会重新执行，code不能删除
                    session['uid'] = userinfo.get('uid')
                    #定义全局变量
                    #g.role = userinfo['role']
                    session['role'] = userinfo['role']
                    #31天内不需要登录
                    session.permanent = True
                    return redirect(url_for('index'))
                else :
                    err_info = "验证码错误"
                    return  render_template('login.html',err_info = err_info) 
            else :
                err_info = "passwd error"
                err_info = "密码错误"
                return  render_template('login.html',err_info = err_info) 
        else:
            err_info = "用户名不存在"         
            return  render_template('login.html', err_info = err_info)

@app.route('/regist/',methods = ['GET','POST'])
def regist():
    if request.method == 'GET' :
        #code_str = gene_code()
        #session['code'] = code_str.lower()
        return render_template('regist.html')
    else :
        users = request.form.to_dict()
        if users.get('passwd') == users.get('passwd1') :
            inputCode = users.pop('code') #删除字典里的pop并取出值
            if inputCode.lower() ==  session.get('code') :
                del users['passwd1']
                users = passwd_hash.set_password(users)
                if insert(users) :
                    return redirect('/login/')
                else :
                    err_info = "用户名已存在"
                    return render_template('regist.html',m = err_info )
            else :
                err_info = "验证码错误"
                return render_template('regist.html',m = err_info )
        else :
            m = "两次输入密码不一致"
            return render_template('regist.html',m = m )
        
@app.route('/article/',methods = ['GET','POST'])
@login_required  #需要先登录
def article():
    if request.method == 'GET' :
        return render_template('quest.html')
    else :
        articles = request.form.to_dict()
        articles['author_id']= session.get('uid')
        print articles
        insert_article(articles)
        return redirect(url_for('index'))

@app.route('/',methods=['GET','POST'])
@app.route('/index/',methods=['GET','POST'])
def index():
    if request.method == "POST" :
        search_texts = request.form.to_dict()
    else :
        search_texts = {'title':''}

    search_result = search_art(search_texts)
    if search_result :
        print search_result
        return render_template('index.html',search_title=search_texts.get('title'),search_result=search_result)
    else :
        return render_template('index.html',search_title=search_texts.get('title'))
        


@app.route('/logout/')
def logout() :
    #session.pop('uid')
    #del session('uid')
    session.clear()
    return redirect(url_for('index'))
