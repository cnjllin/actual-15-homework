#!/usr/bin/python
#coding:UTF-8
from flask import Flask,render_template
app=Flask(__name__)

@app.route('/index')
def index():
    res='welcom nss'
    return render_template('tj.html',result=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
