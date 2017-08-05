## 数据存储

### 变量
    name = "panda"

### 列表存储
    user = ['panda','kk']

### 字典存储
    user = {'name':'panda','age':18}

### 文件存储
    cat user.txt
    panda
    kk

### 数据库存储
        mysql
        
## 列表list

```javascript
>>> a = ['aa','bb','cc']
>>> a
['aa', 'bb', 'cc']
```
```
>>> a.append('dd')
>>> a
['aa', 'bb', 'cc', 'dd']
>>> a.insert(1,'aa')
>>> a
['aa', 'aa', 'bb', 'cc', 'dd']
```
#### list.pop() 参数为index
```
>>> a
['aa', 'aa', 'bb', 'cc', 'dd']
>>> a.pop(1)
'aa'
>>> a
['aa', 'bb', 'cc', 'dd']
```
#### list.remove() 参数为value
```
a
['aa', 'bb', 'cc', 'dd']
>>> a.remove('dd')
>>> a
['aa', 'bb', 'cc']
```
list.reverse() 反转列表
```
['aa', 'bb', 'cc']
>>> a.reverse()
>>> a
['cc', 'bb', 'aa']
```
list.sort() 列表排序
```
['cc', 'bb', 'aa']
>>> a.sort()
>>> a
['aa', 'bb', 'cc']
```
### 遍历列表a，x,y随意写，x是下标，y是下标对应的列表内容
```
>>> a
['aa', 'bb', 11, 22, 'cc']
>>> for x,y in enumerate(a):
...     print y,x
...
aa 0
bb 1
11 2
22 3
cc 4
```
### 列表取值
```
>>> a
['aa', 'bb', 11, 22, 'cc']
>>> a[:4]
['aa', 'bb', 11, 22]
>>> a[:4:1]
['aa', 'bb', 11, 22]
>>> a[:4:2]
['aa', 11]
>>> a[:4:3]
['aa', 22]
```
* split(",") 以逗号为分隔将字符串转换为列表
* ",".join() 以逗号为分隔将列表转换为字符串

```
a = '124.238.248.52 - - [30/Jul/2017:15:22:42 +0800] "POST /crontab/collect HTTP/1.1" 200 151 "-" "Python-urllib/2.6" "-" "0.166" "10.3.0.136:5000" "200" "0.106"'
b = []
for i in [0,3,6]:
    b.append(a.split(" ")[i])
print b
['124.238.248.52', '[30/Jul/2017:15:22:42', '/crontab/collect']
```

* logs = log.split(",").split("[").strip()
* b = ",".join(logs)

### 字典dict

* a.keys()  查看所有key
* a.value() 查看所有值
* a.has_key('name') 查看有没有name这个key，返回bool值
* a.update(b) 合并ab2个字典
```
>>> dict
{'Age': 7, 'Name': 'Manni'}
>>> for hehe in dict:
...     print hehe,'value is %s' % dict[hehe]
...
Age value is 7
Name value is Manni
```
dict.items()会把字典的key，value变成个元组，然后把所有元组放在一个列表里。
```
>>> dict
{'Age': 7, 'Name': 'Manni'}

>>> dict.items()
[('Age', 7), ('Name', 'Manni')]
>>> dict.items()[0]
('Age', 7)
>>> dict.items()[0][1]
7
>>> dict.items()[0][0]
'Age'
>>> for i in dict.items():
...     print i
...
('Age', 7)
('Name', 'Manni')
>>> for i in dict.items():
...     print i[0]
...
Age
Name
>>> for i in dict.items():
...     print i[1]
...
7
Manni
>>> for i in dict.items():
...     print i[0][0]
...
A
N

>>> for x,y in dict.items():
...     print x,y
...
Age 7
Name Manni
```
```
for k,v in b.items():
	print "%s --> %s" %(k,v)
```
* a.get("name","hehe") get取值，如果name这个key不存在，则给指定的hehe作为默认值,不指定默认为空。
```
>>> a = {'name':'tom','gf':{'lily':18,'vivi':20},'age':22,'job':'java'}
>>> a
{'job': 'java', 'gf': {'vivi': 20, 'lily': 18}, 'age': 22, 'name': 'tom'}
>>> a.get("name")
'tom'
>>> a.get("name","")
'tom'
>>> a.get("name","hehe")
'tom'
>>> a.get("nam","hehe")
'hehe'
```
```
In [2]: users
Out[2]:
[{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},
 {'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},
 {'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}]
In [4]: for i,user in enumerate(users):
   ...:     print i,user['name']
   ...:
0 wd
1 kk
2 pc
```
with open() as f: 自动close()不用在手动输入f.close()
```
In [5]: with open('test.txt','a+') as f:
   ...:     data = f.read()
   ...:

In [6]: data
Out[6]: 'aaa\n'
```
