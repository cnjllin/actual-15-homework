# coding:utf-8

from flask import Flask,render_template,request,redirect
import utils

app=Flask(__name__)


User='user'
user_list=['id','username','password','role']


# 首页
@app.route('/')
@app.route('/index/')
def index():
    username=""
    return render_template("index.html",username=username)






# 登录首页
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        user=utils.get_name(User,user_list,user_dict['username'])
        if  user  and  user_dict['password'] in user :
           res=dict(zip(User,user))
           result=utils.list(User,user_list)
           return render_template("list.html",result=result,res=res)
        else:
           result={'code':1,'msg':'username or password  is error'}
           return render_template("login.html",result=result)
    result={}
    return render_template("login.html",result=result)






#注册页面
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        user=utils.get_name(User,user_list,user_dict['username'])
        if  user:
           result={'code':1,'msg':'username is already'} 
           return render_template("reg.html",result=result)
        else:
           utils.insert(User,user_dict)
           result={'code':1,'msg':' register success'}
           return redirect("/login/")
    result={} 
    return render_template("reg.html",result=result)
      


# 删除 
@app.route('/delete/',methods=['GET','POST'])
def delete():
    uid=request.args.get('id')
    print uid,table
    utils.delete(User,uid)
    return redirect('/login/')

# 更新界面
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
     uid=request.args.get('id')
     result=utils.get_one(User,user_list,uid)
     print result
     return render_template("update.html",result=result)

# 刷新
@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       utils.update(User,user_list,user_dict)
       return  redirect("login")


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)

