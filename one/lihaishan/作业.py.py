#coding=utf-8
number=0
name=raw_input("请输入用户名：")
while number<3:
    if name=="李海山":
        number+=1
        password=raw_input("请输入密码：")
        password_len=len(password)
        if password=="123456":
            print "恭喜您登陆成功"
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


