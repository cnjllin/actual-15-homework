#!/usr/bin/python
# coding:UTF-8
import ConfigParser
def getconfig(filename,section=''):
    # 创建ConfigParser对象
    cf = ConfigParser.ConfigParser()
    # 读取文件filename
    cf.read(filename)
    # cf.items(section) 得到该section中所有的键值对
    # cf.has_section(section) 判断是否有section
    # a = 3 if 2>1 else 1;结果a=3;这是一个if表达式
    # 最终以字典的形式把该section中的内容用字典的形式展现出来
    cf_items = dict(cf.items(section)) if cf.has_section(section) else {}
    return cf_items
def setconfig(filename,section='',key='',value=''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    if not cf.has_section(section):  
        cf.add_section(section)
    cf.set(section,key,value)
    cf.write(open(filename,'w'))
def delconfig(filename,*pa):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    if len(pa) > 2 :
        print "paragram is too much"
    elif len(pa)==2 and cf.remove_option(pa[0],pa[1]):
        cf.write(open(filename,'w'))
    elif len(pa)==1 and cf.remove_section(pa[0]):
        cf.write(open(filename,'w'))
    else:
        print 'section or option is not exist'            
        
   
if __name__ == '__main__':
    conf=getconfig('im.conf','web')
    setconfig('im.conf','imlog2','port','1090')
    delconfig('im.conf','imlog2')
