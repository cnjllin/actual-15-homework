# 作业

## 1. falsk实现用户的登录注册功能，用户名和密码写入文件

## 2.nginx日志中IP数最高的10个

# 功能模块

## 登录与注册模块

 - 输入: 前端判断输入是否合法
 - 验证: 后台对用户名和密码进行验证
  + 成功: 返回用户名
  + 失败: 返回 0 并在页面提示失败原因

## nginx日志统计

  状态 : 用户处于登录状态可以查看日志信息

## 文件说明

```
 1. user.txt 用户名密码信息
 2. index.py 主程序
 3. /templates/login.html 登录与注册页面
 4. /tmplates/user.html　用户中心
 5. /tmplates/ip.html nginx日志统计展示页
 ```

 ## 效果展示
### 登录

![image](https://github.com/51reboot/actual-15-homework/raw/master/four/yangyi/day04/login1.png)

![image](https://github.com/51reboot/actual-15-homework/raw/master/four/yangyi/day04/login2.png)

### 注册

![image](https://github.com/51reboot/actual-15-homework/raw/master/four/yangyi/day04/login3.png)

### 日志统计

![image](https://github.com/51reboot/actual-15-homework/raw/master/four/yangyi/day04/IP.png)

