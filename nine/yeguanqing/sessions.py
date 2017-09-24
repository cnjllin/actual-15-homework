#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import session
def sessioninfo():
    msg = {'username':session['username'],'role':session['role']}
    return msg

