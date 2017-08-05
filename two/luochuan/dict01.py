b = {'age':18,'job':'sa','city':'beijing','gf':{'age':20,'job':'th','city':'shenzhen'}}
print b

print b.values()

print b['age']

print b['gf']
print b['gf']['age']

b['gf']['age'] = 23

print b['gf']['age']

b['gf']['name'] = 'lll'
print b['gf']

del b['city']
print b

del b['gf']['city']
print b

