作业总结

写代码需要逻辑思路清晰，然后需要注释代码规范。代码需求是否合理。
写代码画思维导图
写测试报告
循环一般嵌套两次最好
使用not or and 查询数据库的时候
rbac权限控制
列表和字典最多的是for循环
最多的形式是列表嵌套字典
开发字典里面使用a.get()
markdown使用总结http://531d2d13.wiz03.com/share/s/1j7iQj2pF4PP2VhPBO1FRNwA0MS8Yz009ARg2G6F7U0XfBq5
数据存储
#1：变量

name = "cf"
#列表

user = ['panda','kk']
#字典

user ={'name':'panpa','age':18}
#文件

cat user.txt
panda
kk
#数据库存储

mysql
#列表去重

#!/usr/bin/python
# --*-- coding: utf-8 --*--
'''
a=[1,1,2,3,4,5,7,6,7] 
b=[]
for i in a:
    if not i in b:
       b.append(i)
print b
'''
#split

字符串.split(文件)
#join

字符串.join(文件)
#字典

#get方法 在字典里面判断很重要（values存在就不报错，不存在就报错）

In [73]: a.get("name")
Out[73]: 'cf'

In [74]: a.get("name","1234")
Out[74]: 'cf'

In [75]: a.get("jobs","1234")
Out[75]: '1234'

In [76]: a.get("job","1234")
Out[76]: 'it'
#打开关闭文件

课堂作业 统计 nginx top10和对应的次数
