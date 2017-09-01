# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from werkzeug.security import generate_password_hash,  check_password_hash

#加盐加密密码
def set_password(user_info):
    user_info['passwd']= generate_password_hash(user_info.get('passwd'))
    return user_info
#判断密码是否匹配 
def check_password(user_info1,user_info2):
    '''
    user_info1为实际存储的用户,user_info2为待验证密码用户,都为字典存储，密码匹配返回True
    '''
    return check_password_hash(user_info1.get('passwd'),user_info2.get('passwd'))
