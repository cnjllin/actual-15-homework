#!/usr/bin/env python
#_*_coding:utf-8_*_

# 需求：把每个人的对此成绩取平均值，并输出有几次成绩，按成绩崇高到底输出
# 结果类似这样：
# ['jim',98,4]
# ['lucy',69,3]
# ['tom',53,7]

# 处理文件
def test_file():
    my_dict={}
    my_count={}
    with open('test.txt') as f:
        for line in f:
            tmp=line.split(' ')
            my_dict[tmp[0]]=my_dict.setdefault(tmp[0],0)+int(tmp[1])
            my_count[tmp[0]]=my_count.get(tmp[0],0)+1
    return my_dict,my_count       

# 统计求和排序
def my_sort(my_dict,my_count):        
    a=sorted(my_dict.items(),key=lambda a:a[1],reverse=True )
    my_sort=[]
    for i in a:   
        a=list(i)
        a.append(my_count[i[0]])
        my_sort.append(a)
    return my_sort

# 入口
def a():
    my_dict,my_count=test_file()
    ma=my_sort(my_dict,my_count)
    return ma

# 测试调用
my_sort=a()
for i in my_sort:
    print i
            
        
                