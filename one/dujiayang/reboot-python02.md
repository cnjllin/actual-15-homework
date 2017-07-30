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
####list.pop() 参数为index
```
>>> a
['aa', 'aa', 'bb', 'cc', 'dd']
>>> a.pop(1)
'aa'
>>> a
['aa', 'bb', 'cc', 'dd']
```
####list.remove() 参数为value
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
