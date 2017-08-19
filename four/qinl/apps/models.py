#coding: utf-8
from apps import db

class Users(db.Model):
    __tablename__ = 'users'

    '''
    primary_key=True 主键
    unique=True:表示不允许重复

    '''

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(150))
    date = db.Column(db.DateTime)

    def is_active(self):
        return True

    def get_id(self):
        return self.id


class Nginxlog(db.Model):
    __tablename__ = 'nginxlog'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255))
    url = db.Column(db.String(3000))
    status = db.Column(db.String(255))
    counts = db.Column(db.String(255))

'''
>cd flaskr
>python

>>> from apps import db
>>> from apps.models import Users
>>> db.create_all()

>>> user = Users(email='qinl@163.com', username='qinl', password='yutian', date=datetime.now())
>>> db.session.add(user)
>>> db.session.commit()
'''