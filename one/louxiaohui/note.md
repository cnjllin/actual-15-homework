1.安装pip——类似linux的yum

2.通过pip安装ipython——ipython能实现自动补全

3.修改pip拉取软件包的源码——从官网变为国内豆瓣源

```
[root@test pip-9.0.1]# cat ~/.pip/pip.conf 
[global] 
trusted-host = pypi.douban.com
index-url = http://pypi.douban.com/simple 
[list] # pip list的格式更优雅
#format=legacy
format=columns
```
4.修改pip配置文件，让pip list显示更好看

5.字符串

```
In [15]: x = "hello,world"
In [16]: print x
hello,world

In [21]: y = " 888"
In [22]: print x + y
hello,world 888
```

### 格式化输出

```
#!/ust/bin/python
# -*- coding:utf-8 -*-

name = "Eric"
age = "18"
job = "sa"
score = float(99.99)
print "name %s, age is %s, jos is %s, score is %0.3f" %(name,age,job,score)
print "name {}, age is {}, jos is {}" .format(name,age,job)
```

### 删除字符串前后空格

```
#删除前后空格
In [8]: test = "lxlc  "

In [9]: test.strip()
Out[9]: 'lxlc'

In [10]: test = "  lxlc  "

In [11]: test.strip()
Out[11]: 'lxlc'

#删除右侧空格
In [12]: test.rstrip()
Out[12]: '  lxlc'

#删除左侧空格
In [13]: test.lstrip()
Out[13]: 'lxlc 
```

### 大小写转换

```
In [17]: test = "  Lxh  "

In [18]: test.strip()
Out[18]: 'Lxh'

In [19]: test.strip().upper()
Out[19]: 'LXH'

In [20]: test.strip().upper().lower()
Out[20]: 'lxh'
```

### 流程控制

```
#!/usr/bin/python
# -*- coding:utf-8 -*-
name = raw_input("please input your name:")
if name == "wd":
    print "welcome %s" % name
else:
    print "sorry, %s" % name
```


```
#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
name = raw_input("please input your name:")
password = raw_input("please input your password:")
if name == "wd":
    if password == "123":
        print "login success" 
    else:
        print "login failed"        
    print "welcome %s" % name
else:
    print "sorry, %s" % name
```

#### 登陆验证(只验证一次)

```
#!/usr/bin/python
# -*- coding:utf-8 -*-
name = raw_input("please input your name:")
password = raw_input("please input your password:")
if name == "wd":
    if password == "123":
        print "恭喜,%s,登陆成功" % name
    else:
        print "密码错误"            
else:
    print "%s用户不存在" % name
```

#### 猜数字
```
#!/usr/bin/python
# -*- coding:utf-8 -*-
count = 1
num = 10
total =3

while count <=3:
    total=total-1
    count+=1
    input_num = int(raw_input("please input num:"))
    if input_num == num:
        print "输入正确"
        break
    elif input_num > num:
        print "输入的数字太大,你还有%d次机会" % total
    else:
        print "输入的数字太小,你还有%d次机会" % total
else:
    print "输入错误超过三次，退出"
```

### for循环求最大值

```
#!/usr/bin/python
# -*- coding:utf-8 -*-

a = [1,23,34,23,23,67,434,34]
print max(a)

max = 1

for i in a:
    if i > max:
        max = i
print max
```

![image](http://i2.kiimg.com/1949/2917e5fafcf7c67b.png)


### git 

```
配置git
[root@test GithubGuide]# cat .git/config  |grep url
        url = https://xoyabc@github.com/xoyabc/GithubGuide.git

git命令
git status
git add test.py 
git commit -m "add a test file"
git config --global user.email 1031138448@qq.com
git commit -m "add a test file"
git push

```

