#/usr/bin/python
#coding:utf-8
def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y

x = int(raw_input("请输入第一个数字：").strip())
y = int(raw_input("请输入第二个数字：" ).strip())
o = raw_input("请输入计算方式：").strip()

if o == 'jia':
    print jia(x,y)
if o == 'jian':
    print jian(x,y)
if o == 'cheng':
    print cheng(x,y)
if o == 'chu':
    print chu(x,y)
else:
    print "计算方式输入错误"
