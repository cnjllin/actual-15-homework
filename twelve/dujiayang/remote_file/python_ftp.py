#!/usr/bin/env python
#coding:utf8
#tornado --facebook 轻量级，工业级的web框架，可以学到web框架的底层,tornado有很多
#的模块，直接用就行。
#django，重量级的不适合刚入门的pythoner
# 1 pip install tornado
#__author__ = 'xinlan'

from tornado import web,ioloop,httpserver

#逻辑处理函数
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
       # self.write('你好') #返回数据
        self.render('index.html') #返回数据
       #找到所有存在的盘符
        
#路由
application = web.Application([
        (r"/index",MainPageHandler),
    ])
#socket服务
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(6969)
    ioloop.IOLoop.current().start()





