#coding=utf-8
def reg():
    f=open("C:\\Users\\xxx\\Desktop\\abcd.txt","a+")
    users=raw_input("please input you name:")
    num=0
    while num<3:
        if len(users)!=0:
            num+=1
            password=raw_input("please input you password:")
            repassword=raw_input("please input you password:")
            if len(password)==0 or password!=repassword:
                print "您输入的密码不符合规则，请重新输入"
                break
            else:
                f.write("%s:%s\n"%(users,password))
                f.close()
                print "恭喜您注册成功"
                break
        else:
            print "您输入的用户名不正确"
            break

def login():
    f=open("C:\\Users\\xxx\\Desktop\\abcd.txt")
    cotent=f.readlines()
    f.close()
    user={}
    for use in cotent:
        name=use.rstrip("\n").split(":")[0]
        user[name]=use.rstrip("\n").split(":")[1]
    #print user
    number=0
    use_name=raw_input("please input you name:").strip()
    while number<3:
        if use_name in user:
            number+=1
            password=raw_input("请输入密码：").strip()
            password_len=len(password)
            if password==user[use_name]:
                return "恭喜您登陆成功"
                break
            else:
                if number<=2 and password_len<6:
                    print "您输入的密码过短，您还有%s机会再次输入"%(3-number)
                elif number<=2 and password_len>=6:
                    print "您输入的密码有误，您还有%s机会再次输入"%(3-number)
                elif number>=3:
                    print "三次机会已试完，该账户冻结十分钟"
        else:
             print "您输入的用户名有误，请重新提交"
             break

def  start():
    action=raw_input("请选择登陆或者注册:")
    if action=="login":
        return login()
    elif action=="registor":
        return reg()
    else:
        print "您输入有误"
result=start()
print result





















