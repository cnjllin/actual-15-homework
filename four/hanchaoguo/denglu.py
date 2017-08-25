#!/usr/bin/python
#coding:utf-8


#登陆函数
def denglu(username,passwd):
       dict_1 = {}
       list_1=[]
       with open('exce.txt') as f:
          for n in f:
             dict_1[n.split(":")[0]] = n.split(":")[1]
             list_1.append(n.split(":")[0])
          if username in list_1:
                 if dict_1[username].strip() == passwd:
                     return  "true"
                 else:
                    return "密码错误"

          else:
                 return  '用户名错误'
