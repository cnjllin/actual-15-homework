#!/usr/bin/python
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect,session
import utils
import json
import datetime
test=Flask(__name__)
test.secret_key='sdfsfklsdlflfd'

filed=['id','username','password','role','email','phone','name']
update_filed=['id','username','name','email','phone']
insert_filed=['username','password','role','email','phone','name']
idc_filed=['id','idcname','idcname_cn','address','contact','phone']
insert_idc_filed=['idcname','idcname_cn','address','contact','phone']
cabinet_filed=['id','name','idc_id','u_num','power']
insert_cabinet_filed=['name','idc_id','u_num','power']
server_filed=['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
insert_server_filed=['hostname','lan_ip','wan_ip','cabinet_id','op','phone']

# Date 数据处理
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# 注册表单
@test.route('/add/',methods=['GET','POST'])
def add():
    if not session:
        return redirect("/login")
    if session['role']==0:
        if request.method == 'POST':
            user_info_dict=dict(request.form)
            user_data={ k:v[0] for k,v in user_info_dict.items() }
            if not utils.checkout_user_exist(user_data['name']) :
                res=utils.insert('user',insert_filed,user_data)
                return json.dumps(res)
        else:
            return render_template('add.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])
    else:    
        return render_template('index.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])

# 注册机房表单
@test.route('/idcadd/',methods=['GET','POST'])
def idcadd():
    if not session:
        return redirect("/login")
    if session['role']==0:
        if request.method == 'POST':
            user_info_dict=dict(request.form)
            user_data={ k:v[0] for k,v in user_info_dict.items() }
            res=utils.insert('idc',insert_idc_filed,user_data)
            return json.dumps(res)
        else:
            return render_template('idcadd.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])
    else:
        return render_template('index.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])

# 注册机柜表单
@test.route('/cabinetadd/',methods=['GET','POST'])
def cabinetadd():
    if not session:
        return redirect("/login")
    if session['role']==0:
        if request.method == 'POST':
            user_info_dict=dict(request.form)
            user_data={ k:v[0] for k,v in user_info_dict.items() }
            res=utils.insert('cabinet',insert_cabinet_filed,user_data)
            return json.dumps(res)
        else:
	    users=utils.list('idc',idc_filed)
            return render_template('cabinetadd.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'],msg=users['msg'])
    else:
        return render_template('index.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])


# 注册主机表单
@test.route('/serveradd/',methods=['GET','POST'])
def serveradd():
    if not session:
        return redirect("/login")
    if session['role']==0:
        if request.method == 'POST':
            user_info_dict=dict(request.form)
            user_data={ k:v[0] for k,v in user_info_dict.items() }
            res=utils.insert('server',insert_server_filed,user_data)
            return json.dumps(res)
        else:
            users=utils.list('cabinet',cabinet_filed)
            return render_template('serveradd.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'],msg=users['msg'])
    else:
        return render_template('index.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])


# 添加工单表单
@test.route('/jobadd/',methods=['GET','POST'])
def jobadd():
    if not session:
        return redirect("/login")
    
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
	user_data['apply_name']=session['name']
	addjob_field = ['apply_type','apply_name','apply_desc']
        res=utils.insert('job',addjob_field,user_data)
        return json.dumps(res)
    else:
        return render_template('jobadd.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])

# 会员中心-首页
@test.route('/userlist/')
def userlist():
    if not session:
        return redirect("/login")
    if session['role']==0:
        users=utils.list('user',filed)
        users1=json.dumps({'code':0,'users':users})
        if users['code'] == 0:
            return render_template('userlist.html',msg=users['msg'],user=session['username'],role=session['role'])
#            return json.dumps({'code':0,'users':users})
    else:
        return render_template('userlist.html',user=session['username'],role=session['role'])

# 机房管理
@test.route('/idc/')
def idc():
    if not session:
        return redirect("/login")
    users=utils.list('idc',idc_filed)
    users1=json.dumps({'code':0,'users':users})
    if users['code'] == 0:
        return render_template('idc.html',msg=users['msg'],user=session['username'],role=session['role'])
#       return json.dumps({'code':0,'users':users})
    else:
        return render_template('idc.html',user=session['username'],role=session['role'])

# 机柜管理
@test.route('/cabinet/')
def cabinet():
    if not session:
        return redirect("/login")
    users=utils.list('cabinet',cabinet_filed)
    users1=json.dumps({'code':0,'users':users})
    if users['code'] == 0:
        return render_template('cabinet.html',msg=users['msg'],user=session['username'],role=session['role'])
    else:
        return render_template('cabinet.html',user=session['username'],role=session['role'])

# 主机管理
@test.route('/server/')
def server():
    if not session:
        return redirect("/login")
    users=utils.list('server',server_filed)
    users1=json.dumps({'code':0,'users':users})
    if users['code'] == 0:
        return render_template('server.html',msg=users['msg'],user=session['username'],role=session['role'])
    else:
        return render_template('server.html',user=session['username'],role=session['role'])

# 订单管理
@test.route('/joblist/')
def joblist():
    if not session:
        return redirect("/login")
    job_field = ['id','apply_name','handle_name','apply_type','apply_desc','handle_desc','status','created','modified']
    users=utils.list('job',job_field)
    joblist=list()
    for x in users['msg']:
	if x['status'] < 2 :
           joblist.append(x)
		
    if users['code'] == 0:
        return render_template('joblist.html',msg=joblist,user=session['username'],role=session['role'])
    else:
        return render_template('joblist.html',user=session['username'],role=session['role'])

# 工单管理-历史工单
@test.route('/jobhistory/',methods=['GET', 'POST'])
def jobhistory():
    if not session:
        return redirect("/login")
    if request.method=='GET':
        job_field = ['id','apply_name','handle_name','apply_type','apply_desc','handle_desc','status','created','modified']
        users=utils.list('job',job_field)
    return render_template('jobhistory.html',msg=users['msg'],user=session['username'],role=session['role'])

# 个人用户-首页
@test.route('/userlist1/')
def userlist1():
    if not session:
        return redirect("/login")
    else:
        user_id=session['id']
        users=utils.getone('user',filed,user_id)
#        users1=json.dumps({'code':0,'users':users})
        if users['code'] == 0:
            return render_template('userlist.html',msg=users['msg'],user=users)

# 会员中心-删除模块
@test.route('/delete/',methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        user_id=request.form.get('id')
    else:
        user_id=request.args.get('id')
    res=utils.delete('user',user_id)
#    return redirect('/userlist/')
#    return render_template('userlist.html',user=session['username'],role=session['role'])
    return json.dumps(res)

# 机房管理-删除模块
@test.route('/idcdelete/',methods=['GET','POST'])
def idcdelete():
    if request.method == 'POST':
        user_id=request.form.get('id')
    else:
        user_id=request.args.get('id')
    res=utils.delete('idc',user_id)
#    return redirect('/userlist/')
#    return render_template('idc.html',user=session['username'],role=session['role'])
    return json.dumps(res)

# 机柜管理-删除模块
@test.route('/cabinetdelete',methods=['GET','POST'])
def cabinetdelete():
    if request.method == 'POST':
        user_id=request.form.get('id')
    else:
        user_id=request.args.get('id')
    res=utils.delete('cabinet',user_id)
#    return redirect('/userlist/')
#    return render_template('idc.html',user=session['username'],role=session['role'])
    return json.dumps(res)

# 主机管理-删除模块
@test.route('/serverdelete',methods=['GET','POST'])
def serverdelete():
    if request.method == 'POST':
        user_id=request.form.get('id')
    else:
        user_id=request.args.get('id')
    res=utils.delete('server',user_id)
#    return redirect('/userlist/')
#    return render_template('idc.html',user=session['username'],role=session['role'])
    return json.dumps(res)


# 会员中心-更新模块
@test.route('/update',methods=['GET','POST'])
def update():    
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user=utils.update('user',user_data) 
        users=json.dumps(user)
        return json.dumps(user)

    else:
        user_id=request.args.get('id')
        data=dict()
        data['id']=user_id
        user=utils.getone('user',filed,data)
        if user['code'] == 0:
            return json.dumps(user['msg'])

# 机房管理-更新模块
@test.route('/idcupdate',methods=['GET','POST'])
def idcupdate():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user=utils.update('idc',user_data)
        users=json.dumps(user)
        return json.dumps(user)

    else:
        user_id=request.args.get('id')
        data=dict()
        data['id']=user_id
        user=utils.getone('idc',idc_filed,data)
        if user['code'] == 0:
            return render_template('idcupdate.html',msg=user['msg'],user=session['username'],role=session['role'])

# 机柜管理-更新模块
@test.route('/cabinetupdate/',methods=['GET','POST'])
def cabinetupdate():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user=utils.update('cabinet',user_data)
        users=json.dumps(user)
        return json.dumps(user)

    else:
        user_id=request.args.get('id')
        data=dict()
        data['id']=user_id
        user=utils.getone('cabinet',cabinet_filed,data)
        users=utils.list('idc',idc_filed)
        if user['code'] == 0:
            return render_template('cabinetupdate.html',msg=user['msg'],user=session['username'],role=session['role'],msg_idc=users['msg'])

# 主机管理-更新模块
@test.route('/serverupdate/',methods=['GET','POST'])
def serverupdate():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user=utils.update('server',user_data)
        users=json.dumps(user)
        return json.dumps(user)

    else:
        user_id=request.args.get('id')
        data=dict()
        data['id']=user_id
        user=utils.getone('server',server_filed,data)
        users=utils.list('cabinet',cabinet_filed)
        if user['code'] == 0:
            return render_template('serverupdate.html',msg=user['msg'],user=session['username'],role=session['role'],msg_cabinet=users['msg'])

# 工单管理-更新模块
@test.route('/jobupdate/',methods=['GET','POST'])
def jobupdate():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user_data['handle_name']=session['name']
	user_data['status']=2
        user=utils.update('job',user_data)
        if  user['code'] == 0:
            return  json.dumps(user)
    else:
        user_info_dict=dict(request.args)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
	user_data['handle_name']=session['name']
	user_data['status']=1
        user=utils.update('job',user_data)
        if  user['code'] == 0:
            return  json.dumps(user)

# 会员中心-更新密码
@test.route('/user/chpwdoneself',methods=['GET','POST'])
def update_chpwdone():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user=utils.update_passwd('user',session['id'],user_info_dict)
        users=json.dumps(user)
        return users
# 登陆模块
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user_all=utils.getone('user',filed,user_data) 
        if user_all['code'] == 0 and utils.checkout_user_pass(user_data['username'],user_data['password']):
            session['id']=user_all['msg']['id']
            session['username']=user_all['msg']['username']
            session['name']=user_all['msg']['name']
            session['email']=user_all['msg']['email']
            session['phone']=user_all['msg']['phone']
            session['role']=user_all['msg']['role']
            return redirect('/')
        else:
            return render_template('login.html',error='username or password is error')
        
    return render_template('login.html')

# 个人中心
@test.route('/userinfo')
def userinfo():
    if not session:
        return redirect("/login")
    user_id=request.args.get('id')
    data=dict()
    data['id']=user_id
    user=utils.getone('user',filed,data)
    return render_template('userinfo.html',id=user_id,user=session['username'],user1=user['msg']['username'],user_cn=user['msg']['name'],email=user['msg']['email'],phone=user['msg']['phone'],role1=user['msg']['role'],role=session['role'])

# 工单详情
@test.route('/jobdetail/')
def jobdetail():
    if not session:
        return redirect("/login")
    job_field=['id','apply_name','handle_name','apply_type','apply_desc','handle_desc','status','created','modified']
    user_id=request.args.get('id')
    data=dict()
    data['id']=user_id
    user=utils.getone('job',job_field,data)
    if  user['code'] == 0:
        return  json.dumps(user,cls=DatetimeEncoder)

# 登出
@test.route('/logout/')
def logout():
    session.clear()
    return redirect("/login")


# 首页
@test.route('/')
def index():
    if not session:
        return redirect("/login")
    else:
        return render_template('index.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])

# 测试母版
@test.route('/base/')
def base():
    return render_template("base.html")

if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
