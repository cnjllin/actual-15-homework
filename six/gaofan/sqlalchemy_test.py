#!/usr/bin/python
#conding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
user_attr =['id_num','user_name','user_pass','user_age',
            'user_sex','user_tel','user_role']

class User(db.Model):
    __tablename__ = 'user'
    id_num = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(20),nullable=False)
    user_pass = db.Column(db.String(50),nullable=False)
    user_age = db.Column(db.String(10))
    user_sex = db.Column(db.String(10))
    user_tel = db.Column(db.String(20))
    user_role = db.Column(db.Integer,nullable=False)

#add
def user_add(**kargs):
    user_info = User(**kargs)
    db.session.add(user_info)
    db.session.commit()

#query
def user_query(id_num):
    user_info = User.query.filter(User.id_num == id_num).first()
    return user_info

#update
def user_update(id_num,**kargs):
    user_get = user_query(id_num)
    for k,v in kargs.items():
        user_get.__setattr__(k,v)
    db.session.commit()

#delete
def user_delete(id_num):
    user_get = user_query(id_num)
    db.session.delete(user_get)
    db.session.commit()

#login
def user_login(name,password):
    user_info = User.query.filter(User.user_name == name).first()
    if user_info:
        if password == user_info.user_pass:
            result = "Welcome!"
        else:
            result = "Password error!"
    else:
        result = "Invalid username!"
    return result

#user_reg
def user_reg(user_dict):
    user_info_add = {i:"".join(user_dict[i]) for i in user_dict}
    user_name_check = User.query.filter(User.user_name ==
                                      user_info_add['user_name']).all()
    if user_name_check:
        result = "User exits!"
    else:
        if user_info_add['passwd1'] == user_info_add['passwd2']:
            user_info_add['user_pass'] = user_info_add['passwd1']
            del user_info_add['passwd1']
            del user_info_add['passwd2']
            user_add(**user_info_add)
            result = "sign up successfully!"
        else:
            result = "Password error!"
    return result

def update_user(id_num,user_dict):

    user_info_add = {i:"".join(user_dict[i]) for i in user_dict}
    user_name_check = User.query.filter(User.user_name ==
                                      user_info_add['user_name']).all()
    if len(user_name_check) > 1:
        result = "User exits!"
    else:
        if user_info_add['passwd1'] == user_info_add['passwd2']:
            user_info_add['user_pass'] = user_info_add['passwd1']
            del user_info_add['passwd1']
            del user_info_add['passwd2']
            user_update(id_num,**user_info_add)
            result = "update successfully!"
        else:
            result = "Password error!"
    return result
