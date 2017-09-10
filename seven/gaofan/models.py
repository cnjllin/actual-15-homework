#!/usr/bin/python
#coding:utf-8

from exts import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer,autoincrement = True,primary_key = True)
    user_name = db.Column(db.String(20),nullable = False,unique = True)
    user_pass = db.Column(db.String(50),nullable = False)
    user_sex = db.Column(db.String(10))
    user_age = db.Column(db.Integer)
    user_email = db.Column(db.String(50))
    user_role = db.Column(db.Integer)

    def __repr__(self):
        return "<User %r,%r,%r,%r>" % (self.user_id,self.user_name,
                                    self.user_email,self.user_role)
