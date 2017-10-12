from flask import render_template
from aa import app


@app.route('/views/')
def views():
	return "<h1>hello view</h1>"
