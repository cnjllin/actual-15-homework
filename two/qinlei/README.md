读nginx日志排序：

    1， 取IP生产IP列表
    2， 去重，并统计重复数量
    3， 排序，取前10IP
    4， 输出结果

v1 傻瓜版


从头到尾使用for循环,冒泡排序，或插入排序，列表切面，字符串分割，实现功能，未使用高级用法


v2 中级版

使用列表生成器，集合生成器，匿名函数等实现功能



结果：

v2 运行时间 1 秒左右，v1 运行时间 1.5 秒左右

说明：

如果要追求速度，使用read一次读取全部文件到内存中运算，但这样会消耗计算机内存，并且尽量减少循环次数。
不追求速度，使用readlines读一行，处理一行。

