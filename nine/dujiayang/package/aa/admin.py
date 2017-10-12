from flask import render_template
from aa import app

@app.route('/admin/')
def admin():
	return "<h1>hello world</h1>"
