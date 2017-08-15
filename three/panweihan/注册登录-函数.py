# -*- coding: utf-8 -*-
def reg():
    while True:
        name = raw_input("请输入用户名：").strip()
        if len(name) == 0:
            res = "用户名不能为空，请重新输入"
        else:
            password = raw_input("请输入密码：").strip()
            repass = raw_input("请再次输入密码：").strip()
            if len(password) == 0 or password != repass:
                res = "密码输入有误"
            else:
                f = open('F:\\user.txt','a+')
                f.write("%s:%s\n"%(name,password))
                f.close()
                res = "恭喜你，注册成功"
                break
    return res
def login():
    f = open('F:\\user.txt')
    user_dict = {}
    content = f.readlines()  # 将文件结果存成列表
    f.close()
    n = 3
    # 读取列表，并转存为字典
    for user in content:
        username = user.rstrip("\n").split(":")[0]
        user_dict[username] = user.rstrip("\n").split(":")[1]
    # 判断账号密码，正确的话提示欢迎信息，连续错误3次退出
    while True:
        login = False
        if n == 0:
            res = "你的账户已经被锁定，请联系管理员！"
            break
        name = raw_input("请输入用户名：").strip()
        if name in user_dict:
            for i in range(3):
                pwd = raw_input("请输入密码：")
                n = n - 1
                if pwd == user_dict[name]:
                    login = True
                    res = "欢迎来到%s的世界" % name
                    break
                elif n > 0:
                    print "密码错误，你还有%s次机会，连续错误3次将被锁定"%n
        else:
            print "用户名错误，请重新输入"
        if login == True:
            break
    return res
def start():
    choos = raw_input("请选择注册（输入1）还是登录（输入2）：").strip()
    if choos == "1":
        res = reg()
    elif choos == "2":
        res = login()
    else:
        res = "非法输入"
    return res
#产生错误的代码
#result = start()
#print start（）
result = start()
print result


