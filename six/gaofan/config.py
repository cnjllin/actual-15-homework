#"dialect+driver://username:password@host:port/database"
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'passw0rd'
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'reboot_15'
SQLALCHEMY_DATABASE_URI ='{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
                    DIALECT,DRIVER,USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
