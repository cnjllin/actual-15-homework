#coding:utf-8

#fo=open("user.txt")
#    users={}
#    content=fo.readlines()
#    fo.close()
#for user in content:
#    name=user.rstrip("\n").split(":")[0]
#    users[name]=user.rstrip("\n").split(":")[1]
    



def login():
    
    name=raw_input("请输入用户名：").strip()
    if name not in users:
        return "用户名不存在，无法登陆"
    else:
        password=raw_input("请输入密码：").strip()
        if password !=users[name]:
            return "密码输入有误，无法登陆"
        else:
            return "恭喜你，登陆成功"            
    





def reg():
    f=open('user.txt','a+')
    while True:
        name=raw_input("请输入用户名：").strip()
        if len(name)==0:
            print "用户名不能为空，请重新输入:"
            continue
        elif name in users:
            print "该用户名已注册，请重新输入"
            continue
        else:
            password=raw_input("请输入密码：").strip()
            repass=raw_input("请再次输入密码：").strip()
            if len(password)==0 or password !=repass:
                print "密码输入有误"
                continue
            else:
                f.write("%s:%s\n" % (name,password))
                f.close()
                return "恭喜你，注册成功"
                break       
       
   
   
   
  
   
def start():
    action=raw_input("请输入reg/login:").strip()
    if action=="login":
        res=login()
    elif action=='reg':
        res=reg() 
    else:
        res="输入不正确"
    return res

fo=open("user.txt")
users={}
content=fo.readlines()
fo.close()
for user in content:
    name=user.rstrip("\n").split(":")[0]
    users[name]=user.rstrip("\n").split(":")[1]
result=start()
print result
