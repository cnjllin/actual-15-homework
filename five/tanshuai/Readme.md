
# 一、 作业
### Flask基于MySQL存储用户信息，快速实现用户的增删改查操作

# 二、技术细节拆分

### 2.1 数据库相关设计与使用说明

**1. 用户表设计**

创建一个reboot15数据库： 
create database reboot15 character set utf8;

建表，username字段加上唯一约束
```
CREATE TABLE `user` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL unique,
  `password` varchar(100) NOT NULL,
  `sex` int(10) DEFAULT NULL,
  `age` int(10) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `role` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
**2. 操作数据库的功能模块设计**
>创建一个数据库操作函数，存入dbutils.py文件，供其他程序调用，功能定义如下：

1. 函数接收三个参数：sql，args，fetch
2. 参数说明：
    * sql：接收前端拼接sql语句
    * args：接收一个元组，default：空元组
    * fetch：
        * 默认True，即执行：查询指令
        * 赋值False时，即执行：添加/更新/删除指令

>具体代码实现：

```
def execute_sql(sql, args=(), fetch=True):
    conn = None
    count = 0
    rt_list = []
    try:
        # 创建一个mysql连接
        conn = mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='reboot15', charset='utf8')
        # 获取游标
        cur = conn.cursor()
        if fetch:
            # 执行查询指令
            count = cur.execute(sql, args)
            rt_list = cur.fetchall()
        else:
            # 执行增/删/改指令
            count = cur.execute(sql, args)
            conn.commit()
    except Exception as e:
        print 'Error %d: %s' % (e.args[0], e.args[1])
    finally:
        if conn:
            conn.close()
    return count, rt_list
```

>数据库模块使用方法说明

使用规则：
调用execute_sql函数，该函数默认执行sql查询操作，如果需要执行sql“增/删/改”操作，更改参数fetch=False即可；

** 查询所有用户**
```
sql = "select * from user"
count, rt_list = execute_sql(sql=sql)
print count, rt_list
```
** 增加一个用户**
```
sql = "insert into user(username,password,sex,age,phone,email,role) values(%s,%s,%s,%s,%s,%s,%s)"
args = ('谭帅03','123456',1,27,'18512341234','185@185.com',1)
count, rt_list = execute_sql(sql=sql, args=args, fetch=False)
print count, rt_list
```
** 删除一个用户**
```
sql = 'delete from user where id=%s'
args = (1,)
count, rt_list = execute_sql(sql=sql, args=args, fetch=False)
print count, rt_list
```

** 更新一个用户**
```
sql = "update user set username=%s,password=%s,sex=%s,age=%s,phone=%s,email=%s,role=%s where id=%s"
args = ('谭帥03','123456',1,27,'18512341234','185@185.com',1,15)
count, rt_list = execute_sql(sql=sql, args=args, fetch=False)
print count, rt_list
```

### 2.2 用户的注册、登录、列表展示、更新、删除功能和前后端实现，请观看我的录制视频；
百度网盘链接:http://pan.baidu.com/s/1nvsnuYH  密码:d9dx
