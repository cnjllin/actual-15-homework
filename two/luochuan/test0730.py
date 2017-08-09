

users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},{'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},{'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}]


print users

a = []
b = len(users)
NAME = raw_input('please input your name :')


for i in range(0,b-1):
    if NAME == users[i]["name"]:
        password = raw_input('please input your password :')
        if users[i].get("passwd") == password :
            a.append(users[i])
        else :
            print 'the password is not exist'
    else :
        continue
print a