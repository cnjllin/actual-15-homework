# Author: tailorYang
from flask import render_template,request,redirect,session
from app import app
import config
import  utils
import json
import db

@app.route('/server/')
def server():
    role = session.get('role')
    res = db.select('server')
    servers = [dict((v,server[k]) for k,v in enumerate(config.server_fields)) for server in res]
    for i in range(len(servers)):
        cabinet = {v:db.select('cabinet',*['name'],id = servers[i]['cabinet_id'])[0][k] for k,v in enumerate(['name'])}
        user = {v:db.select('user',*['username','phone'],id = servers[i]['user_id'])[0][k] for k,v in enumerate(['username','phone'])}
        servers[i] = dict(servers[i],**cabinet)
        servers[i] = dict(servers[i],**user)
    print(servers)
    return render_template("/server/serverlist.html",servers = servers,role = role)

@app.route("/serveradd/",methods=['GET','POST'])
def serveradd():
    if request.method == 'GET':
        res = db.select('cabinet')
        cabinets = [dict((v,idc[k]) for k,v in enumerate(config.idc_fields)) for idc in res]
        resb = db.select('user')
        users = [dict((v,user[k]) for k,v in enumerate(config.user_fields)) for user in resb]
        return render_template('/server/serveradd.html',cabinets=cabinets,users=users,role = session.get('role'))
    data = {k: v[0] for k, v in dict(request.form).items() }
    res = db.select('server',hostname=data['hostname'])
    if res:
        return json.dumps({'code': 0, 'result': 'add cabinet name already exist'})
    db.add('server', data)
    return json.dumps({'code': 1, 'result': 'add cabinet success'})

@app.route('/server_update/',methods=['GET','POST'])
def server_update():
    if request.method == 'GET':
        res = db.select('cabinet')
        cabinets = [dict((v, cabinet[k]) for k, v in enumerate(config.cabinet_fields)) for cabinet in res]
        resb = db.select('user')
        users = [dict((v, user[k]) for k, v in enumerate(config.user_fields)) for user in resb]
        id = request.args.get('id')
        server = db.select('server ', id=id)[0]
        server = {v: server[k] for k, v in enumerate(config.server_fields)}
        return json.dumps({'code': 1, 'server': server, 'cabinets': cabinets,'users':users})
    data = {k: v[0] for k, v in dict(request.form).items()}
    conditions = ["%s='%s'" % (k, v) for k, v in data.items()]
    if db.update('server', conditions, data['id']) > 0:
        return json.dumps({'code': 1, 'result': 'update completed!'})

@app.route('/server_delete/',methods=['POST'])
def server_delete():
    id = request.form.get('id')
    db.delete('server',id)
    return json.dumps({'code':0,'result':'delete success!'})