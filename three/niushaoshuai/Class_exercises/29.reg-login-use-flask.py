#!/usr/bin/python
# -*- coding:UTF-8 -*-
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/reg/<string:name>/<string:passwd>/')
def reg(name,passwd):
    #print name
    f = open('user_message.db', 'a+')
    f.write("%s:%s \n" % (name,passwd))
    return "welcom %s" % (name)

@app.route('/')
def index():
    return render_template("tj.html")

@app.route('/1')
def index1():
    res="result"
    return render_template("tj.html",result=res)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
