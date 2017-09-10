DEBUG=True

CSRF_ENABLED = True
SECRET_KEY = 'YRFRxtRJNgLbEdrpFjEuxQVFfuXPxNqK'

#PASSWD = 'qinl@#^##112'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://qinl:%s@104.199.207.83/cmdb' %(PASSWD)
#SQLALCHEMY_TRACK_MODIFICATIONS = True

DB_INFO = {
    'HOST':'192.168.78.128',
    'USER':'root',
    'PASSWD':'yutian',
    'DB':'cmdb',
    'CHARSET':'utf8',
}
DB_FIELDS = {
    'VERIFY_USER':['username','password','role','status','phone','email'],
    'USER_FIELD' : ['id','username','nickname','phone','email','role','status','createtime','lasttime'],
}