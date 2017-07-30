## 1.登录成功
```
[root@LearnPython liruizhong]# python login_v1.py
Please input your name:liruizhong
Please input your passwd:reboot@123
Login successful
```
## 2.用户不存在
```
[root@LearnPython liruizhong]# python login_v1.py
Please input your name:lrz
Sorry,The user you entered does not exist.Please enter again
Please input your name:lzx
Sorry,The user you entered does not exist.Please enter again
Please input your name:liruizhong
Please input your passwd:reboot@123
Login successful
```
## 3.密码长度不够6位
```
[root@LearnPython liruizhong]# python login_v1.py
Please input your name:liruizhong
Please input your passwd:11
The password number must exceed 6
Please input your passwd:dgsags
The password number must exceed 6
Please input your passwd:reboot@123
Login successful
```
## 4.密码输入次数超过三次
```
[root@LearnPython liruizhong]# python login_v1.py
Please input your name:liruizhong
Please input your passwd:ll
The password number must exceed 6
Please input your passwd:mingadegegg
Sorry,The password you entered is incorrect. Please enter again
Please input your passwd:sdgsg
Three password errors, account locking
```
