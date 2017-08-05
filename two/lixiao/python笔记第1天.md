python第1天课堂笔记
====
第1阶段 基础安装
----
#### 1. linux系统安装`python`
>[root@linux-node1 ~]# yum -y install openssl-devel python-devel zlib*

#### 2. 安装`pip`
***`pip`类似linux系统中的`yum`***

* 2.1 首先下载`pip`
> [root@linux-node1 ~]# wget https://bootstrap.pypa.io/get-pip.py
>
> 如果在安装过程中出现报错，则添加参数`--no-check-certificate`

* 2.2 安装`pip`
> [root@linux-node1 ~]# python get-pip.py

* 2.3 查看`pip`列表

> [root@linux-node1 ~]# pip list

	DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.

	configobj (4.7.2)
	decorator (3.4.0)
	iniparse (0.4)
	perf (0.1)
	pip (9.0.1)
	pycurl (7.19.0)
	pygobject (3.14.0)
	pygpgme (0.3)
	pyliblzma (0.5.3)
	pyudev (0.15)
	pyxattr (0.5.1)
	setuptools (36.2.1)
	slip (0.4.0)
	slip.dbus (0.4.0)
	urlgrabber (3.10)
	wheel (0.29.0)
	yum-metadata-parser (1.1.4)

* 2.4 查看`pip`版本
> [root@linux-node1 ~]# pip -V

	pip 9.0.1 from /usr/lib/python2.7/site-packages (python 2.7)

#### 3. 使用`pip`安装`flask`和ipython
* 3.1 安装`flask`
> [root@linux-node1 ~]# pip install flask	

	[root@linux-node1 ~]# pip list|grep Flask
	Flask                              0.12.2

* 3.2 安装`ipython`

***注：安装ipython的时候提示`error: command 'gcc' failed with exit status 1`的报错，要安装`gcc`和`python-devel`***
> [root@linux-node1 ~]# pip install ipython	
> 
> [root@linux-node1 ~]# ipython
> 
	Python 2.7.5 (default, Nov  6 2016, 00:28:07) 
	Type "copyright", "credits" or "license" for more information.

* 3.3 修改`pip`配置文件，让`pip list`列表显示更优雅
  
*第1种方法：配置当前用户的`python`源*

	[root@linux-node1 ~]# mkdir ~/.pip
	[root@linux-node1 ~]# cd ./.pip	
	[root@linux-node1 .pip]# vim pip.conf
	[global]
	trusted-host=pypi.douban.com 
	index-url = http://pypi.douban.com/simple 
	[list] # pip list的格式更优雅
	format=columns

*第2种方法：配置全局的`pip`源码环境*
	
	[root@linux-node1 ~]# vim /etc/pip.conf
	[global]
	trusted-host=pypi.douban.com 
	index-url = http://pypi.douban.com/simple 
	[list]
	format=columns

***推荐使用第一种方法，因为第二种方法容易污染其他的环境***

#### 4. `python`和`ipython`的区别
<pre>
1) `ipython`是一个增强的交互式的python shell
2) `ipython`和`python`最大区别在于`ipython`会对命令提示符的每一行进行编号
3）`ipython`可以`tab`键不全命令
4）`ipython`可以使用hist查看历史记录
5）`ipython`可以在程序的任意地方进行断点调试
</pre>

第2阶段 基础练习
----
#### 1. 使用`python`打印`hello world`和四则运算

	In [1]: print "hello world"
	hello world
	In [2]: print 10+10
	20
	In [3]: print (10+10)*2
	40
	In [4]: print (10+10)*2/4
	10
	In [5]: print 10+10*2
	30
	In [6]: print 10+10*2/3
	16
	In [7]: print 10+10*2/5
	14

#### 2. 拼接字符串和变量

	In [8]: print "hello "+"world"
	hello world

	In [9]: print "hell"+"o"
	hello

	In [10]: x = "hello"

	In [11]: y = "world"

	In [12]: print x+y
	helloworld

	In [13]: x = "hello "

	In [14]: print x+y
	hello world

#### 3. 交互式输入、使用脚本打印内容
	
	In [19]: raw_input("please input your name: ")
	please input your name: reboot
	Out[19]: 'reboot'

	In [20]: raw_input("please input your name: ")
	please input your name: lixiao
	Out[20]: 'lixiao'

	[root@linux-node1 ~]# mkdir /python
	[root@linux-node1 ~]# cd /python/
	
	[root@linux-node1 python]# vim test.py
	#!/usr/bin/python								oython脚本的固定格式，或者下面的方式都可
	#!/usr/bin/env python    						固定格式
	print "hello world" 							//打印hello world
	x = raw_input("please input your name: ")      
	print "hello "+x								//交互式输入打印
	
    打印结果
	[root@linux-node1 python]# python test.py 
	hello world
	please input your name: reboot
	hello reboot

#### 4. `python`脚本的注意细节
<pre>
1) `python`脚本的缩进问题：`python`脚本对缩进非常严格，缩进不正确会直接倒是脚本执行失败
2）字符集问题：如果`python`脚本里包含汉字，则要指定字符集
  #coding:utf-8
  例如：  每个python脚本的开头写入以下内容即可：
  #!/usr/bin/python 或者#!/usr/bin/env python
  #coding：utf-8
</pre>

#### 5. 字符串格式化输出

	定义变量
	In [5]: name = "lx"
	In [6]: age = "20"
	In [7]: job = "sa"
	输出方式：
	In [8]: print "hello "+name+",age is "+age+",job is "+job
	hello lx,age is 20,job is sa
	经过c语言格式化以后
	In [10]: print "hello %s,age is %s,job is %s"%(name,age,job)
	hello lx,age is 20,job is sa
	
	或者经过c#方式格式化：
	In [14]: print "hello {},age is {},job is {}" .format(name,age,job)   //注：format的前面的“.”号不能丢，否则报错
	hello lx,age is 20,job is sa

	In [17]: print "hello %s,age is %d,job is %4s,fenshu is%3f"%(name,age,job,99.9)
	hello lx,age is 20,job is   sa,fenshu is99.900000
***注释：%s----字符串  %d----数值   %f-----浮点数   %4s----4代表占位符   %2f-----2代表保留多少位小数***

#### 6. 模块
	
	1）统计value值的个数
	In [39]: name = ["aoi","maria","aoi","aaa","aoi","aaa"]

	In [40]: name.count("aaa")
	Out[40]: 2
	In [41]: name.count("aoi")
	Out[41]: 3
	
	2）消除字符两端的空格
	In [46]: name = "hello world     "
	In [49]: name
	Out[49]: 'hello world     '
	In [50]: name.strip()
	Out[50]: 'hello world'
	
	In [51]: name = "       hello world     "
	In [52]: name
	Out[52]: '       hello world     '
	In [53]: name.strip()
	Out[53]: 'hello world

	3）消除字符左边和右边的空格
	In [54]: name = "       hello world     "

	In [55]: name.lstrip()					//消除左边的空格
	Out[55]: 'hello world     '

	In [56]: name.rstrip()					//消除右边的空格
	Out[56]: '       hello world'
	
	4）设置大小写转换
	In [54]: name = "       hello world     "
	In [58]: name.strip().upper()	//转换大写
	Out[58]: 'HELLO WORLD'
	In [59]: name = "hello world"
	In [61]: name.upper()			//转换大写
	Out[61]: 'HELLO WORLD'
	
	In [62]: name = "HELLO WORLD"

	In [63]: name.lower()			//转换小写
	Out[63]: 'hello world'

	In [65]: name.lower().strip()	//转换小写
	Out[65]: 'hello world'

	5）设置验证码
	In [69]: import string			//导入模块，必须

	In [70]: string.letters			//打印字符
	Out[70]: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

	6）随机数模块
	In [74]: import random			//导入模块
	In [76]: random.sample("aabbddceeada",6)		//随机抽取6个字符
	Out[76]: ['e', 'd', 'a', 'b', 'a', 'a']

	7）随机字符串
	In [77]: "".join(random.sample("aabbddceeada",6))
	Out[77]: 'bdaaab'


第3阶段 `if/for/while`语句的使用
----
#### 1. if语句的流程控制

***if else语句实现逻辑控制***

	if 判断真假:
	    如果是真 执行命令1
    else:
		如果是假 执行命令2
    print 命令3  	//此行的打印与上面的if语句无关，不管命令是真是假都会执行

***if elif else语句实现逻辑控制***

	if 判断真假:
	    如果是真 执行命令1
    elif 判断真假
	    如果是真 执行命令2
	...
    else:
		如果是假 执行命令3

***或与非***

	if  a == b：				//一个'='是赋值。'=='是做比较运算
        情况是true的，执行c
        情况是true的，执行d
    else：
        情况是flasede ，执行e	
	
	A and B 都是 true的才是true
	A or B 任何一个是true的就是true，
    not A 如果A是not返回true

- 1.1  `if`语句练习	

<pre>
	In [78]: name = raw_input("please input your name: ")
	please input your name: reboot

	In [79]: if name == "reboot":
		...:     print "%s is right!"% name
		...: else:
		...:     print "%s is error!"% name
		...:     
	reboot is right!

	In [80]: name = raw_input("please input your name: ")
	please input your name: lixiao

	In [81]: if name == "reboot":
		...:     print "%s is right!"% name
		...: else:
		...:     print "%s is error!"% name
		...:     
	lixiao is error!
 	
	###用脚本判断用户名是否为reboot
    [root@linux-node1 python]# cat test.py 
	#!/usr/bin/python
	name = raw_input("please input your name: ")
	if name == "reboot":
		print "%s is right!" % name
	else:
		print "%s is error!" % name

	[root@linux-node1 python]# python test.py 
	please input your name: lixiao
	lixiao is error!
	[root@linux-node1 python]# python test.py 
	please input your name: reboot
	reboot is right!
</pre>
* 1.2 用`if`语句实现用户名和密码登录

<pre>	
	第一种方式：						//此方式简单粗暴
	#!/usr/bin/python
	name = raw_input("please input your name: ")
	passwd = raw_input("please input your name: ")
	
	if name == "reboot" and passwd == "123456":
		print "welcome you %s" % name
	else:
		print "sorry,%s is error!"% name
	                                                                                                                                     
	[root@linux-node1 python]# python test1.py 
	please input your name: lixiao
	please input your name: 123456
	sorry,lixiao is error!
	[root@linux-node1 python]# python test1.py 
	please input your name: reboot
	please input your name: 123456
	welcome you reboot
	
	第二种方式：
	#!/usr/bin/python
	name = raw_input("please input your name: ")
	if name == "reboot":
		passwd = raw_input("please input your passwd: ")
		if passwd == "123456":
			print "welcome you %s" % name
		else:
			print "sorry,password is error!"
	else:
	print "user not is exist!"
</pre>

#### 2. while循环语句
	
	while语句流程控制
	方式1：
	while 判断情况是否成立：
		如果情况是True,缩进里的代码就会持续执行，直到情况是flase
	
	方式2：
	while True
		情况成立，代码会持续执行

	A and B 都是 true的才是true
	A or B 任何一个是true的就是true，
    not A 如果A是not返回true

* 2.1 while语句练习

<pre>
	name = ""
	while not name:
		name = raw_input("please input your name: ")
	print "hello " + name    	//注意此处的print，缩进和不锁进是有很大区别的

例1：打印1--10的数字
	#!/usr/bin/python
	i = 0				//定义一个变量i
	while i <= 10:		//判断i是否小于10，如果大于10则不成立
		print i			//情况成立则打印i
		i += 1			//i自增


例2：让用户一直输入数字，如果输入的是0，终止程序，并且打印所有数字之和
	#!/usr/bin/python
	#coding:utf-8
	num = ""							//定义num为一个空变量
	i = 0								//定义变量
	while num != "0":					//判断变量是否不等于0
        num = raw_input("input num: ")	//交互式输入
		i == num						
		i = int(i)+int(num)
	print i

	
例3：用户一直输入数字，如果没有输入任何值则终止程序，并打印出所有数字的平均值
	方法1：
	#!/usr/bin/python
	#coding:utf-8
	i = "0"
	num = 0
	n = 0
	while True:
		num = raw_input("please input num: ")
		if num != "":
			i = int(i)+int(num)
			n += 1
		else:
			print i/n
			break;

	方法2：
	sum = 0
	n = 0
	while True:
		num = raw_input("num: ")
		if num == "":
			break;
		sum += int(num)
		n += 1
	print sum/n
	
例4：存10000块钱，年利率是3.25%，多少年翻番
	num = 10000
    years = 0
	while num < 20000:
		num = num*1.0325
		years += 1
	print years


例5：登录用户，用户名和密码输入三次提示错误
	#!/usr/bin/python
	#coding:utf-8
	i = 0
	while i < 3:
		user = raw_input("please input your user: ")
		i += 1
		if user == "reboot":
			passwd = raw_input("please input your passwd: ")
			if passwd == "123456":
				print "welcome you %s!" %user
			else:
				print "sorry,passwd is wrong!"
		else:
			print "sorry,user not is exist!"
	
例6：指定数字50，循环输入数字，如果输入的不对，则提示太大或太小。超过三次退出，并提示还有几次机会
	#!/usr/bin/python
	#coding:utf-8
	i = 0
	time = 0
	while i < 3:
		num = int(raw_input("please input your num: "))
		i += 1
		time = 3-i
		if num != int(50):
			if num < int(50):
				print "您输入的数字太小了，您还有%s次机会"%time
			else:
				print "您输入的数字太大，您还有%s次机会"%time
		else:
			print "is good"
			break
</pre>

#### 3. `for`循环语句

	`for`循环语法：
	for n in 1,2,3,4,5
	    print "num is %s"%n
		
    for n in range(1,5)
	    print "num is %s"%n

	i = [1,2,3]
	for n not in i
		print "num is %s"%n
	==================================
		
	xrange和range的区别
	range（10）会马上分配生成10个数的空间
	xrange（10）不会一次全部分配空间，需要多少分配多少

	rang的用法
	In [2]: range(1,10)
	Out[2]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

	In [3]: range(1,10,2)
	Out[3]: [1, 3, 5, 7, 9]
	
例1，求num = []的最大值
	#!/usr/bin/python
	#coding:utf-8
	a=[1,23,34,23,26,89,67,454,53,34,67,13,68,134]
	num=0
	for n in a:
		if num < n:
			num = n
	print num
	
	python中推荐的方式：
	#!/usr/bin/python
	#coding:utf-8
	a=[1,23,34,23,26,89,67,454,53,34,67,13,68,134]
	print max(a)
	
例2：遍历一个序列["C","js","python","js","css","js","html","node","js"],统计js出现的次数
	#!/usr/bin/python
	#coding:utf-8
	stri = ["C","js","python","js","css","js","html","node","js"]
	num = "js"
	i = 0
	for n in stri:
		if num == n:
			i +=1
	print i

#### 4. 排错，判断字符类型对错
    例如：print 1/0,正常情况下，会报错
    [root@linux-node1 python]# python test.py 
	Traceback (most recent call last):
	File "test.py", line 3, in <module>
		print 1/0
	ZeroDivisionError: integer division or modulo by zero
	
	用try排错
	#!/usr/bin/python
	#coding:utf-8
	try：
		1/0
	except Exception,e:
		print e  //此处可以自定义，例如print "语法错误"

	[root@linux-node1 python]# python test.py 
	integer division or modulo by zero





































