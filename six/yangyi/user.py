# Author: tailorYang
import utils

# 添加客户
def add(user):
    execute = utils.DB()
    execute.table = 'user'
    sql = "INSERT INTO %s(%s) values(%s)" % (
    execute.table, ','.join(user.keys()), ','.join(["'%s'" % i for i in user.values()]))
    result = execute.commit(sql)
    execute.close()
    return result

# 查询指定用户所有信息
def select_one(user):
    execute = utils.DB()
    execute.table = 'user'
    sql = 'SELECT * FROM %s WHERE username = "%s"' % (execute.table, user)
    result = execute.fetch_one(sql)
    execute.close()
    return result
# 查询用户角色
def check_role(user):
    execute = utils.DB()
    execute.table = 'user'
    sql = 'SELECT role FROM %s WHERE username = "%s"' % (execute.table, user)
    result = execute.fetch_one(sql)
    execute.close()
    return result
# 查询所有用户信息
def select_all():
    execute = utils.DB()
    execute.table = 'user'
    sql= 'SELECT  *  FROM %s  ;' % (execute.table)
    result = execute.fetch_all(sql)
    return result

# 更新用户信息

def update_user(user):
    execute = utils.DB()
    execute.table = 'user'
    sql = 'UPDATE  %s SET %s WHERE id = %s;' % (
    execute.table, ','.join(["%s='%s'" % (k, v) for k, v in user.items() if k != 'id']), user['id'])
    result = execute.commit(sql)
    execute.close()
    return result

# 删除用户信息

def delete_user(id):
    execute = utils.DB()
    execute.table = 'user'
    sql = 'DELETE  FROM %s WHERE id = %s;' % (execute.table, id)
    result = execute.commit(sql)
    execute.close()
    return result
