
### 作业需求：    

*  通过登录与注册的页面，实现可以登录和注册
### 思路分析：

*  定义一个脚本：通过引用，flask框架，定义两个函数，分别为登录与注册 
*  定义登录的html，向后端传输username和password两个参数
*  定义注册的html，想后端传输username,new_password,confirm_password 三个参数
*  1、登录
*  定义一个登录的html，html中定义一个表单，用户在表单中输入：用户名和密码
*  Python脚本中定义一个login的函数，先从user.txt文件读取每行，将用户名放入一个列表，将用户名和密码对应存放在一个字典
*  Longin从前端html获取到用户名和密码，先判断用户名是否在列表中，判断用户名是否正确，如果正确，再通过字典，去判断密码是否正确，正确则提示登录成功
*  2、注册
*  定义一个注册的html，html中定义一个表单，用户在表单中输入：用户名、密码和确认密码
*  Python脚本中定义一个register的函数，先从user.txt文件读取每行，将用户名放在一个列表
*  Register从前端html获取到用户名、密码和确认密码，先判断用户名是否为空，然后判断用户名是否在列表里，如果在则提示已被注册，然后输入的密码是否为空，然后判断两次输入密码是否相同，如果两次密码也想通，则提示注册成功，并将用户名:密码，写入user.txt

### 作业说明：
 
*  ├── login_register.py   登录注册脚本
*  ├── templates           存放html的目录
*  │   ├── login.html      登录的html
*  │   └── register.html   注册的html
*  ├── test.docx           测试文档
*  ├── user.txt            用户信息表
*  └── xiangmu.docx        项目文档
