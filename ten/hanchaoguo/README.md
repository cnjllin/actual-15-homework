## 项目文档
写一套运维管理系统，实现用户管理，机房管理，机柜管理，服务器管理，工单管理。

## 需求分析：
###用户管理
### 首页：
        提供登录与注册的入口
        点击登录按钮跳转到登录页面
        点击注册按钮跳转到注册页面

### 注册：
       通过POST请求获取前端传来的注册信息
       通过数据库模块insert 写入到数据库
       If :
          写入成功跳转到登录页面
       ese:
          返回写入失败原因渲染到注册页面
### 登录：
        1 通过POST请求获取前端传来的登录信息
        2 通过数据库模块getone查寻信息是否正确
         If 正确
             跳转到个人主页
         Else:
             返回失败原因给jq。
### 个人信息主页:
       显示个人基本信息，提供修改密码和修改个人资料接口
       点击修改密码弹出模态窗
           后端通过POST请求获取前端传来的密码信息
           通过数据库模块getone查询旧密码是否正确
           If 旧密码正确：
               将新密码通过数据库模块update 更新到数据库
               讲更新后的数据返回给jq
           Else:
               提示具体失败原因返回给jq
### 用户列表页面：
       管理员用户：
           显示用户列表
           提供添加用户，编辑用户，删除用户的接口
        点击添加用户：
             跳转并弹出添加用户页面
             后端通过reques.form请求获取前端传来的用户信息
              后端通过数据库模块insert 讲用户信息写入到数据库
               If 添加成功：
                    跳转到登录页面
                Else:
                 返回失败信息并渲染到注册页面
        点击编辑：
             后端通过request.form获取到前端传来的id信息
             通过数据库模块getone查出人员信息并返回给jq渲染到模态窗
             前端通过模态窗修改相关数据提交POST请求到后端
             后端获取更新后的数据通过数据库模块update模块更新到数据库
             将数据库返回的信息return 到jq
        点击删除按钮：
              前端通过GET请求将id传到后端
              后端通过requset.get接收到id信息
              后端通过数据库模块delete删除相关信息
              将数据库返回的信息返回给jq提示是否删除成功
        普通用户：
             无法看到用户信息列表

##机房管理
### 机房列表页
             管理员
                可以对机房信息列表增删改查
             普通用户：
               只能查看机房信息，没有任何写权限

### 添加机房
    get请求跳转到添加机房页面
    通过request.post接收前端传来的机房信息
    将获取到的机房信息通过insert插入到数据库
    将插入数据库后返回的结果返回给jq

###编辑机房信息
    通过request.get方法接收要更新的id
    通过id查出要编辑的机房信息
    将查出来的机房信息通过jq传给前端
    通过request.form接收前端传来的信息
    将传来的信息通过update方法更新到数据库
    将数据库返回的结果传给jq

### 删除机房
     通过request。form接收要删除机房的Id
     通过delete方法删除机房
     将数据库处理结果返回给jq

## 机柜管理
同机房管理

##服务器管理
同机柜管理

#工单系统
###工单列表
     通过select方法将工单数据查出
     通过render_template传给前端


### 工单详情
    通过request.args 接收要查询的工单id
    通过getone 将单条工单信息查出并通过jq传给前端

    
### 工单申请
     通过request.form 接收前端传来的需要创建的工单信息
     通过time.strftime('%Y-%m-%d %H:%M') 创建时间信息
     通过insert方法将工单信息插入数据库并将结果返回给jq传到前端


### 历史工单
    通过select方法将工单查出并通过render_template传到前端展示






#图片展示
###登录
![](http://F:\reboot\15期\第十天\image\login.png)
###登录成功
![](http://F:\reboot\15期\第十天\image\loginsucess.png)
###用户信息
![](http://F:\reboot\15期\第十天\image\userinfo.png)
###用户列表
![](http://F:\reboot\15期\第十天\image\userlist.png)
###添加用户
![](http://F:\reboot\15期\第十天\image\useradd.png)
###编辑用户信息
![](http://F:\reboot\15期\第十天\image\userupdate.png)
###机房列表
![](http://F:\reboot\15期\第十天\image\idclist.jpg)
###添加机房
![](http://F:\reboot\15期\第十天\image\idcadd.jpg)
###编辑机房信息
![](http://F:\reboot\15期\第十天\image\idcupdate.jpg)
###机柜列表
![](http://F:\reboot\15期\第十天\image\cabinetlist.jpg)
###添加机柜
![](http://F:\reboot\15期\第十天\image\cabinetadd.jpg)
### 编辑机柜信息
![](http://F:\reboot\15期\第十天\image\cabinetupdate.jpg)
### 服务器列表
![](http://F:\reboot\15期\第十天\image\serverlist.jpg)
### 添加服务器
![](http://F:\reboot\15期\第十天\image\serveadd.png)
###编辑服务器
![](http://F:\reboot\15期\第十天\image\serverupdate.png)
###申请工单
![](http://F:\reboot\15期\第十天\image\jobadd.png)
### 工单列表
![](http://F:\reboot\15期\第十天\image\joblist.png)
###历史工单
![](http://F:\reboot\15期\第十天\image\jobhistory.png)
