from flask import Flask

app = Flask(__name__)
app.secret_key = '2w3er5t67yh9fjnsx'

from app import user,idc,cabinet
