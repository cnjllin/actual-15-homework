### 需求分析

> 用户权限管理系统

#### 功能模块

##### 首页

V: index.html
    1. reg/login两个导航按钮，链接到登录注册模块
    2. 欢迎信息：welcome {{username}}

C: @app.route("/")
   @app.route("/index")
   def index():
       username = "xerxes"
       return render_template("index.html",username=username)

##### 注册页面
V:  reg.html
    <form action="/reg/",method="post">
        用户名，密码
    </form>

C:  @app.route("/reg/",methods=["GET","POST"])
    def reg():
        if method == post:
            username = request.form.get('username','')
            if 用户存在:
                返回错误信息render_template("reg.html",error=error)
            else:
                sql
                return redirect("登录页面")
        return render_template("reg.html")

M:  user
    select * from user where username=username
    insert into user () values ()

##### 登录页面
V:  login.html
    <form action="/login/",method="post">
        username
        password
    </form>

C:  @app.route("/login/",methods=['GET''POST])
    def login():
        if request.method == 'POST':
            user = request.form
            res = getone('user',field,user)
            if res['code'] == 0:
                pass
            else:
                pass
        return render_template("login.html")

M:  def getone(table,field,user):
        sql = 'select *from user where username="xerxes"'
        res = cur.execute(sql)
        if res:
            result = {}
        else:
            result = {}
        return result

##### 管理页面／用户列表
V: userlist.html
    <table>
    {% for user in result %}
        <td>{{user['username']}}</td>
        <td>{{user.password}}</td>
        {% endfor %}
    </table>

C: @app.route("/userlist")
    def userlist():
        result = list('user',field)
        if result['code'] == 0:
            result = result['msg']
        return tender_template("userlist.html",result=result)

M: sql = select * from user
   cur.execute(sql)
   res = cur.fetchall()
   for row in res:
        print row
    if res:
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'errormsg':'data is null'}
    return result

##### 用户更新
V: update.html
    <form action="/update",method='post'>
        <input type="hidden" value="{{result.id}}" name="id">
        username: <input type="text" value="{{result.username}}" name="username"><br>
        password: <input type="text" value="{{result.password}}" name="password"><br>
        <input type="submit" value="更新"><br>
    </form>

C: @app.route("/update",methods=['POST','GET'])
    def modity():
        if request.method == 'POST':
            data = dict(request.form)
            data = {k:v[0] for k,v in data.items()}
            result = update('user',field,data)
            if result['code']==0:
                return redirect('/userlist/')
            else:
                return render_template("update.html",result=result)
        else:
            uid = request.args.get("id","")
            data = {'id':uid}
            result = getone('user',field,data)
            if result['code'] == 0:
                result = result['msg']
            return render_template("update.html",result=result)

M: conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = 'update %s set %s where id="%s"' % (table,','.join(conditions),data['id'])
    print sql
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'msg':'wrong'}
    return result

##### 删除用户
C: @app.route("/del/",methods=['GET','POST'])
    def deluser():
        if request.method == 'GET':
            userid = request.args.get('id')
            del_user(userid)
            return redirect('/userlist/')

M: sql = 'delete from user where id=%d' % int(userid)








