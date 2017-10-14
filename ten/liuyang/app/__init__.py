from flask import Flask

app = Flask(__name__)
app.secret_key="daf"

import cmdb,db,utils,config
