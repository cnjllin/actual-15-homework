#coding:utf-8
from flask import Flask,request,render_template,redirect

app = Flask(__name__)


# @app.route('/submit/')
# def submit():
#     return render_template("submit.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        user01 = request.form.get('user','')
        pwd = request.form.get('pwd','')
        if len(user01) == 0 or len(pwd) == 0:
            return "username or password is null"
    with open('E:\\fl_test\\zhuce.log','a+') as f1:
        f1.write(user01+':'+pwd+'\n')
    return redirect('/userlist')

@app.route('/userlist')
def userlist():
    userlist = []
    with open('E:\\fl_test\\zhuce.log') as f2:
        for l in f2:
            userlist.append(l.split(':'))
        return render_template('userlist.html',userxxx=userlist)



@app.route('/login/', methods=['GET'])
def submit():
     return render_template('submit.html')

@app.route('/login/submit', methods=['POST'])
def login():
    with open('E:\\fl_test\\zhuce.log', 'r')as f:
        user = request.form.get('username','')
        passwd = request.form.get('password','')
        x = {}
        Username = []

        for line in f.readlines():
            x[line.strip().split(":")[0]] = line.strip().split(":")[1]

        for i in x:
            Username.append(i)

        if user in Username:
            if passwd == x.get(user):
                choice = '1'
            else:
                choice = '0'
        else:
            choice = '2'
    return render_template('login.html', choice=choice,user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
