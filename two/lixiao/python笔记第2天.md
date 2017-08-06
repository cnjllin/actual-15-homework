python笔记--第2天
=====
#### 1. 各种工具的使用
> 1. git
> 2. markdown使用
> 3. pasted在线代码分享工具
> 4. trello任务流程控制
> 5. 百度脑图
> 6. processon 流程控制图

#### 2. 数据存储

* 2.1 变量

		name = "reboot"
* 2.2 列表存储
		
		name = ["rice","peach","orange","apple"]         	//列表是有序的
* 2.3 字典存储

		user = {"name":"lixiao","age":"18","job":"ufo"}		//字典是无序的
* 2.4 文件存储

		cat file.txt
* 2.5 数据库存储
		
		mysql

#### 3. 数据类型
> python中有5中内建的数据结构：
> 
> 3.1 列表---列表list是处理一组有序项目的数据结构。列表中的项目应该包含在方括号'[]'中，每个项目之间用'逗号分隔。可以添加、删除、或者搜素列表中的项目

 * 3.1.1 列表的增删改查
 
<pre>
help(list)				//列出的帮助，列出所有列表的用法
type(name)				//type是判断数据类型是列表还是字典或者元组

例如：
	In [3]: arr = [1,2,3,4]
	In [4]: type(arr)
	Out[4]: list

	In [6]: name = {'a','b','c'}
	In [8]: type(name)
	Out[8]: set
</pre>
<pre>
name.append('aaa')			//在列表的末尾增加一个项目
name.insert(2,'bbb')			//在列表的指定位置插入一个元素。列表中的元素是从0开始算起
例：
	In [9]: arr = ["apple","pear","banna",]

	In [10]: arr.append("orange")
	In [11]: arr
	Out[11]: ['apple', 'pear', 'banna', 'orange']
	
	In [12]: arr.insert(1,"peach")
	In [13]: arr
	Out[13]: ['apple', 'peach', 'peer', 'banna', 'orange']
</pre>
***列表去重set(name)***
<pre>
	In [21]: a = ["aa","bb","cc"]	
	In [22]: b = ["bb","cc","dd"]
	
	In [23]: a + b
	Out[23]: ['aa', 'bb', 'cc', 'bb', 'cc', 'dd']
	
	In [24]: set(a+b)
	Out[24]: {'aa', 'bb', 'cc', 'dd'}
	
	In [25]: type(set(a+b))
	Out[25]: set
	
	In [26]: list(set(a+b))
	Out[26]: ['aa', 'cc', 'dd', 'bb']
	
	In [29]: type(list(set(a+b)))
	Out[29]: list
</pre>	
<pre>
del name[1]				//根据索引删除列表中相应的项目
name.remove('banna')			//直接删除指定的元素
name.pop()				//直接删除列表中的最后一个元素
例：
	In [15]: del arr[1]
	In [16]: arr
	Out[16]: ['apple', 'peer', 'banna', 'orange']
	
	In [17]: arr.remove("banna")	
	In [18]: arr
	Out[18]: ['apple', 'peer', 'orange']
	
	In [19]: arr.pop()
	Out[19]: 'orange'
	In [20]: arr
	Out[20]: ['apple', 'peer']
</pre>
<pre>
name[0]						//分片查，输出索引为0的元素
name[0:2]					//分片查询，输出前2个列表中的元素，name[0]，name[1]。name[2]这个元素不输出
name[:]						//输出所有元素
name[1:]					//输出第2个元素以后的元素，包括第2个元素
name[0-1]					//除了最后一个元素，其他元素全部输出
例：
	In [30]: arr = ["aa","bb","cc","dd","ee"]

	In [31]: arr[0]
	Out[31]: 'aa'
	
	In [32]: arr[0:2]
	Out[32]: ['aa', 'bb']
	
	In [33]: arr[:]
	Out[33]: ['aa', 'bb', 'cc', 'dd', 'ee']
	
	In [34]: arr[2:]
	Out[34]: ['cc', 'dd', 'ee']
	
	In [35]: arr[0:-1]
	Out[35]: ['aa', 'bb', 'cc', 'dd']
</pre>
<pre>
name.sort()					//查询，将项目按首字母排序，数字>大写>小写
name.reverse()					//项目顺序倒转
例：
	In [40]: arr.sort()
	In [41]: arr
	Out[41]: ['1', '2', '22', '3', '33', '34', '45', '5', '57', '6']   //按首个数字排序的
	
	In [45]: arr= ["2","5","1","4","3","6","4","2","7"]
	In [46]: arr
	Out[46]: ['2', '5', '1', '4', '3', '6', '4', '2', '7']
	
	In [47]: arr.sort()
	In [48]: arr
	Out[48]: ['1', '2', '2', '3', '4', '4', '5', '6', '7']

	In [49]: arr.reverse()
	In [50]: arr
	Out[50]: ['7', '6', '5', '4', '4', '3', '2', '2', '1']
</pre>

<pre>
len(name)			//查看列表中的元素个数
max(name)			//查看列表中的最大值
min(name)			//查看列表中的最小值
name.count('apple')		/查看列表中某个元素的个数
for apple in namelist:  	//搜索apple是否在namelist列表中
name.index("apple")		//查看apple在列表中的位置(索引号)

name['apple'] = "peach"	//修改列表中的元素
name[2]="peach"		//通过索引修改列表中的元素
</pre>

* 3.1.2 列表小练习
<pre>
	练习1：
	In [51]: for n in arr:
    ...:     print n
    ...:     

	4
	3
	2
	1
	
	练习2：
	In [63]: arr = ["abc","aaa","123"]

	In [64]: for n in arr:
    	...:     print "hello %s"%(n)
    	...:     
	hello abc
	hello aaa
	hello 123

	练习3：
	In [66]: arr = [{"name":"abc","age":"21","job":"sa"},{"name":"123","age":"25","job":"tt"},{"name":"ddd","age":"40","job":"it"}]

	In [67]: arr
	Out[67]: 
	[{'age': '21', 'job': 'sa', 'name': 'abc'},
	 {'age': '25', 'job': 'tt', 'name': '123'},
	 {'age': '40', 'job': 'it', 'name': 'ddd'}]
	
	In [68]: for user in arr:
	    ...:     print user
	    ...:     
	{'job': 'sa', 'age': '21', 'name': 'abc'}
	{'job': 'tt', 'age': '25', 'name': '123'}
	{'job': 'it', 'age': '40', 'name': 'ddd'}
	
	In [69]: for user in arr:			//优雅的显示
	    ...:     print "name is %s,age is %s,job is %s"%(user["name"],user["age"],user["job"]) //提取字典数据的方式
	name is abc,age is 21,job is sa
	name is 123,age is 25,job is tt
	name is ddd,age is 40,job is it
</pre>
* 3.1.3 字符串拼接
<pre>
	栗子：将192.168.1.1-254存入列表
    #!/usr/bin/python
    host_list = []
    netip = '192.168.1.'
    for n in range(1,254):
        ip = netip+str(n)    	
        host_list.append(ip)
    print host_list
</pre>
* 3.1.4 列表的遍历	
<pre>
普通遍历：
for item in namelist:		//for循环将列表以字符串的形式输出
    print item

enumerate形式				//for循环列出元素及下标
for n element in enumerate(list):
    print i,element 

举栗说明：
练习1：
	In [84]: num = ["one","two","three","four" ]

	In [88]: for i,element in enumerate(num):
	    ...:     print "num is %d element is %s" %(i,element)
	    ...:     print "num is %d element is %s" %(i,num[i])   //等价与上面的Print
	    ...:     
	num is 0 element is one			//0是下标，one是元素
	num is 0 element is one
	num is 1 element is two
	num is 1 element is two
	num is 2 element is three
	num is 2 element is three
	num is 3 element is four
	num is 3 element is four
练习2：
	In [92]: arr = [{"name":"abc","age":"21","job":"sa"},{"name":"123","age":"25","job":"tt"},{"name":"ddd","age":"40","job":"it"}]

	In [93]: for n,element in enumerate(arr):
	    ...:     print "%s----%s"%(n,element)
	    ...:     
	0----{'job': 'sa', 'age': '21', 'name': 'abc'}
	1----{'job': 'tt', 'age': '25', 'name': '123'}
	2----{'job': 'it', 'age': '40', 'name': 'ddd'}	
</pre>
	
> 3.2 元组
> 
> 3.3 字典

> 字典结构: 把键和值联系在一起，组成键值对。字典是dict类的实例对象

* 3.3.1 定义字典
<pre>
定义一个字典：
	dict = {"name":"aa","age":"18","job":"hk"}"
</pre>

* 3.3.2  字典的增删改查
<pre>
增加字典元素
	dict["address"] = "beijing"

查看字典
	In [101]: dict.keys()			//输出所有的keys
	Out[101]: ['job', 'age', 'name', 'address']

	In [102]: dict.values()			//查看所有的values值
	Out[102]: ['hk', '18', 'aa', 'beijing']

	In [104]: dict.values()[-1]		//查看最后一个值
	Out[104]: 'beijing'

	In [110]: dict['gs']
	Out[110]: {'age': '22', 'job': 'tc', 'name': 'bb'}

	In [111]: dict['gs']['job']		//查看字典中字典的元素
	Out[111]: 'tc'

	In [124]: dict.has_key('name')		//查看字典中是否存在这个元素，存在则返回True,否则返回False
	Out[124]: True

	n [125]: dict.has_key('names')
	Out[125]: False

	取值
	In [103]: dict["name"]
	Out[103]: 'aa'

	优雅显示	----->重点
	In [136]: dict.get("name",'haha')		//取值时如果不存在则打印指定的内容，不指定输出内容默认为空
	[136]: 'aa'

	In [137]: dict.get("names",'haha')
	Out[137]: 'haha'

	In [138]: dict.get("names")

	In [139]: dict.setdefault('name')		//取值时，如果存在则打印，如果不存在则输出空，并把错误的key加入元素
	Out[139]: 'aa'

	In [140]: dict.setdefault('names')

	In [141]: dict.setdefault('names','hha')

	In [143]: dict
	Out[143]: 
	{'address': 'beijing',
	 'age': '18',
	 'job': 'hk',
	 'name': 'aa',
	 'names': None,
	 'scroe': '80'}

修改
	In [113]: dict['gs']['job']='module'

	In [114]: dict
	Out[114]: 
	{'address': 'beijing',
	 'age': '18',
	 'gs': {'age': '22', 'job': 'module', 'name': 'bb'},
	 'job': 'hk',
	 'name': 'aa',
	'score': ['90', '100', '75']

字典嵌套  ---属于增加
	In [106]: dict["score"] = ['90','100','75']

	In [107]: dict
	Out[107]: 
	{'address': 'beijing',
	 'age': '18',
	 'job': 'hk',
	 'name': 'aa',
	 'score': ['90', '100', '75']}
	
	In [108]: dict['gs'] = {'name':'bb','age':'22','job':'tc'}
	
	In [109]: dict
	Out[109]: 
	{'address': 'beijing',
	 'age': '18',
	 'gs': {'age': '22', 'job': 'tc', 'name': 'bb'},
	 'job': 'hk',
	 'name': 'aa',
	 'score': ['90', '100', '75']}

删除字典
	In [116]: dict.pop('score')
	Out[116]: ['90', '100', '75']

字典合并
	In [127]: a = {"scroe":"80"}

	In [128]: dict.update(a)

	In [129]: dict
	Out[129]: {'address': 'beijing', 'age': '18', 'job': 'hk', 'name': 'aa', 'scroe': '80'}
</pre>
<pre>
字典的for循环-------重点****
	In [131]: for n,i in dict.items():
     	...:     print "%s---->%s" %(n,i)
     	...:         
	name---->aa
	age---->18
	scroe---->80
	job---->hk
	address---->beijing
</pre>


> 3.4 集合
> 
> 3.5 字符串
	In [70]: name = 'abcd'
		
	In [71]: name[0]
	Out[71]: 'a'
		
	In [72]: name[3]
	Out[72]: 'd'
> 3.6 文件的基本操作

<pre>
文件的读写操作

//打开文件，默认是只读，括号内可以是相对路径也可以是绝对路径
In [6]: fo = open("/python/access.txt") 

//查看文件句柄
In [7]: fo
Out[7]: <open file '/python/access.txt', mode 'r' at 0x34099c0>

//读取，read是一次全部读完，结果为一个整体的字符串。readline是逐条读取。readlines也是一次全部读完，但是结果不是整体的字符，是每行分开的
In [8]: fo.read()

Out[8]: '61.152.81.193 - - [30/Jul/2017:18:27:01 +0800] "GET /themes/tag/20170723.wvo7o.tkugf.cn HTTP/1.0" 200 24257 "-" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; SE 2.X MetaSr 1.0)" "-" "0.780" "10.3.0.201:80" "200" "0.643"\n

//写入
In [9]: fo.write("aaa:bbb")

//关闭文件，关闭后无法打开了
In [12]: fo.close()

</pre> 
<pre>
with方式读写文件。格式如下：
with open('file') as fo:
    data = fo.read()
    print data
例：
with open('/python/access.log') as fo:
    data = fo.readlines()
    for n in data:
        ip_num.append(n.split(' ')[0])
</pre>
<pre>
打开文件的几种模式
open('path')				//默认只读打开
open('path','r+')			//读写打开，如果有内容，就会从头覆盖相应字符串的内容
open('path','w')			//写入，先删除源文件重新写入，没有文件自己创建
open('path','w+')			//读写，同上
open('path','a')			//写入，在文件末尾追加新内容，文件不存在则创建
open('path','a+')			//读写，同上，最常用
open('path','b')			//打开二进制文件，要上述模式结合使用。读取图片
open('path','J')			//支持所有的换行符号，值\r \n \r\n
open()open()open()open()open()open()open()open()open()open()open()open()
</pre>
#### 4. ***字符串和列表之间的转换***
<pre>
log.split('.')		//split是按要求将字符串转换为列表。"."为分隔符，可任意指定。将数据分割成不同的元素
"**".join(log)		//将列表转换为字符串，"**"为指定的分隔符。
	
举个栗子：
	In [73]: log = '117.135.223.42 - - [30/Jul/2017:18:27:01 +0800] "GET /assets_default/css/reset-da43457f77.css HTTP/1.1" 200 1245 "https://www.moxiu.com//" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Trident/4.0;)" "-" "0.168" "1
    ...: 0.3.0.215:80" "200" "0.000"'

	In [74]: log.split(' ')

	Out[74]: 
	['117.135.223.42',
	 '-',
	 '-',
	 '[30/Jul/2017:18:27:01',
	 '+0800]',
	 '"GET',
	 '/assets_default/css/reset-da43457f77.css',
	 'HTTP/1.1"',
	 '200',
	 '1245',
	 '"https://www.moxiu.com//"',
	 '"Mozilla/4.0',
	 '(compatible;',
	 'MSIE',
	 '6.0;',
	 'Windows',
	 'NT',
	 '5.1;',
	 'Trident/4.0;)"',
	 '"-"',
	 '"0.168"',
	 '"10.3.0.215:80"',
	 '"200"',
	 '"0.000"'
	
获取第1个元素
	In [75]: log.split(' ')[0]
	Out[75]: '117.135.223.42'

定义一个空变量，然后获取第1、4、6、8个元素
	In [76]: logs = []

	In [77]: logs.append(log.split(" ")[0])
	
	In [79]: logs.append(log.split(" ")[3])
	
	In [80]: logs.append(log.split(" ")[6])
	
	In [81]: logs.append(log.split(" ")[8])
	
	In [82]: logs
	Out[82]: 
	['117.135.223.42',
	 '[30/Jul/2017:18:27:01',
	 '/assets_default/css/reset-da43457f77.css',
	 '200']

将以上获取的列表转化成字符串
	In [83]: "###".join(logs)   //"###"为分隔符，可任意指定
	Out[83]: '117.135.223.42###[30/Jul/2017:18:27:01###/assets_default/css/reset-da43457f77.css###200'
</pre>



#### 练习题

	习题1：
	列表去重练习，将列表name中的元素去重。 name = ["123","abc","de","de","21","abc","123","aaa","abc","21"]
	思路：
	1）首先遍历列表
	2）创建一个空列表，将name列表的元素添加到空列表中
	3）判断空列表中是否存在这个元素，如果存在，则不添加，如果不存在，则添加
	#!/usr/bin/python
	name = ["123","abc","de","de","21","abc","123","aaa","abc","21"]
	num = []
	for n in name:
	    if n not in num:
	        num.append(n)
	print num

    练习2：输入一个用户名，判断字典中是否存在，如果存在则输入密码登录，否则提示用户名不存在或密码错误
	#!/usr/bin/python
	users = [{'name':'wd','pwd':'123','age':18,'job':'coo'},{'name':'dd','pwd':'222','age':30,'job':'cfo'},{'name':'pc','pwd':'111','age':50,'job':'ceo'}]
	
	name = []
	pwd = []
	user = raw_input("please input name: ")
	
	for n in users:
	    name.append(n['name'])
	    pwd.append(n['pwd'])
	#    if user not in name:
	#        print "user not is exist"
	    if user == n['name']:
	        passwd = raw_input("please input pwd: ")
	        if passwd == n['pwd']:
	            print "ok"
	            break
	        else:
	            print "pwd wrong"
	            break
	else:
    print "user not is exist"




























