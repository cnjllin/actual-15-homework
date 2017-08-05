# 作业
### 对nginx访问日志分析，取出top10
#### 分析
# 作业
### 对nginx访问日志分析，取出top10
#### 分析
* 打开并遍历文件，分隔空格，定义到空字典   with open(xx) as f:
* 切分IP列，根据字典的get方法，计数  dic.get()
* 对字典的items遍历，使用 lambda value作为key 排行.并倒叙 




#### 测试代码

/usr/bin/env python
```
[root@kdc4 changhuawei]# python top10.py 
请输入统计排行数:10
--------top10---------
IP: 123.174.51.164  Count:6958
IP: 111.85.34.165  Count:2307
IP: 118.112.143.148  Count:1617
IP: 117.63.146.40  Count:1489
IP: 118.182.116.39  Count:1404
IP: 1.48.219.30  Count:1352
IP: 60.222.231.46  Count:1132
IP: 10.35.1.82  Count:1129
IP: 27.227.163.200  Count:943
IP: 58.253.6.133  Count:880


[root@kdc4 changhuawei]# python top10.py 
请输入统计排行数:5
--------top5---------
IP: 123.174.51.164  Count:6958
IP: 111.85.34.165  Count:2307
IP: 118.112.143.148  Count:1617
IP: 117.63.146.40  Count:1489
IP: 118.182.116.39  Count:1404
[root@kdc4 changhuawei]# 

```* 打开并遍历文件，分隔空格，定义到空字典   with open(xx) as f:
