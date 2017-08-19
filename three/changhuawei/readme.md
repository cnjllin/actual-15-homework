# 01
### 使用函数方式，实现用户登录，注册
### 分析
* 把之前的代码及定义成单个的函数模块 def aa() return
* 通过一个引入函数，匹配用户输入功能，调用相应的函数  res = aa()


#### 测试代码

/usr/bin/env python
```
[root@kdc4 changhuawei]# python 03_zuoye.py 
plrase input  zhuce/login:  zhuce
请输入用户名: user2
请设置密码: 111111
请确认密码: 111111
注册用户user2成功
None
[root@kdc4 changhuawei]# python 03_zuoye.py 
plrase input  zhuce/login:  user2
input err
[root@kdc4 changhuawei]# python 03_zuoye.py 
plrase input  zhuce/login:  login     
plrase input your name: user2
plrase input your pass: 111111
欢迎登陆user2
None
```


# 02
### 对nginx访问日志分析，取出top10
#### 分析
* 打开并遍历文件，分隔空格，定义到空字典   with open(xx) as f:
* 切分IP列，根据字典的get方法，计数  dic.get()
* 对字典的items遍历，使用 lambda value作为key 排行.并倒叙
* 用函数并在网页展示列表




#### 测试代码
未上图片
/usr/bin/env python
```
IP	counts
123.174.51.164	6958
111.85.34.165	2307
118.112.143.148	1617
117.63.146.40	1489
118.182.116.39	1404
1.48.219.30	1352
60.222.231.46	1132
10.35.1.82	1129


```
