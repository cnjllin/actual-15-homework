20170730听课大纲
# 一、True or False 语义讲解：
# 二、变量定义原则：
## 1、见名知意，如下：
###  username  
###  userpass
## 2、驼峰写法：
###  user_name
###  user_pass
# 三、工具介绍：
 - 在线代码共享:http://pasted.co/
 - 百度脑图：http://naotu.baidu.com 
 - markdown在线编辑：http://mahua.jser.me/
  - markdown在线编辑:tool.oschina.net/markdown/
 - 贴图网：http://www.tietuku.com/1eb46f0cad717328 
 - markdown语法：https://www.w3cschool.cn/markdownyfsm/
 - 团队远程协作工具:https://trello.com/login
 - 拓扑图在线设计：https://www.processon.com/;jsessionid=A565C1EC6DE91CD55B8E1ED41ADA1FDE.jvm1 

 # 四、数据存储归类：
 - 变量
 - 列表
 - 字典
 - 文件
 - 数据库
 # 五、列表操作：
 - 增加：
   - append用法：
     - list.append(obj) 
   ```python
   In [3]: my_list=[]
   In [4]: my_list.append("hello")
   In [6]: my_list.append("world")
   In [7]: my_list
   Out[7]: ['hello', 'world']
   ```
   *点评：该参数只能在列表结尾追加元素，因此不用指定列表索引。*
   - extend 用法：
     - list.extend(list1)
    ```python
    In [1]: my_list=[1,2,3,4,5,6]
    In [2]: my_list1=[7,8,9]
    In [3]: my_list.extend(my_list1)
    In [4]: my_list
    Out[4]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [5]: my_list.append(my_list1)
    In [6]: my_list
    Out[6]: [1, 2, 3, 4, 5, 6, 7, 8, 9, [7, 8, 9]]
    ```
    *点评：list.extend(list1)是list和list1的合并，list.append(list1)是list1作为一个元素追加到list中。*   
   
   - insert用法：
     - list.insert(index, obj)
   ```python
   In [13]: my_list.insert(2,"susan")
   In [14]: my_list
   Out[14]: ['hello', 'world', 'susan']
   ```
   *点评：该参数需要指定列表索引，可以在列表任意位置新增插入，之后的obj后移。*
   
   - 切片新增：
      - list[index:index]=[obj1,obj2,obj3]
    ```python
    In [15]: my_list
    Out[15]: ['hello', [7, 8, 9], 9, 8, 7, 6, 5, 4, 3, 2, 1]
    In [17]: my_list[3:3]=["xin","zeng"]
    In [18]: my_list
    Out[18]: ['hello', [7, 8, 9], 9, 'xin', 'zeng', 8, 7, 6, 5, 4, 3, 2, 1]
    ```
    *点评：等同insert,但是可以插入多个obj。*
  - 删除：
     - del用法：
       - del(list(index))
     ```python
     In [8]: my_list
     Out[8]: ['hello', 'world', 'susan']
     In [9]: del(my_list[2])
     In [10]: my_list
     Out[10]: ['hello', 'world']
     ```
     *点评：del()需要指定列表索引，可以在列表中删除任意位置的元素。*
     
     - remove用法：
       - list.remove(obj)
       ```python
       In [37]: a = [3,2,2,1]
       In [38]: a.remove(2)
       In [39]: a
       Out[39]: [3, 2, 1]
       In [40]: a.remove(3)
       In [41]: a
       Out[41]: [2, 1]
       ```
     *点评：remove()需要指定列表元素，可以在列表中删除该元素。*
     
     - pop用法：
       - list.pop([index])
       ```python
       In [43]: a = [3,2,2,1,4,5,6]
       In [44]: a.pop()
       Out[44]: 6
       In [45]: a
       Out[45]: [3, 2, 2, 1, 4, 5]
       In [46]: a.pop(2)
       Out[46]: 2
       In [47]: a
       Out[47]: [3, 2, 1, 4, 5]
       ```
      *点评：pop()需要指定列表索引，可以在列表中删除任意位置的元素并返回该索引。*
      
  - 修改：
    ```python
    In [47]: a
    Out[47]: [3, 2, 1, 4, 5]
    In [48]: a[1]=6
    In [49]: a
    Out[49]: [3, 6, 1, 4, 5]
    In [11]: my_list
    Out[11]: [1, 'hello', 2, 3, 4, 5, 6, 7, 8, 9, [7, 8, 9]]
    In [12]: my_list.sort()
    In [13]: my_list
    Out[13]: [1, 2, 3, 4, 5, 6, 7, 8, 9, [7, 8, 9], 'hello']
    In [14]: my_list.reverse()
    In [15]: my_list
    Out[15]: ['hello', [7, 8, 9], 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ```
    *点评：list.sort() 是对列表进行排序修改，list.reverse()是对列表进行翻转修改*
    
  - 查询：
    ```python
    In [49]: a
    Out[49]: [3, 6, 1, 4, 5]
    
    In [50]: a.sort()
    In [51]: a
    Out[51]: [1, 3, 4, 5, 6]
    *点评：a.sort() 对list列表元素递增排序，修改列表自身*
    
    In [52]: a.reverse()
    In [53]: a
    Out[53]: [6, 5, 4, 3, 1]
    *点评：a.reverse() 对list列表元素翻转排列，修改列表自身*
    
    In [55]: max(a)
    Out[55]: 6
    *点评：max(a) 提取a列表元素中最大值*
    
    In [56]: min(a)
    Out[56]: 1
    *点评：min(a) 提取a列表元素中最小值*
    
    In [57]: len(a)
    Out[57]: 5
    *点评：len(a) 计算列表a中元素个数*
    
    In [58]: a[::-1]
    Out[58]: [1, 3, 4, 5, 6]
    In [59]: a[0:2]
    Out[59]: [6, 5]
    In [60]: a[0::2]
    Out[60]: [6, 4, 1]
    In [61]: a[0:-1]
    Out[61]: [6, 5, 4, 3]
    *点评：列表a的切片操作，list[start:stop:step] ,注意不包括stop索引的元素。start为空表示从0索引开始，stop亦然。*
    
    In [64]: a= [6, 5, 4, 3, 1,1,2,5,6]
    In [65]: set(a)
    Out[65]: {1, 2, 3, 4, 5, 6}
    In [66]: a
    Out[66]: [6, 5, 4, 3, 1, 1, 2, 5, 6]
    *点评：set(a) 对列表a中元素去重并递增排序展示出来，不修改列表自身*
    *点评：常用在开发中，eg:对个人和部门权限重合的部分去重*
    
    In [66]: a
    Out[66]: [6, 5, 4, 3, 1, 1, 2, 5, 6]
    In [67]: a.index(1)
    Out[67]: 4
    *点评：a.index(obj) 获取元素的索引*
    
    Out[29]: ['124.238.248.52', '[30/Jul/2017:15:22:42', '/crontab/collect', '200']
    In [30]: b=",".join(a)  #join 列表转换成字符串
    In [31]: b
    Out[31]: '124.238.248.52,[30/Jul/2017:15:22:42,/crontab/collect,200'
    *点评：列表转换成索引*
    
    In [5]: with open('test.txt','a+') as f:
    ...:     for i,v in  enumerate(f.readlines()):
    ...:         print i,v
    0 hello world
    1  hello world2
    2  hello world3
    *点评：enumerate（list）遍历去除obj中的index和obj ，常用于for语句中*
    ```
    
 # 六、字典操作：
 - 增加：
     - 赋值方法：
       - dict[new_key]=value
     ```python
     In [19]: dict={'name':'my_dict'}
     In [20]: dict['age']='18'
     In [21]: dict
     Out[21]: {'age': '18', 'name': 'my_dict'}
     ```
     *点评：简单粗暴*
    
     - update方法：
       - dict.update(new_dict)
     ```python
     In [27]: dict
     Out[27]: {'age': '18', 'name': 'my_dict'}
     In [28]: dict1={'sex':'male'}
     In [29]: dict.update(dict1)
     In [30]: dict
     Out[30]: {'age': '18', 'name': 'my_dict', 'sex': 'male'}
     ```
     *点评：dict.update(dict1) ,dict收购dict1*
     
  - 删除：
     - del方法：
       - del dict[key] 
     ```python
     In [36]: dict
     Out[36]: {'age': '18', 'name': 'my_dict', 'sex': 'male'}
     In [37]: del dict['sex']
     In [38]: dict
     Out[38]: {'age': '18', 'name': 'my_dict'}
     ```
     *点评：根据key删除字典中的元素*
     
     - del方法：
       - del dict
    ```python
    In [40]: dict
    Out[40]: {}
    In [41]: del dict
    In [42]: dict
    Out[42]: dict
    In [43]: type(dict)
    Out[43]: type
    ```
    *点评：删除字典dict*
     
     - clear方法：
       - dict.clear() 
     ```python
     In [38]: dict
     Out[38]: {'age': '18', 'name': 'my_dict'}
     In [39]: dict.clear()
     In [40]: dict
     Out[40]: {}
     
     In [1]: x={}
     In [2]: y=x
     In [3]: x['name']='xiaoming'
     In [4]: y
     Out[4]: {'name': 'xiaoming'}
     In [5]: x.clear()
     In [6]: x
     Out[6]: {}
     In [7]: y
     Out[7]: {}

     In [1]: x={}
     In [2]: y=x
     In [13]: x['name']='xiaoming'
     In [14]: y
     Out[14]: {'name': 'xiaoming'}
     In [15]: x={}
     In [16]: y
     Out[16]: {'name': 'xiaoming'}

     In [69]: x
     Out[69]: {'name': 'xiaoming'}
     In [70]: y=x.copy()
     In [71]: x['age']=18
     In [72]: x
     Out[72]: {'age': 18, 'name': 'xiaoming'}
     In [73]: y
     Out[73]: {'name': 'xiaoming'}
     In [74]: x.clear()
     In [75]: x
     Out[75]: {}
     In [76]: y
     Out[76]: {'name': 'xiaoming'}

     ```
     *点评：清空字典中的元素,.clear()方法是清空复制关系中字典们的数据，但不会清空副本中数据。{}只会清空当前字典中的数据*
     
     - pop方法：
       - dict.pop(key)
     ```python
     In [49]: dict
     Out[49]: {'age': '20', 'name': 'my_dict', 'score': [80, 90, 100], 'sex': 'male'}
     In [51]: dict.pop('sex')
     Out[51]: 'male'
     In [52]: dict
     Out[52]: {'age': '20', 'name': 'my_dict', 'score': [80, 90, 100]}
     ```
     *点评：等同于del命令，除此之外pop方法还可以返回被删除元素的value*
     
  - 修改：
     ```python
     In [45]: dict={'age': '18', 'name': 'my_dict', 'sex': 'male'}
     In [46]: dict['age']='20'
     In [47]: dict
     Out[47]: {'age': '20', 'name': 'my_dict', 'sex': 'male'}
     ```
     *点评：根据字典中的元素key，修改该元素的value*
     
  - 查询：
    ```python
    In [52]: dict
    Out[52]: {'age': '20', 'name': 'my_dict', 'score': [80, 90, 100]}
    In [53]: dict['name']
    Out[53]: 'my_dict'
    *点评：简单粗暴*
    
    In [54]: dict.has_key('name')
    Out[54]: True
    *点评：相当于for x in a ；返回True or False*
    
    In [58]: dict
    Out[58]: {'address': 'CN', 'age': '20', 'name': 'my_dict', 'score': [80, 90, 100]}
    In [76]: dict.items()
    Out[76]: 
          [('age', '20'),('score',[80, 90, 100]),('name', 'my_dict'),（'address', 'CN')]
    In [75]: for key,value in dict.items() :
    ...:     print "{}  {}".format(key,value)
    ...:     
       age  20
       score  [80, 90, 100]
       name  my_dict
       address  CN
    *点评:dict.items()以列表的形式返回可遍历的(键, 值) ,结合for循环可以实现遍历字典的功能*
    
    In [77]: dict
    Out[77]: {'address': 'CN', 'age': '20', 'name': 'my_dict', 'score': [80, 90, 100]}
    In [78]: dict.get('address','Unknow')
    Out[78]: 'CN'
    In [79]: dict.get('address')
    Out[79]: 'CN'
    In [80]: dict.get('address-1')
    In [81]: dict.get('address-1','Unknow')
    Out[81]: 'Unknow'
    *点评：dict.get(key,[' ']) 判断字典中是否包含有key，如果有 返回value ；否则返回空也可以自定义输出。* 
    
    In [82]: dict.setdefault('address-1')
    In [83]: dict.setdefault('address')
    Out[83]: 'CN'
    In [84]: dict.setdefault('address-1','Unknow')
    In [85]: dict
    Out[85]: {'address': 'CN', 'address-1': None, 'age': '20', 'name':'my_dict', 'score': [80, 90, 100]}
    *点评：dict.setdefault(key,[]) 判断字典中是否包含有key，如果有 返回value ；否则返回空也可以自定义输出。*
    
    In [6]: dict.items()
    Out[6]: [('age', '18'), ('name', 'my_dict'), ('sex', 'male')]
    In [8]: dict.keys()
    Out[8]: ['age', 'name', 'sex']
    In [9]: dict.values()
    Out[9]: ['18', 'my_dict', 'male']
    *点评：dict.keys() 获取字典中所有的key，dict.values()获取字典中所有的值*
    ```
        
 # 七、文件操作
 - open函数：
   - f=open(filename[,mode[,buffering]])
     - name参数表示需要打开的文件名称
     - mode是打开模式
     - buffering用来控制文件的缓冲，默认值为0，表示不缓冲，设置为1就会有缓冲.
   - 打开模式，mode:
     - r             读取模式打开文件
     - w             读写模式打开文件
     - a             写入模式打开文件
     - b             二进制模式打开文件(可以和其他模式并用)
     - \+             读/写模式(可以和其他模式并用)
     - U             支持换行符(例如：\n、\r 或 \n\r 等)
   - 对象操作：f.<>
     - read() 把文件的全部内容读取成一个字符串。
     - readline() 一次只读取文件内容的第一行
     - readlines() 把文件的全部内容读取为一个列表，每一行作为列表的一个元素。
   ```python
   In [1]: f = open('test.txt','w')
   In [2]: f.write("hello")
   In [3]: f.close()
   
   In [4]: f = open('test.txt','r')
   In [5]: f.read()
   Out[5]: 'hello,world'
   
   In [1]: with open('test.txt','a+') as f:
   ...:       f.write("hello world")
   In [2]: with open('test.txt','a+') as f:
   ...:       f.write("\n hello world2")
   In [3]: with open('test.txt','a+') as f:
   ...:       f.write("\n hello world3")
   In [4]: with open('test.txt','a+') as f:
   ...:       print f.readlines()
          ['hello world\n', ' hello world2\n', ' hello world3']
          
    *点评：with open('file'，a+) as f:   这种方式写自动关闭文件，不需要以f.close结尾*
   ```
  
 # nginx日志分析：
 ```python
 In [23]: log='124.238.248.52 - - [30/Jul/2017:15:22:42 +0800] "POST /crontab/collect HTTP/1.1" 200 151 "-" "Python-urllib/2.6" "-" "0.166" "
    ...: 10.3.0.136:5000" "200" "0.106"'
In [24]: a=[]
In [25]: a.append(log.split(" ")[0])   #split转换成列表
In [26]: a.append(log.split(" ")[3])
In [27]: a.append(log.split(" ")[6])
In [28]: a.append(log.split(" ")[8])
In [29]: a
Out[29]: ['124.238.248.52', '[30/Jul/2017:15:22:42', '/crontab/collect', '200']
In [30]: b=",".join(a)  #join 列表转换成字符串
In [31]: b
Out[31]: '124.238.248.52,[30/Jul/2017:15:22:42,/crontab/collect,200'
In [1]: for i,element in enumerate(a):
   ...:     print "xiabiao is {},value is {}".format(i,element)
