username = 'lc'
password = '123456'
num = 0


while num <= 2:
    user = raw_input('please input your usrname:')
    passwd = raw_input('please input your password:')
    if user != username:
        print 'your username or password is not currect'
        num += 1
        continue
    elif user == username and passwd == password:
        print 'welcome %s' %username
        break
    elif len(passwd) != 6:
        print 'the length of the password is not currect'
        num += 1
        continue
    elif passwd != password :
        print 'your password is not currect'
        num += 1
        continue
else :
    print 'wrong input,you have exit'




