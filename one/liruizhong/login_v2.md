## 1.登录成功
```
[root@LearnPython liruizhong]# python login_v2.py
Please input your name:liruizhong
Please input your passwd:reboot@123
Login successful
```
## 2.用户不存在
```
[root@LearnPython liruizhong]# cat user_file
liruizhong:reboot@123
luofeng:reboot@123
liyongxin:reboot@123
dujiayang:reboot@123
[root@LearnPython liruizhong]# python login_v2.py
Please input your name:mingming
Users don't exist

```

## 3.密码长度不够6位
```
[root@LearnPython liruizhong]# python login_v2.py
Please input your name:liruizhong
Please input your passwd:ll
The password number must be greater than 6
Please input your passwd:llll
The password number must be greater than 6
Please input your passwd:lllll
Three password errors, account locking
```
## 4.密码输入次数超过三次,用户被锁
```
[root@LearnPython liruizhong]# cat lock_user
liming
[root@LearnPython liruizhong]# python login_v2.py
Please input your name:liruizhong
Please input your passwd:ll
The password number must be greater than 6
Please input your passwd:llll
The password number must be greater than 6
Please input your passwd:lllll
Three password errors, account locking
[root@LearnPython liruizhong]# cat lock_user
liming
liruizhong        #liruizhong已追加到被锁文件中
```

下次再登录，被告知被锁定
```
[root@LearnPython liruizhong]# python login_v2.py
Please input your name:liruizhong
The liruizhong user is locked
```
