#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request,redirect,session
#from utils import insert,getone,select,update,delete
from db import insert,getone,update,select,delete
import json
app=Flask(__name__)
app.secret_key = 'askdmsakldalsdk'
filed = ['id','username','name','password','phone','mail','role','status']
filed1=['id','name','name_cn','address','adminer','phone']
filed2=['id','name','idc_id','u_num','power']
filed3=['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']

#---------------------------用户管理------------------------------------

# 首页
@app.route('/')
def index():
    return render_template('index.html')


# 注册
@app.route('/reg/',methods=['POST','GET'])
def reg():
    filed = ['id','username','name','password','phone','mail','role']
    if request.method == 'POST':
        users = {k:v[0] for k,v in dict(request.form).items()}
        result = insert('user',filed,users)
        if result['code']==0:
            return render_template('login.html',msg=result['msg'])
        return render_template('reg.html',msg=result['errmsg'])
    return render_template('reg.html',msg="")
    

# 登录
@app.route('/login/',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        info = {k:v[0] for k,v in dict(request.form).items()}
        result = getone('user',filed,info)
        if  result['code'] == 0:
             if result['msg']['password'] == info['password']:
                   session['username'] = info['username']
                   session['role'] = result['msg']['role']
                   session['id'] = result['msg']['id']
                   return json.dumps(result) 
             else:
                 result = {'errmsg':'passwd is error'}
                 return json.dumps(result)
        else:
             return json.dumps(result)
    return render_template('login.html')

# 用户个人主页
@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.args).items()}
    if info:
        users = getone('user',filed,info) 
    else:
        users = getone('user',filed,session)
    return render_template('userinfo.html',users=users['msg'])

#查询单个用户信息
@app.route('/selectone/')
def selectone():
    if not session:
        return redirect('/login/')
    data={k:v[0] for k,v in dict(request.args).items()}
    result=getone('user',filed,data)
    if result['code']==0:
        res=result['msg']
        return json.dumps(res)
    return json.dumps(result)

# 更新用户信息
@app.route('/update/',methods=['POST','GET'])
def update1():
      filed=['id','username','name','phone','mail']
      if not session:
          return redirect('/login/')
      if request.method == 'POST':
          data={k:v[0] for k,v in dict(request.form).items()}
          result = update('user',filed,data)
          if result['code']==0:
              return json.dumps(result)
          else:
              return json.dumps(result)
          return json.dumps(result)

# 修改个人密码
@app.route('/user/chpwdoneself',methods = ['POST','GET'])
def updatepassword():
     if not session:
         return redirect('/login/')  
     info = {k:v[0] for k,v in dict(request.form).items()}
     users=getone('user',filed,session)
     if info['oldpasswd'] == users['msg']['password']:
          file = ['id','password']
          data={}
          data['password']=info['newpasswd'] 
          data['id']=session['id']
          result=update('user',file,data)
          if result['code']==0:
              return json.dumps(result) 
          else:
              return json.dumps(result)
     else:
         result = {'errmsg':'password is error'}
         return json.dumps(result)

# 用户列表
@app.route('/userlist/')
def userlist():
    if not session:
        return redirect('/login/')
    result=select('user',filed)
    if result['code']==0:
        return render_template('userlist.html',users=session,res=result['msg'])        
    return render_template('userlist.html',users=session,res=result['errmsg'])        

# 删除用户
@app.route('/delete/',methods=['POST','GET'])
def deleteUser():
    if not session:
        return redirect('/login/')
    info={k:v[0] for k,v in dict(request.args).items()}
    result=delete('user',filed,info)
    if result['code']==0:
        return json.dumps(result)
    return json.dumps(result)

# 添加用户
@app.route('/adduser/',methods=['POST','GET'])
def adduser():
    filed = ['username','name','password','phone','mail','role','status']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        result=insert('user',filed,data)
        if result['code']==0:
            return json.dumps(result)
        return json.dumps(result)
    return render_template('adduser.html',users=session)

# 注销
@app.route('/logout/')
def logout():
    if session:
        session.clear()
    return redirect('/login/')



#----------------------机房管理------------------------------------
# 机房信心列表
@app.route('/idc/',methods=['POST','GET'])
def idc():
    if not session:
        return redirect('/login/')
    info={k:v[0] for k,v in dict(request.form).items()}
    res = select('idc',filed1)
    return render_template('idc.html',users=session,result=res['msg'])

# 编辑机房信息
@app.route('/updateidc/',methods=['POST','GET'])
def updateidc():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        info={k:v[0] for k,v in dict(request.args).items()}
        res=getone('idc',filed1,info)
        if res['code']==0:
            print res
            return json.dumps(res['msg'])
        print res
        return json.dumps(res)
    info={k:v[0] for k,v in dict(request.form).items()}    
    res=update('idc',filed1,info)
    if res['code']==0:
        return json.dumps(res)
    return json.dumps(res)

# 删除机房
@app.route('/idcdelete/',methods=['POST','GET'])
def idcdelete():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.form).items()}
    result=delete('idc',filed1,info)
    if result['code']==0:
        return json.dumps(result)
    return json.dumps(result)



# 添加机房
@app.route('/idcadd/',methods=['POST','GET'])
def idcadd():
    filed1=['name','name_cn','address','adminer','phone']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        info={k:v[0] for k,v in dict(request.form).items()}
        result = insert('idc',filed1,info)
        if result['code']==0:
             return json.dumps(result)
        return json.dumps(result)
    return render_template('idcadd.html',users=session)

#-------------------------------机柜管理---------------------------------------------------

# 机柜信息列表
@app.route('/cabinet/',methods=['POST','GET'])
def cabinet():
    if not session:
        return redirect('/login/')
    res = select('cabinet',filed2)
    return render_template('cabinet.html',users=session,result=res['msg'])


# 添加机柜
@app.route('/cabinetadd/',methods=['POST','GET'])
def cabinetadd():
    filed2=['name','idc_id','u_num','power']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        info={k:v[0] for k,v in dict(request.form).items()}
        result = insert('cabinet',filed2,info)
        if result['code']==0:
             return json.dumps(result)
        return json.dumps(result)
    return render_template('cabinetadd.html',users=session)


# 删除机柜
@app.route('/cabinetdelete/',methods=['POST','GET'])
def cabinetdelete():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.form).items()}
    result=delete('cabinet',filed2,info)
    return json.dumps(result)



# 编辑机柜信息
@app.route('/updatecabinet/',methods=['POST','GET'])
def updatecabinet():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        info={k:v[0] for k,v in dict(request.args).items()}
        res=getone('cabinet',filed2,info)
        if res['code']==0:
            return json.dumps(res['msg'])
        return json.dumps(res)
    info={k:v[0] for k,v in dict(request.form).items()}
    res=update('cabinet',filed2,info)
    if res['code']==0:
        return json.dumps(res)
    return json.dumps(res)

#-----------------------服务器管理--------------------------------------------

# 添加服务器
@app.route('/serveradd/',methods=['POST','GET'])
def serveradd():
    filed3=['hostname','lan_ip','wan_ip','cabinet_id','op','phone']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        info={k:v[0] for k,v in dict(request.form).items()}
        result = insert('server',filed3,info)
        if result['code']==0:
             return json.dumps(result)
        return json.dumps(result)
    return render_template('serveradd.html',users=session)


# 服务器信息列表
@app.route('/server/',methods=['POST','GET'])
def server():
    if not session:
        return redirect('/login/')
    res = select('server',filed3)
    return render_template('server.html',users=session,result=res['msg'])


# 编辑服务器信息
@app.route('/updateserver/',methods=['POST','GET'])
def updateserver():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        info={k:v[0] for k,v in dict(request.args).items()}
        res=getone('server',filed3,info)
        if res['code']==0:
            return json.dumps(res['msg'])
        return json.dumps(res)
    info={k:v[0] for k,v in dict(request.form).items()}
    res=update('server',filed3,info)
    if res['code']==0:
        return json.dumps(res)
    return json.dumps(res)



# 删除服务器
@app.route('/serverdelete/',methods=['POST','GET'])
def serverdelete():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.form).items()}
    result=delete('server',filed3,info)
    return json.dumps(result)





if __name__=='__main__':
    app.run(host='0.0.0.0',port=500,debug=True)
