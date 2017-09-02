# 作业

## 使用 MVC 思想实现用户的增删改查

### 项目分析

- 共三个页面(首页,错误页,用户列表页) ， 一个弹窗(更新用户)
- 首页
  - session 判断用户是否存在 存在： return redirect('/user') 不存在： 用户选择登录或注册(默认显示登录的 div)
  - 登录 ：
    1. 通过form表单获取用户输入，同时通过JS判断用户输入是否符合本系统要求
    2. request.form获取用户信息，并通过生成式优化用户信息并传递至user模块判断用户是否存在
    3.  存在：更改路由 让路由监听 /user 不存在则放回 error.html
  - 注册 (原理与登录相似)

- 用户列表页 ：
    1. 判断用户角色，超级管理员显示所有用户信息并可以更改或删除其他用户信息，但不能删除本人信息，普通用户可以更改个人信息。
    2.当点击更新操作时当前用户信息会以弹窗的形式在本页面进行显示，用户可以对当前用户信息进行修改。修改成功后通过 location.reload()重新加载当前页面 。
    3.当点击删除操作时弹窗提示是否确认删除，若确认则通过 ajax 向后台传递要删除用户的id并进行删除，当删除成功后重新加载当前页面

- 错误信息页 ： 当程序出错时显示错误信息

## 程序说明
```
.
├── app.py
├── __pycache__
│   ├── user.cpython-35.pyc
│   └── utils.cpython-35.pyc
├── README.md
├── static
│   ├── css
│   │   ├── index.css
│   │   ├── login.css
│   │   └── user.css
│   ├── images
│   └── js
│       └── jquery-2.2.4.min.js
├── templates
│   ├── error.html
│   ├── index.html
│   └── user.html
├── user.py
├── user.sql
└── utils.py
```

