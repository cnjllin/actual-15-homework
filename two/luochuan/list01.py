a = ['abc',{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},'bbc','dawsda']

print a

a.append('123')

print a

a.insert(3,'123456')

print a

b = ['aac','bbc','ccn','ddda']
print a+b

print a [-2]
print type(a[-2])
print a [0]

print a [1:3]

for x in a:
    print 'hello %s'  %x

del b [0]
print b

b.remove('bbc')
print b

print b.pop()


