from apps import app
import db

def login():
    name = "qinl"
    d = {}
    for i in db.query('users',app.config.get('FIELDS')):
        d[i['name']] = [i['password'],i['role'],i['id'],i['status']]
    if not name:
        print name







