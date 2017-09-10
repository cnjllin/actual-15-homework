#!/usr/bin/python
#coding:utf-8

from models import User
from exts import db

def user_add(**kargs):
    user_new = User(**kargs)
    db.session.add(user_new)
    db.session.commit()


def user_get(**kargs):
    if kargs.get('user_id'):
        id = kargs['user_id']
        user_info = User.query.filter(User.user_id == id).first()
    else:
        name = kargs.get('user_name')
        user_info = User.query.filter(User.user_name == name).first()
    return user_info

def user_all():
    users_info = User.query.all()
    return users_info

def user_delete(user_id):
    user_info = user_get(user_id=user_id)
    db.session.delete(user_info)
    db.session.commit()


def user_update(user_id,**kargs):
    user_info = user_get(user_id=user_id)
    for k,v in kargs.items():
        user_info.__setattr__(k,v)
    db.session.commit()

def user_check(user_name):
    user_info = User.query.filter(User.user_name == user_name).first()
    if not user_info:
        return True
    else:
        return False

def user_dict(request_form):
    user_dict = dict(request_form)
    user_info = {k:"".join(v) for k,v in user_dict.items()}
    return user_info

def passwd_check(user_info):
    if user_info['passwd1'] == user_info['passwd2']:
        user_info['user_pass'] = user_info['passwd1']
        del user_info['passwd1']
        del user_info['passwd2']
        return True
    else:
        return False
