#!/usr/bin/python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect,session
import json,hashlib

#import paramiko

import utils

app = Flask(__name__)
app.secret_key = 'adfagfagrehyrejutkyu'

import user
import idc
import util
import cabinet
import server
import jobadd
#import joblist
