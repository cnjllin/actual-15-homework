#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse

field = ['id','username','password','email','phone','role']

# 首页--用户资料
def index(request):
    return render(request,"index.html")

# 用户添加
def reg(request):
	    return render(request,'reg.html')

# 用户登录
def login(request):
    return render(request,"login.html")



# 用户列表
def userlist(request):
    return render(request,"userlist.html")


# 用户更新
def modify(request):
        return render(request,'update.html')


## 删除用户
#@app.route('/delete/')
#def deleteuser():
#     if not session:
#        return redirect("/login")
#     if request.method == 'GET':
#	uid = request.args.get('id','')
#        result = delete('user',uid)
#	return json.dumps(result)
#	return redirect('/userlist/')

