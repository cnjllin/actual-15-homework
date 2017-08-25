# 04作业

------
## 用户登录注册渲染
### 知识点
* 用到模块
from flask import Flask,request,render_template （render_template 到前端渲染）
* methods=['GET', 'POST'])
* post --->request.form.get('name')
* get  ---->request.args.get('name')
* 路由 @app.route('/login/')


------
命令行：
```
/bin/bash

[root@kdc4 four]# tree changhuawei/
changhuawei/
├── 04_zuoye_flask01.py
├── 04_zuoye_flask02.py
├── templates
│   ├── index.html
│   ├── login.html
│   ├── reg.html
│   └── zhuce.html
└── yonghu.txt

1 directory, 7 files
[root@kdc4 four]# 
[root@kdc4 changhuawei]# python 04_zuoye_flask01.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 163-126-751
root@kdc4 changhuawei]# python 04_zuoye_flask02.py 
 * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 163-126-751
 

```


