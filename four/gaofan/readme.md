### 文档结构：  

	[root@Python01 gaofan]# tree
		.
	├── login.py	#主程序，flask文件
	├── templates	#存放所有用到的模板目录
	│   ├── after_reg.html	#成功注册后，跳转到登录界面
	│   ├── login.html		#用户登录界面入口
	│   ├── login_userinfo.html		#成功登陆后显示用户信息界面
	│   ├── register.html	#注册界面
	│   └── skip.html		#登录失败跳转回登录界面
	├── userinfo.db		#存储用户信息数据库文件
	└── user_manager_system.py		#用户管理模块，内置注册和登录相关函数，被login.py调用
### 实现方式：    
* 抽象登录，注册，检测用户是否存在，密码输入是否正确等现象为函数
* 根据脑图所描绘的，确定好所需html文件的数目和内容
* 编写主程序文件，整合封装函数和html文件
* 脑图：  

![](https://github.com/51reboot/actual-15-homework/blob/master/four/gaofan/mind-image.png)




   * 测试结果：  
![](https://github.com/51reboot/actual-15-homework/blob/master/four/gaofan/result.gif)