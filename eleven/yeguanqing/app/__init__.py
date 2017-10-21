#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect,session
import json
import paramiko

app = Flask(__name__)
app.secret_key = "dfafdkadfkakdfkasdfkdfkdasf"

import login
import user
import userlist
import idc
import cabinet
import server
import job
import ansible_ye
