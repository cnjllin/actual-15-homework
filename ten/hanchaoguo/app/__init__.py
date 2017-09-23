#!/usr/bin/python
#coding:utf-8
from flask import Flask

app=Flask(__name__)
import idc 
import cabinet 
import config 
import server 
import utils 
import user 
#import joblist
import job
import db
app.secret_key = 'askdmsakldalsdk'
