
## 课堂作业

>统计nginx访问日志，取出top10访问IP及其出现的次数

## 重点
>列表、字典循环

>join、split用法

>文件操作


## 作业讲解及注意事项


实现用户名密码登陆验证

1：判断用户名密码是否正确，正确则打印欢迎信息，错误则输出具体错误原因信息

2：用户可以连续输入三次密码。超过三次则锁定用户

3：密码位数必须超过6位
```
1.先判断密码长度
2.密码是否正确
3.密码输入错误超过三次则锁定用户
4.加注释
5.参考hanchaoguo代码
```
### 逻辑图
![Markdown](http://i4.eiimg.com/1949/b7c40d136b5c2728.png)

### 作业参考人员
张玲珑  陶亚可  李肖  这三位同学的github作业



## 空(字符串、列表、字典)真假判断

```
1.空字符串
2.None
3.0
4.空列表
5.空字典
6.True为真、False为假
```

![empty_string](http://i2.tiimg.com/1949/f3311b7d500822f8.png)
![empty_list](http://i2.tiimg.com/1949/2e32e1bfccf6feac.png)
![empty_dict](http://i2.tiimg.com/1949/b2325091ae97d593.png)
![zero](http://i2.tiimg.com/1949/1d6192db11192d80.png)
![0_and_1_not](http://i2.tiimg.com/1949/1f036838b3add555.png)


### GIT删除

```
git rm file
git commit -m "description"
git push
```


### 一些工具

* 团队协作
  
  https://trello.com/login
* 逻辑图
  
  https://www.processon.com/;jsessionid=A565C1EC6DE91CD55B8E1ED41ADA1FDE.jvm1
* 前端UI
  
  http://www.js-css.cn/divcss/admin/ace/index.html#

### 数据存储

![Markdown](http://i4.eiimg.com/1949/d665072f8a4c0d12.png)


### 列表
空列表
b = []
非空列表
a = ['a','b','c']

* 列表定义
```
In [2]: a = ['a','b','c']

In [3]: a
Out[3]: ['a', 'b', 'c']

In [4]: type(a)
Out[4]: list
```
### 列表操作

#### 追加与插入

  * apped末尾追加   
  * insert后面的括号中要有2个参数，第一个为插入位置 (从0开始算起)，第二个为插入元素,列表是**有序**的。
```
In [11]: a
Out[11]: ['a', 'b', 'e', 'c', 'd']

In [12]: a.append('f')

In [13]: a
Out[13]: ['a', 'b', 'e', 'c', 'd', 'f']

In [14]: a.insert(1,'g')
```

#### 元素取数据，第一个元素下标为0
```
In [16]: a
Out[16]: ['a', 'g', 'b', 'e', 'c', 'd', 'f']

#取第一个元素
In [17]: a[0]
Out[17]: 'a'

#取第一个至第三个元素
In [18]: a[0:2]
Out[18]: ['a', 'g']

#取最后一个元素
In [19]: a[-1]
Out[19]: 'f'

#取出所有元素
In [20]: a[:]
Out[20]: ['a', 'g', 'b', 'e', 'c', 'd', 'f']

#去除第二个到倒数第二个元素
In [21]: a[1:-1]
Out[21]: ['g', 'b', 'e', 'c', 'd']

```
#### 循环
```
In [32]: a
Out[32]: ['a', 'g', 'b', 'e', 'c', 'd', 'f']

In [33]: for x in a:
    ...:     print "hello,%s" % x
    ...:     
    ...:     
hello,a
hello,g
hello,b
hello,e
hello,c
hello,d
hello,f
```
#### 删除
```
In [35]: a
Out[35]: ['g', 'b', 'e', 'c', 'd', 'f']

In [36]: del a[0]

In [37]: a
Out[37]: ['b', 'e', 'c', 'd', 'f']

In [38]: a.remove('e')

In [39]: a
Out[39]: ['b', 'c', 'd', 'f']

In [40]: a.pop()
Out[40]: 'f'

In [41]: a
Out[41]: ['b', 'c', 'd']
```

#### 修改

```
In [46]: a
Out[46]: ['b', 'c', 'd']

In [48]: a[0]='e'

In [49]: a
Out[49]: ['e', 'c', 'd']
```



#### 列表删除重复元素

* 方式一
![Markdown](http://i2.tiimg.com/1949/46b6b1e25bcf5327.png)

* 方式二
![Markdown](http://i2.tiimg.com/1949/5123f98ba5755683.png)
```
1. 定义一个列表a
2. 定义一个空列表b
3. 遍历列表a，判断x是否在列表a中，如果不在就b.append(x)，然后print b
```

```
[root@test scripts]# cat list_clear_duplicate_element.py 
#!/usr/bin/python
# -*- coding:utf-8 -*-

a=[1,1,2,3,4,5,7,6,7]

b = []

for i in a:
    if i in b:
        continue
    else:
        b.append(i)
print b

'''
for i in a:
    if not i in b:
        b.append(i)
print b
'''
[root@test scripts]# 
[root@test scripts]# python list_clear_duplicate_element.py 
[1, 2, 3, 4, 5, 7, 6]
```


#### 列表拼接

a + b

a.extend(b)


#### split与join

* split
作用：把字符串转换为列表

用法：字符串.split('分隔符')[1]  

![Markdown](http://i4.eiimg.com/1949/0d5068dd03b40d7d.png)


```
#日志
'24.238.248.52 - - [30/Jul/2017:15:22:42 +0800] "POST /crontab/collect HTTP/1.1" 200 151 "-" "Python-urllib/2.6" "-" "0.166" "10.3.0.136:5000'
# 输出ip 时间 请求内容  状态

In [86]: log.split(" ")[6]
Out[86]: '/crontab/collect'

In [87]: 

In [87]: log.split(" ")[8]
Out[87]: '200'

In [88]: log.split(" ")[6]
Out[88]: '/crontab/collect'

In [89]: log.split(" ")[3].split('[')[1]
Out[89]: '30/Jul/2017:15:22:42'


log = '24.238.248.52 - - [30/Jul/2017:15:22:42 +0800] "POST /crontab/collect HTTP/1.1" 200 151 "-" "Python-urllib/2.6" "-" "0.166" "10.3.0.136:5000'
In [103]: a = []

In [104]: a.append(log.split(" ")[0])

In [105]: a.append(log.split(" ")[3].split('[')[1])

In [106]: a.append(log.split(" ")[6])

In [107]: a.append(log.split(" ")[8])

In [108]: a
Out[108]: ['24.238.248.52', '30/Jul/2017:15:22:42', '/crontab/collect', '200']
```

* join


作用：把列表转换为字符串

用法："分隔符".join(列表) 
```
In [122]: a
Out[122]: ['24.238.248.52', '30/Jul/2017:15:22:42', '/crontab/collect', '200']

In [123]: logs= "888".join(a)

In [124]: logs
Out[124]: '24.238.248.5288830/Jul/2017:15:22:42888/crontab/collect888200'

```


### 元组

元素不能修改


### 字典


* 字典操作

```
# 定义
In [144]: a = {'age':18,'name':18,'gf':{'age':18,'job':'model','name':'lucy'},'score':[90,100,110]}

#取出所有key
In [145]: a.keys()
Out[145]: ['gf', 'age', 'score', 'name']

#取出所有值
In [146]: a.values()
Out[146]: [{'age': 18, 'job': 'model', 'name': 'lucy'}, 18, [90, 100, 110], 18]

#增
In [147]: a['gender']='male'

In [148]: a
Out[148]: 
{'age': 18,
 'gender': 'male',
 'gf': {'age': 18, 'job': 'model', 'name': 'lucy'},
 'name': 18,
 'score': [90, 100, 110]}

#删
In [149]: a.pop('gender')
Out[149]: 'male'

In [150]: a
Out[150]: 
{'age': 18,
 'gf': {'age': 18, 'job': 'model', 'name': 'lucy'},
 'name': 18,
 'score': [90, 100, 110]}

#查
In [152]: a['gf']['job']
Out[152]: 'model'

#改
In [153]: a['gf']['job']='teacher'

In [154]: a
Out[154]: 
{'age': 18,
 'gender': 'male',
 'gf': {'age': 18, 'job': 'teacher', 'name': 'lucy'},
 'name': 18,
 'score': [90, 100, 110]}
```

 * get方法

dictionary_name.get('key','default_value')
检查key是否存在，不存在给其赋予一个默认值

```
In [169]: a
Out[169]: 
{'age': 18,
 'gender': 'male',
 'gf': {'age': 18, 'job': 'teacher', 'name': 'lucy'},
 'name': 18,
 'score': [90, 100, 110]}

In [170]: 

In [170]: a.get('names','default_value')
Out[170]: 'default_value'
```
 * 判断值是否存在
```
In [172]: a.has_key('names')
Out[172]: False

In [173]: a.has_key('name')
Out[173]: True
```

#### 字典中变量赋值

```
# print "%(key1)s %(key2)s %(key3)s" % dict_name

info = {'passwd': 'abcdef', 'age': 19, 'job': 'cto', 'name': 'kk'}
print "welcome %(name)s,your job is %(job)s,age is %(ages " % info 
```

#### 课堂作业

* 罗川
```
users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},{'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},{'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}]


print users

a = []
b = len(users)
NAME = raw_input('please input your name :')


for i in range(0,b-1):
    if NAME == users[i]["name"]:
        password = raw_input('please input your password :')
        if users[i].get("passwd") == password :
            a.append(users[i])
        else :
            print 'the password is not exist'
    else :
        continue
print a

```

* 常华伟
```
#!/usr/bin/python
#encoding:utf-8
users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': 'wd'},
 {'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'kk'},
 {'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'pc'}]

username = raw_input("please you name: ").strip()
userpass = raw_input("please you pass:").strip()
for i in users:
    if username in i['name']:
        if userpass in i['passwd']:
            print "ok"
            break
        else:
            print "err"
            break
else:
    print "err"
```

### 文件读取

#### 打开文件

f = open('test.py',a+)  

f.open('')

f.write()

f.read()


* 关于open 模式：
```
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )
```

read --字符串
readline --逐行读取
readlines ---列表

