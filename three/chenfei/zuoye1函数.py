#!/usr/bin/python
#coding:utf-8
#import login,sgin

def start():
    action = raw_input("请输入sign/login:").strip()
    if action == "login":
      from config.login import login
      login()
    else:
      from config.sign  import sign
      sign()
start();
