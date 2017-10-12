#!/usr/bin/env python
#coding:utf8

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,getlist,update,delete
import json,util

app = Flask(__name__)
#app.secret_key=" 
