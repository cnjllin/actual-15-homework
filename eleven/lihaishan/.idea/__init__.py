
# __*__coding:utf-8__*__

from flask import Flask,request,render_template,redirect,session
import json
import utils
import util


app = Flask(__name__)
app.secret_key="2134j1kjsdjfadsfl"

import login
import user
import CMDB
import job