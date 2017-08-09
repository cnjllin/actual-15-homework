
说明：

    zuoye_ip.py  统计IP地址，输出html文件
    login.py     读取/etc/passwd文件判断用户是否存在并是否添加，通过/etc/shadows验证用户是否有效,连续三次输入错误密码锁定用户。


实现思路：

    zuoye_ip.py    
    
    1. 读取日志文件，通过split获取IP列表
    2. 使用集合去重
    3. 排序取前10个IP
    4. 通过字符串拼接生成HTML表格，并写入文件


    login.py

    1. 读取/etc/passwd 返回用户名列表
    2. 读取/etc/shadows 返回密码、盐值列表
    3. 用户输入的密码+盐(2步返回的盐) 使用crypt加密后与密码(shadows密码)比较是否正确
    4. 通过shadow密码前是否有！号来获取用户是否被锁定
    
