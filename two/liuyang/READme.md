#### 作业说明
- zuoye.py为程序代码

- 作业流程图.png为作业流程图

- 代码执行结果

#### 作业要求及思路

- 作业要求：

    - 打印access.log中前10个访问网站次数最多的IP

- 作业思路：

    - 读取access.log文件内容
  打开文件 open('文件绝对路径','读取权限，一般读写用a+')
  
    - 读取后关闭文件，以防忘记关闭文件，占用系统资源 
    
      -  一般用 with ..open..，打开后自动关闭文件
  with open('access.txt','a+') as f:
      - f.read()读取文件所有内容
      - f.readline()读取一行内容
  
    - 循环获取的文件内容 for line in f: 生成temp_dict,ip:对应出现次数

    - 因为dict没有顺序，所以将dict转成list对出现次数进行排序

    - 冒泡排序，速度比较快，因为要取出现次数多的前10，所以简单冒泡10次（看之前视频想到的排序方法）
