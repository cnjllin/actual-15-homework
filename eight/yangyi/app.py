from flask import Flask ,render_template,redirect,session,request
import json,utils

app = Flask(__name__)
app.secret_key = 'ddrre567hygtre8ng6'
user_fields = ['id','username','password','role','phone','job']
idc_fields = ['id','name','name_cn','address','userid']
@app.route('/')
@app.route('/index/')
def index():
    if 'username' in session:
        role = session.get('role')
        return render_template('index.html',role=role)
    return render_template('login.html')

@app.route('/login/',methods=['post','get'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = {k:v[0] for k,v in dict(request.form).items()}
    if user.get('username') and user.get('password'):
        result = utils.select_one('user',user_fields,**user)['result']
        if result:
            session['role'] = result[0]['role']
            session['id'] = result[0]['id']
            session['username'] = result[0]['username']
            return json.dumps({'code': '1', 'result': 'login success'})
        else:
            return json.dumps({'code': '0', 'result': 'name or password wrong'})
    else:
        return json.dumps({'code':'0','result':'username or password not be null'})

@app.route('/useradd/',methods=['post','get'])
def useradd():
    if request.method == 'GET':
        return render_template('add.html',role = session.get('role'))
    data = {k:v[0] for k,v in dict(request.form).items()}
    if utils.add('user',data):
        return json.dumps({'code':1,'result':'add user success'})


@app.route('/userinfo/')
def userinfo():
    if request.args.get('id'):
        user = utils.select_one('user', user_fields,id=request.args.get('id') )
        return json.dumps({'result':user['result'][0]})
    else:
        role = session.get('role')
        user = utils.select_one('user', user_fields, **session)
        if user['code']:
            res = user['result'][0]
            return render_template("userinfo.html", user = res, role=role)

@app.route('/userlist/')
def userlist():
    role = session.get('role')
    if role:
        users = utils.select_one('user', user_fields)
        return render_template("userlist.html", users=users['result'], role=role)
    else:
        user = utils.select_one('user', user_fields, session.get('id'))
        return render_template("userinfo.html", user=user[0], role=role)

@app.route('/update/',methods=['GET','POST'])
def update():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    if data.get('newpassword'):
        conditions = ["password='%s'"% data.get('newpassword')]
    else:
        conditions = [ "%s='%s'" %  (k,v) for k,v in data.items() if v !='id']
    utils.update('user',conditions,data['id'])
    session['role'] = data['role']
    return json.dumps({'code':1,'result':'update completed!'})

@app.route('/delete/',methods=['post'])
def delete():
    utils.delete('user',request.form.get('id'))
    return json.dumps({'code': 1, 'result': 'delete success!'})

@app.route('/idc/')
def idc():
    role = session.get('role')
    idcs = utils.select_one('idc',idc_fields)['result']
    user = utils.select_one('user',['username','phone'],id=idcs[0]['userid'])['result']
    idcs=[dict(k,**v) for k in idcs for v in user]
    print(idcs)
    return render_template("idclist.html",idcs = idcs,role = role)

@app.route('/idcadd/',methods=['post','get'])
def idcadd():
    if request.method == 'GET':
        users = utils.select_one('user', user_fields)['result']
        return render_template('idcadd.html',users=users, info=session, role=session.get('role'))
    data = {k:v[0] for k,v in dict(request.form).items()}
    if utils.add('idc',data):
        return json.dumps({'code':1,'result':'add user success'})
@app.route('/logout/')
def loginout():
    if session:
        session.pop('role')
        session.pop('username')
        session.pop('id')
    return redirect('/login/')

if __name__ == "__main__":
    app.run(debug=True)