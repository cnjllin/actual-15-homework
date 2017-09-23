# Author: tailorYang
from flask import render_template,request,redirect,session
from app import app
import json,db,config,utils

@app.route('/idc/')
def idc():
    role = session['role']
    res = db.select('idc')
    idcs = [dict((v, idc[k]) for k, v in enumerate(config.idc_fields)) for idc in res]
    for i in range(len(idcs)):
        field = ['username','phone']
        user = {v:db.select('user',*field,id = idcs[i]['userid'])[0][k] for k,v in enumerate(field)}
        idcs[i] = dict(idcs[i],**user)
    return render_template("/idc/idclist.html",idcs = idcs,role = role)

@app.route('/idcadd/',methods=['post','get'])
def idcadd():
    if request.method == 'GET':
        res = db.select('user',*['id','username'])
        users = [dict((v, user[k]) for k, v in enumerate(['id','username'])) for user in res]
        return render_template('/idc/idcadd.html',users=users, info=session, role=session.get('role'))
    data = {k:v[0] for k,v in dict(request.form).items()}
    if db.add('idc',data):
        return json.dumps({'code':1,'result':'add idc success'})

@app.route('/idcupdate/',methods=['GET','POST'])
def idcupdate():
    if request.method == 'GET':
        res = db.select('user')
        users = [dict((v, user[k]) for k, v in enumerate(config.user_fields)) for user in res]
        id = request.args.get('id')
        idc = db.select('idc', id = id)[0]
        idc = {v: idc[k] for k, v in enumerate(config.idc_fields)}
        return json.dumps({'code':1,'idc': idc,'users':users})
    data = {k:v[0] for k, v in dict(request.form).items()}
    conditions = ["%s='%s'" % (k, v) for k, v in data.items()]
    db.update('idc', conditions, data['id'])
    return json.dumps({'code': 1, 'result': 'update completed!'})

@app.route('/idc_delete/',methods=['POST'])
def idc_delete():
    id = request.form.get('id')
    db.delete('idc',id)
    return json.dumps({'code':0,'result':'delete success!'})