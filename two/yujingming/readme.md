# 作业说明

* top10.py为程序代码

* 作业流程图.png为作业流程图



# 作业要求及思路

## 作业要求：    打印access.log中前10个访问网站次数最多的IP
## 作业思路：

* 读取access.txt文件内容 打开文件 open('文件绝对路径')
一般用 with ..open..，打开后自动关闭文件 
with open('access.txt','a+') as f:
f.read()读取文件所有内容
f.readline()读取一行内容
* 循环获取的文件内容 for line in f: 生成temp_dict,ip:对应出现次数

* 虽然Python的内置dictionary数据类型是无序的。
可是有时我们需要对dict中的item进行排序输出，可能根据key，也可能根据value来排
参考sorted 方法：
http://www.cnblogs.com/linyawen/archive/2012/03/15/2398292.html



流程图

```
graph TD
A(读取access.txt)-->B(split解析ip)
B(split解析ip)-->C(字典存储ip,次数,次数用get方法实现)
C --> D(dict按value,用sorted方法排序) 
D --> E(排序后输出top10) 

```
