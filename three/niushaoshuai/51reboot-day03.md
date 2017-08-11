# 代码分析
## 统计nginx访问日志中访问ip前10：
- 版本1
```
#!/usr/bin/python
# --*-- coding:UTF-8 --*--

#生成ip为元素的列表。
my_list=list()
f=open('/home/niushaoshuai/access.txt','r')
for line in f.readlines():
    my_list.append(line.split(' ')[0])
f.close()

#生成{ip:times}为元素的字典。
my_key=dict()
for ip in my_list:
    if ip in my_key:
        my_key[ip]+=1
    else:
        my_key[ip]=1
    

#对字典进行排序，取出前十。
for i in  sorted(my_key.iteritems(),key = lambda asd:asd[1],reverse=True)[:10]:
    print "%s request %d times" % i
```
- 版本2
```
#!/usr/bin/python
# --*-- coding:UTF-8 --*--

#生成ip为元素的列表。
my_list=list()
f=open('/home/niushaoshuai/access.txt','r')
for line in f.readlines():
    my_list.append(line.split(' ')[0])
f.close()

#生成{ip:times}为元素的字典。
my_key=dict()
for ip in my_list:
    if ip in my_key:
        my_key[ip]+=1
    else:
        my_key[ip]=1

#对{ip:times}字典翻转
nd=dict()
od=dict()

for k,v in my_key.items():
    if v in nd:
        nd[v]+=1
    else:
        nd[v]=1
for k in nd:
    if nd[k]>1 :
        od.setdefault(k,[])
for k,v in my_key.items():
    if v in od:
        od[v].append(k)
    else:
        od[v]=k

#对字典进行排序，取出前十。
for t in range(10):
    m_key=max(od.keys())
    print "{} {}".format(m_key,od[m_key])
    od.pop(m_key)
```
 - 版本3

```
#!/usr/bin/python
# --*-- coding:UTF-8 --*--

#生成ip为元素的列表。
my_list=list()
f=open('/home/niushaoshuai/access.txt','r')
for line in f.readlines():
    my_list.append(line.split(' ')[0])
f.close()

#生成{ip:times}为元素的字典。
my_key=dict()
for ip in my_list:
    my_key[ip]=my_key.get(ip,0)+1
    
#对{ip:times}字典翻转
od=dict()
for k,v in my_key.items():
    od.setdefault(v,[])
    od[v].append(k)

#对字典进行排序，取出前十。
for t in range(10):
    m_key=max(od.keys())
    print "{} {}".format(m_key,od[m_key])
    od.pop(m_key)
```

### 对比版本1和版本2：
#### 差异：对字典排序的处理：
- sorted:   
  - sorted(my_key.iteritems(),key = lambda asd:asd[1],reverse=True)[:10]
  - *点评：简洁优雅，但必须经过百度搜索获得，也不便于代码阅读*
- for 循环：
  - m_key=max(od.keys()) 取出最大值，m_key.pop(m_key)
  - *点评：代码逻辑清晰，易读*
## 对比版本2和版本3：
### 差异：生成字典和字典翻转。
- 生成（ip:times）字典：
  - for 循环：对原字典遍历，如果原来不在my_key[ip]=1，否则my_key[ip]+=1；从而生成my_key新字典。
  - *点评：代码朴素*
  - for循环：对原字典遍历，my_key[ip]=my_key.get(s,0)+1 直接重构新字典。
  - *点评：代码优雅*
- 翻转新字典：
  - for 循环：3个循环重构2个函数，第一个重构字典对times出现的次数，第二个如果次数大于1 则第三个循环让重构的第二个函数v为列表类型（od.setdefault(v,[])），翻转。
  - *点评：代码臃肿，第一，二个循环可以忽略，让所有的v都为列表*
  - 版本2 优化后：一次for遍历，让所有的v都为列表：od.setdefault(v,[]) 放心的 od[v].append(k)翻转。
  - *点评： 代码优雅。*
  
## 代码整体点评：
### 统计日志访问次数的脚本需要经过四个步骤：
- 生成list[ip] 列表。
- 根据列表生成list {ip：times} 字典
- 对字典进行翻转，找出重复的项 。
- 对新字典进行排序。


## python生成html文件
```python
#!/usr/bin/python
# --*-- coding:UTF-8 --*--

#生成ip为元素的列表。
my_list=list()
f=open('/home/niushaoshuai/access.txt','r')
for line in f.readlines():
    my_list.append(line.split(' ')[0])
f.close()

#生成{ip:times}为元素的字典。
my_key=dict()
for ip in my_list:
    my_key[ip]=my_key.get(ip,0)+1

#对{ip:times}字典翻转
od=dict()
for k,v in my_key.items():
    od.setdefault(v,[])
    od[v].append(k)

#对字典进行排序，取出前十。
f=open('tongji.html','a+')
f.write("<html><table  border=1 >")
f.write("<tr><th>次数</th><th>单词</th></tr>")
pd=dict()
for t in range(10):
    m_key=max(od.keys())
    pd[m_key]=od[m_key]
    for pk in od.pop(m_key):
        f.write('<tr><td>%s</td><td>%s</td></tr>' % (m_key,pk))
f.write("</table></html>")
f.close()
```
### 相关代码分析：
   - f.write() 结合 html语言插入表头。
   - f.write() 结合for循环、html语言插入数据部分。
   - f.write() 结合html语言插入表尾。