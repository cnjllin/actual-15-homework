#coding:utf-8

DEBUG = True

args = { 'HOSTNAME':'localhost',
        'DIATECT':'mysql',
        'DRIVER':'mysqldb',
        'USER':'root',
        'PASSWD':'passw0rd',
        'PORT':'3306',
        'DB':'reboot_15'
       }

SQLALCHEMY_DATABASE_URI = '{DIATECT}+{DRIVER}://{USER}:{PASSWD}@{HOSTNAME}:{PORT}/{DB}?charset=utf8'.format(**args)

SQLALCHEMY_TRACK_MODIFICATIONS = False

fields = [ 'user_id',
           'user_name',
           'user_pass',
           'user_sex',
           'user_age',
           'user_email',
           'user_role'
         ]

SECRET_KEY = 'aqdwqfqwfbr214523tvhgr'
