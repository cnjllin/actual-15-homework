# 第四天作业

## 用户注册登录接口项目文档

###  1 项目需求
   - 用户注册 - 填写用户信息，并写入文件 
   - 用户登录 - 填写用户账号密码，返回登录结果 
 ### 2 项目分析
   - 用户注册：HTML页面提交表单（用户名，密码，确认密码），后端判断用户是否存在，返回用户注册状态
   - 用户登录：HTML页面提交表单（用户，密码），后端判断输入信息是否匹配，返回登录状态
 ### 3 项目细节：==前端输入后端接收存入文件，后端返回渲染HTML返回给前端==
  框架--mvc(代码-python 框架（模板）-falsk 显示-jinjia2后端渲染html返回)
 #### 3.1 Flask框架
   - flask框架是简单的web模型，包括包目录 模板 类 函数 流程控制
   - 通过route装饰器访问URL，调用函数，返回结果
   - 项目共定义两个URL
    
    -- 1./页面
      @app.route('/')
      def index():
	  return render_template('login.html')

      @app.route('/login',methods=['GET','POST'])
       render_template('loginsucess.html',status=status)	
       
    -- 2./registor (前端提交post表单，函数调用request模块获取表单内容)
       @app.route('/registor')
       def registor():
	       return render_template('registor.html')
       #注册页面
       @app.route('/reg',methods=['POST','GET'])
       return render_template('regsucess.html',name=name,status=status)
   - 定义函数，URL调用
   - app.run()调用flask框架的route，返回网络协议，访问IP及端口
 #### 3.2 Python代码
    -- userfile()函数：获取用户密码文件存入字典
       userfile() 返回user_dict
    -- login()：
       调用userfile()判断输入用户密码，返回登录status,render_template()渲染成html返回给URL
    -- reg():
       调用userfile()判断输入是否存在，两次输入密码是否匹配，返回注册status,render_template()渲染成html返回给URL
  #### 3.3 后端渲染HTML返回
    -- login.html:/主页面,action=/login（执行登录）
        <html>
         <body>
          <form action="/login" method="POST">
           <ul>
            <li>用户名：<input type="text" name="username"> </li>
            <li>密码：<input type="password" name="passwd"> </li>
            <li><input type="submit" name="提交登录" ></li>
           </ul>
          </form>
         </body>
        </html>
    -- loginsucess.html 登录状态返回页面
    -- registor.html 注册页面
    -- regsucess.html 注册记过返回页面
 ### 4 项目测试
      
    -- 登录：登录.png
    -- 登录返回：登录返回.png
    -- 注册：注册.png
    -- 注册返回：注册返回.png
