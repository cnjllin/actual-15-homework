#!/usr/bin/env python
#encoding: utf-8
#name:changhuawei 
#eml:513314416@qq.com
#time:201707232200
import sys
f = open('/tmp/yonghu.txt','a+')
username = raw_input("请输入用户名: ").strip()

while True:
    passwd = raw_input("请设置密码: ").strip()
    passwd1 = raw_input("请确认密码: ").strip()
    if passwd == passwd1:
        print "注册用户{}成功".format(username)
        break
    else:
    	print "请重试"
        sys.exit() 
aa = "{}:{}\n".format(username,passwd)
f.write(aa)
f.close()
