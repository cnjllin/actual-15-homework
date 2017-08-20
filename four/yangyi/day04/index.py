# Author: tailorYang
from flask import Flask,render_template,request

app = Flask(__name__)
title = "TailorYang"
#网站首页
@app.route('/')
def index():
    return render_template('login.html',title = title)

#用户登录，登录成功返回用户名，失败返回 0
@app.route('/login',methods=['POST','GET'])
def login():
    user=request.form.get('user').lower()
    pwd=request.form.get('password')
    users = getuser()
    #判断用户名密码是否匹配
    if users.get(user) == pwd:
        result = user
    else:
        result = "0"
    return result

#用户注册
@app.route('/register',methods=['POST'])
def register():
    username = request.form.get("user").lower()
    pwd = request.form.get("password1")
    with open("user.txt","a+") as f:
        usermessage = f.write('%s:%s \n'%(username,pwd))
    if usermessage :
        result = username
    else:
        result = '0'
    return result

#获取所有用户名和密码
def getuser():
    users = {}
    try:
        with open("user.txt") as f:
            for k in f:
                k = k.strip("\n")
                users.setdefault(k.split(":")[0],k.split(":")[1].strip())
    except Exception as e:
            users= {}
    return users

#判断用户名密码是否存在
@app.route('/checkuser',methods=['POST'])
def checkuser():
    users = getuser()
    user = request.form.get('user').lower()
    if user in users.keys():
        result = "1"
    else:
        result = "0"
    return result

#登录成功进入用户中心
@app.route('/user/<username>')
def ucenter(username):
    user = username.split("=")[1]
    return render_template('user.html',user=user,title=title)
#统计IP出现次数
def countIP(count):
    statistics = {}
    last = []
    with open(r'access.txt', "r") as f:
        # for循环日志文件的每一行
        for i in f:
            # 判断字典中是否存在此ip 存在 value +=1 不存在 key = ip value =1
            if str(i).split(" ")[0] in statistics:
                statistics[str(i).split(" ")[0]] += 1
            else:
                statistics.setdefault(str(i).split(" ")[0], 1)
    # for循环字典反转key 与value的值并 append 至列表
    for k, v in statistics.items():
        last.append((v, k))
    result = sorted(last,reverse=True)[:count]
    return result
#展示出现次数最多的10 个IP
@app.route('/ip')
def IP():
    count = int(request.args.get('count'))
    user = request.args.get('user')
    TopTen = countIP(count)

    return render_template('ip.html',TopTen=TopTen,user=user,title=title,count=count)

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)