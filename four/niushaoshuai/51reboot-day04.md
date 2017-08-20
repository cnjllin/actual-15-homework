# 代码赏析
## flask框架传参：
##传参代码1：
```python
#!/usr/bin/python
#coding:UTF-8
from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def index():
    username=request.args.get('name')
    userpass=request.args.get('age')
    return "welcom %s your age is %s" % (username,userpass)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
```

### *http://59.110.12.72:5002/?name=牛少帅&age=28 ，?后面带有k=v的参数。*
### *request.args.get('name')，request.args.get('k')从浏览器中获取参数对应的值。*
### *request是flask方法之一
### *index() 函数中不需要指定参数。
### *输出结果： welcom 牛少帅 your age is 28*
### *request.args 的值为：ImmutableMultiDict([('age', u'28'), ('name', u'\u725b\u5c11\u5e05')])  是一个列表，可以变为字典。

##传参代码2：
```python
#!/usr/bin/python
#coding:UTF-8
from flask import Flask
app=Flask(__name__)

@app.route('/<string:name>/<string:passwd>')
def index(name,passwd):
    username=name
    userpass=passwd
    return "welcom %s,your pass is %s" % (username,userpass)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
```
### *hhttp://59.110.12.72:5002/niushaoshuai/123456 访问url*
### *在修饰器中直接定义接受的参数变量name，passwd*
### *index()函数中需要指定name,passwd参数*
### *函数体中直接对name,passwd进行操作，return信息。*
### *输出结果：welcom niushaoshuai,your pass is 123456*
### *传入参数未知，因此显得很死板*

## 渲染代码：
```python
#!/usr/bin/python
#coding:UTF-8
from flask import Flask,render_template
app=Flask(__name__)

@app.route('/index')
def index():
    res='welcom nss'
    return render_template('tj.html',result=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
```
### *引入render_template模块*
### *在py同级目录下新建 templates/ ，把html文件放入templates目录*
### *res变量定义渲染的内容*
### *{{ result }} 加到temples/html文件中*
### *render_template模块根据result对html进行渲染*