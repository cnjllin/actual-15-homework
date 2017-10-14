#  作业
###  扒页面

###  static目录没有上传

# 目录结构

<pre>

├── app
│   ├── cmdb.py            # 资产管理
│   ├── job.py            # 工单系统
│   ├── __init__.py
│   ├── static             # 静态文件
│   │   ├── css
│   │   ├── img
│   │   ├── js
│   │   └── pulgin
│   ├── templates                # html目录
│   │   ├── add.html             # 添加用户
│   │   ├── base.html            #  模板 
│   │   ├── cabinet.html          # 机柜列表
│   │   ├── cabinet_update.html   # 更新机柜
│   │   ├── idc_add.html          # 添加机房
│   │   ├── idc.html               # 机房列表
│   │   ├── index.html             # 主页面
│   │   ├── list.html              #  用户主界面
│   │   ├── login.html             #  登录界面
│   │   ├── reg.html               # 注册界面
│   │   ├── server.html            # 服务器列表
│   │   ├── server_update.html     # 服务器更新
│   │   ├── log.html               # 饼状图
│   │   ├── map.html                # 地图
│   │   ├── job_add.html            # 添加工单
│   │   ├── jobhistory.html         # 工单历史
│   │   ├── joblist.html            # 工单列表
│   │   └── userlist.html           # 用户列表
│   ├── user.py              # 用户权限模块
│   └── log.py                # 可视化
├── config.py                 # 数据库配置模块
├── run.py                    # 入口         
├── util.py                   # 日志模块
├── utils.py                  # 功能模块





</pre>


# 测试结果


## 日志

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/日志.png)

# 用户权限

## 用户列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/用户列表.png)

## 用户添加

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/用户添加.png)

## 用户编辑

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/用户编辑.png)

# 资产管理CMDB

## 机房列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/机房列表.png)

## 机房添加

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/机房添加.png)

## 机房编辑

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/机房编辑.png)

## 机柜列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/机柜列表.png)

## 机柜添加

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/添加机柜.png)

## 机柜编辑

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/机柜编辑.png)


## 服务器列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/服务器列表.png)

## 服务器添加

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/服务器添加.png)

## 服务器编辑

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/nine/liukai/test/服务器编辑.png)

## 工单添加

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/ten/liukai/test/%E2%95%94%D1%8A%E2%95%9F%D1%8B%E2%95%A3%D0%B4%E2%95%A1%D0%B5.png)

## 工单列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/ten/liukai/test/%E2%95%A3%D0%B4%E2%95%A1%D0%B5%E2%94%B4%E2%95%A8%E2%96%92%D1%8D.png)

## 申请工单详情

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/ten/liukai/test/%E2%95%A3%D0%B4%E2%95%A1%D0%B5%E2%95%94%D1%8A%E2%95%9F%D1%8B%E2%95%A7%D1%8A%E2%95%9F%D1%89.png)

## 工单历史

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/ten/liukai/test/%E2%94%94%C2%B7%E2%95%A9%E2%95%96%E2%95%A3%D0%B4%E2%95%A1%D0%B5.png）

## 日志饼状图

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/ten/liukai/test/%E2%96%92%C2%A4%E2%95%AB%E2%94%A4%E2%95%90%E2%95%9D.png）

# 项目文档

## 需求分析：

> 用户权限管理系统

## 功能模块

### 首页

V: index.html

	1. reg/login两个导航按钮，会连接到登录注册模块
	2. 欢迎信息：wlcome {{username }}
C端
<pre>
@app.route('/') 
@app.route('/index/')
def index():
    username="wd"
    return render_template("index.html",username=username)
</pre>

### 注册页面
V端：reg.html
<pre>
  <\form atction"/reg/",method="POST">
    用户名，密码，角色
  <\/form>
</pre>   
 
C端：
<pre>
@app.route("/reg/",methods=['GET','POST'])
def reg():
    if  method为POST：
        username=request.form.get('username','')
		.........
        if  判断用户是否存在
            如果存在则返回错误信息render_template("reg.html",error=error)
        else:
            sql
            return rediret("跳转到登录页面")
    return render_tempalte("reg.html")
</pre>  

M端:user
<pre>
 mysql> CREATE TABLE `user` (
 ->   `id` int(100) NOT NULL AUTO_INCREMENT,
 ->   `username` varchar(100) NOT NULL,
 ->   `password` varchar(100) NOT NULL,
 ->   `role` int(10) NOT NULL,
 ->   PRIMARY KEY (`id`)
 -> )  DEFAULT CHARSET=utf8;

select * from user where username=username
insert into user () values()
</pre>

#### 登录页面
V端: login.html
<pre>
    <\form atction '/login/',method="POST">
        用户名，密码
    <\/form>
</pre>

C端:
<pre>
@app.route("/login/",methods=["GET","POST"]
def login():
    if method为post：
       username=request.form.get("username"," ")
       password=request.form.get("password"," ")
       if 判断用户是存在并且密码正确：
             if role==1:
                user_dict=查询所有用户信息,并转换为字典
                return render_template("user_list.html",user_dict=user_idct,usaername=username,role=role)
             else:
                user=按用户名查询单用户信息
                return render_template("user.html",user=user)
       
       else：
           msg=用户或密码错误
           return redicet("/login/?msg='用户名或密码错误'")
    return render_tempalte("login.html")
</pre> 

M端:  
<pre>
查所用户信息 sql=" select * from user"
按username 查单用户信息 sql= "select * from user where username=%s"%username
</pre>

## 管理页面/用户列表
    
### 管理员界面    
V端: 
<pre>
1. 左部分 ----><font color=red>显示管理员功能/普通用户更能</font>

2. 右部分 
list.html （右边一个表格显示所有用户信息） 
id ，用户名 ，密码， 权限 ，操作（删除，修改） 
{% for i in user_dict %}                                
  {{ user_dict.id}} ,{{user_dict.username}},{{user_idct.password}},{{user_dict.role}}<\a href="/delete/?id={{user_dict.id }}">删除</a><\a href="/update/?id={{}user_dict.id}">修改</id>
{% endfor %}
</pre>        
     
C端：
<pre>
@app.route("/delete/")
def delete():
    id=request.args.get("id"," ")
        执行删除函数
    return render_tempalte("user_list.html")
</pre>

M端: 
<pre>
sql="delete from user where id=%s"%id
</pre>

### 删除界面
V端： 在list.html上有个按钮，删除后直接跳到登录界面

C端： 获取前端id，根据执行删除sql，然后跳转到login.html

M端： sql="delete from %s where id =%s"%(table,uid)

### 更新页面
V端: update.html

   显示一个表格(名称 ，信息) ,信息内容可改，最下方有个提交按钮（跳转到管理员页面）
                                            
C端:
<pre>
@app.route("/update/")
def update():
    user=执行查询单用户sql，
        return  render_tempalte('update.html'user=user)

@app.route("/update/")
    获取修改的数据
    执行update sql 更改数据库
            
    return render_template("跳转登录界面")
       
  普通用户同上 
</pre>  

M端：
<pre>
  sql="select * from user where id=%s"%id
  
  sql="update user set password='%s',sex=%d,age=%d,phone=%d,email='%s',role=%d where id=%d"%(my_tup[0],my_tup[1],my_tup    
</pre>       

# cdmd 资产管理 

## 机房列表

V端: idc.html  
     <pre>
     显示一个表格（编号，机房名，地址，中文名， 联系人，电话 ，操作）操作里有两个按钮（编辑，删除）表格上方有添加按钮
     点击添加,弹出模态窗，添加机房信息
     点击编辑按钮，跳转到界面，idc_uptdae.html
     点击删除按照，直接执行删除sql
     
     idc_update.html
     点击编辑按钮 ,跳转到idc_update.html，获取id.执行utils.getone。渲染信息
     修改信息。然后点击更新，执行util.update.
     </pre>
     
 C端：
 <pre>
 @app.route('/idc/')
 def idc()：
       查所有机房，
       return render_template("渲染信息")
   
  @app.route("/idc_getone")
  def idc_getone():
      date=utils.getone(idc_table,filed,data)
      return render_template(‘渲染信息')
   
 @app.route('/idc_update/'） 
 def idc_update():
     date=utils.update()
     return json.dumps(data)
   </pre> 
 
 M端：
   <pre> 
    查idc表
    执行util.select(idc_table,idc_field,data)
    
    查单idc信息
    util.getone(idc_table,idc_field,data)
    
    #更新
    utils.update(idc_table,idc_field,data)
    </pre>
