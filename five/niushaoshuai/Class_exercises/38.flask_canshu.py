#!/usr/bin/python
#coding:UTF-8
from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def index():
    username=request.args.get('name')
    userpass=request.args.get('age')
    print request.args
    return "welcom %s your age is %s" % (username,userpass)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
