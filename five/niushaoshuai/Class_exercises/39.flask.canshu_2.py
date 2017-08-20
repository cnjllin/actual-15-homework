#!/usr/bin/python
#coding:UTF-8
from flask import Flask
app=Flask(__name__)

@app.route('/<string:name>/<string:passwd>')
def index(name,passwd):
    username=name
    userpass=passwd
    return "welcom %s,your pass is %s" % (username,userpass)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
