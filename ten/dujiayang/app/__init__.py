#/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect,session
import json

app = Flask(__name__)
app.secret_key="dsadfasfadsfasf"


import cmdb
import order
import user
