# Author: tailorYang
from flask import render_template,request,redirect,session
from app import app
import json,db,config,utils

@app.route('/cabinet/')
def cabinet():
    role = session.get('role')
    res = db.select('cabinet')
    cabinets = [dict((v, idc[k]) for k, v in enumerate(config.cabinet_fields)) for idc in res]
    for i in range(len(cabinets)):
        field = ['name_cn']
        name = {v:db.select('idc',*['name_cn'],id = cabinets[i]['idc_id'])[0][k] for k,v in enumerate(['name_cn'])}
        cabinets[i] = dict(cabinets[i],**name)
    return render_template("/cabinet/cabinetlist.html",cabinets = cabinets,role = role)

@app.route("/cabinetadd/",methods=['GET','POST'])
def cabinetadd():
    if request.method == 'GET':
        res = db.select('idc')
        idcs = [dict((v,idc[k]) for k,v in enumerate(config.idc_fields)) for idc in res]
        return render_template('/cabinet/cabinetadd.html',idcs=idcs,role = session.get('role'))
    data = {k: v[0] for k, v in dict(request.form).items() }
    res = db.select('cabinet',name=data['name'])
    if res:
        return json.dumps({'code': 0, 'result': 'add cabinet name already exist'})
    db.add('cabinet', data)
    return json.dumps({'code': 1, 'result': 'add cabinet success'})

@app.route('/cabinet_update/',methods=['GET','POST'])
def cabinet_update():
    if request.method == 'GET':
        res = db.select('idc')
        idcs = [dict((v, idc[k]) for k, v in enumerate(config.idc_fields)) for idc in res]
        id = request.args.get('id')
        cabinet = db.select('cabinet', id=id)[0]
        cabinet = {v: cabinet[k] for k, v in enumerate(config.cabinet_fields)}
        return json.dumps({'code': 1, 'idcs': idcs, 'cabinet': cabinet})
    data = {k: v[0] for k, v in dict(request.form).items()}
    conditions = ["%s='%s'" % (k, v) for k, v in data.items()]
    if db.update('cabinet', conditions, data['id']) > 0:
        return json.dumps({'code': 1, 'result': 'update completed!'})

@app.route('/cabinet_delete/',methods=['POST'])
def cabinet_delete():
    id = request.form.get('id')
    db.delete('idc',id)
    return json.dumps({'code':0,'result':'delete success!'})
