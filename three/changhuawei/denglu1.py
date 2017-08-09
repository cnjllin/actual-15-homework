#!/usr/bin/env python
#encoding: utf-8
#name:changhuawei 
data = {}
with open('/tmp/yonghu.txt') as f: 
	for line in f:
		users = line.rstrip().split(":")
		data[users[0]] = users[-1]


name1 = raw_input("plrase input your name: ").strip()
pass1 = raw_input("plrase input your pass: ").strip()
#for x in data.items():
if name1 in data:
    if data[name1] == pass1:
        print 'ok'
    else:
        print 'pass err'
else:
    print 'name err'
