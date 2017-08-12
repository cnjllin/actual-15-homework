#usr/bin/python
#coding:utf-8

def registration():
    user_name = raw_input("Please inpput your userName:").strip()
    user={}
    if user_name != "":
        with open("user.txt","r")as f:
            for a in f:
                a=a.strip("\n")
                user.setdefault(a.split(":")[0],a.split(":")[1])
        if user.get(user_name):
            print"This user already exist!"
        else:
            status = True
            while status:
                pwd_one = raw_input("Please input your password :")
                if len(pwd_one)>=6:
                    pwd_two = raw_input("Please input your password again :")
                    if pwd_two == pwd_one:
                        print"Welcome %s"%user_name
                        with open("user.txt","a+") as f:
                            f.write("%s:%s\n"%(user_name,pwd_one))
                            status = False
                    else:
                        print "Registration Failed , two inconsistencies"
                        continue
                else:
                    print"Failed to register, the password length is less than six"
                    continue
      
    else:
        print"The user_name is empty!"
        

def login():
    user ={}
    user_name = raw_input("Please input your name:")
    try:
        with open("user.txt","rb")as f:
            for a in f:
                a=a.strip("\n")
                user.setdefault(a.split(":")[0],a.split(":")[1])
            while user_name in user:
                pwd = raw_input("Please input your password :")
                if user.get(user_name) == pwd:
                    print"Welcome %s!"%user_name
                    break
                else:
                    print"The password is wrong"
                    continue
            else:
                print"This user doesn't exist!"
    except Exception,e:
        print e

if __name__ =='__main__':
    choice = int(raw_input("注册：1,登录：2 > ").strip())
    if choice == 1:
        registration()
    elif choice == 2:
        login()
    else:
        print("你的选择有误！")
    



