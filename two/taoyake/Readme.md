####目录结构:

homework.py为代码内容

流程图.png为思维导图

第二天课知识点总结为课堂笔记总结

####作业需求:
 * 获取access.log日志top前10行ip地址
 
####作业需求分析：
1.第一步: 读取日志文件，获取每行日志中的ip地址并且存入字典：

* 用到知识点：

	* 1)使用open打开文件，默认只读方式
	*	2)使用for循环readlines的方式读取每一行日志
	*	3)使用split把ip获取出来,循环读取每一行日志，每读一次的时候，获取到日志中的ip地址，然后
存放在字典中

2.第二步: 把字典转化成列表，因为字典是无序的，列表是有序的，使用列表可以进行排序

* 用到知识点

Log_List = Log_Dict.items()
	

3.第三步: 排序，取出前十个ip地址

* 用到知识点: 
	* 冒泡排序

例子：python的冒泡排序

```
List = [30,22,19,78,36,21,90,62,5,8]
length = len(List)
for j in range(length-1): #这个循环负责设置冒泡排序进行的次数
for k in range(length-j-1): #j为列表下标
if List[k] > List[k+1]:
List[k],List[k+1] = List[k+1],List[k]

print List
```
 