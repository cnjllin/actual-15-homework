#!/usr/bin/env python
#encoding:utf-8
#changhuawei 513314416@qq.com
#201708011439


#file_path = "/root/15/02/access.txt"

with open("/root/15/02/access.txt") as f:
    dic = {}
    for line in f:
        arr = line.split(' ')
        ip = arr[0]
        dic[(ip)] = dic.get((ip),0) + 1
    items = dic.items()
    backitems=[[v[1],v[0]] for v in items] 
    print backitems.sort() 
    #for k,v in dic.items():
    #print items
    
#print sorted(items)


