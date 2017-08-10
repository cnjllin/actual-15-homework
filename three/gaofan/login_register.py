#!/usr/bin/python
#coding:utf-8

''' 需求：利用函数实现简单的用户登录注册系统
    思路：
        1.用户的选择0代表登录，1代表注册，采用字典以及try实现switch功能；
        2.函数针对不同情况采用主要if--else以及while流程控制实现
        3.采用文本处理函数，实现数据的查询和写入
'''
# 注册函数
def reg(f,users):
    name = raw_input("请输入用户名：").strip()
    passwd1 = raw_input("设置您的账号密码：")
    passwd2 = raw_input("确认您的账号密码：")
    if name in users:
        result = "该用户已存在！"
    else:
        if len(name) == 0:
            result = "用户名不能为空"
        elif passwd1 != passwd2:
            result = "两次密码输入不一致！"
        else:
            f.write('%s:%s\n'% (name,passwd1))
            result = "注册成功!"
    return result
# 登录函数
def login(f,users):
    name = raw_input("请输入用户名：").strip()
    if name not in users:
        result = "用户不存在！"
    else:
        count = 0
        while count < 3:
            passwd = raw_input("请输入密码：")
            if passwd == users[name]:
                result = "恭喜您，登录成功!"
                break
            else:
                print "密码不正确，还有%s输入机会" % (2-count)
                count += 1
        else:
            result = "密码输入错误三次，账户已被锁定，请联系管理员"
    return result
# 开始函数，调用注册或者登录函数
def start():
    action = raw_input('请输入数字"0(登录)"或者"1(注册)"：\n')
    f = open("userinfo.txt","a+")
    users = {x.rstrip('\n').split(":")[0]:x.rstrip('\n').split(":")[1] for x in
             f.readlines()}
    operator = {"0":login,"1":reg}
    try:
        result = operator.get(action)(f,users)
    except:
        result = "您的输入有误！"
    finally:
        f.close()
    return result
print start()
