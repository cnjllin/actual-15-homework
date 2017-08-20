from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

@app.route('/top',methods=['GET','POST'])
def top():
    if request.method == 'GET':
        return render_template('top.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
