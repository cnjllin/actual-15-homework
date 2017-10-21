#!/usr/bin/env python
# _*_coding:utf-8_*_

from flask import Flask,request,render_template,redirect,session
import json
from utile  import insert,list,delete,getone,update
import util

app = Flask(__name__)
app.secret_key="2134j1kjsdjfadsfl"


import user
import userlist
import login
import cabinet
import server
import idc
import job
import ansible


