#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
for t1 in range(1,10):
    for t2 in range(1,10):
        t3=t1*t2
        print "%d * %d = %d" % (t1,t2,t3)
'''
#print [t1*t2 for t1 in range(1,10) for t2 in range(1,10) ]
print ["%d * %d = %d" % (t1,t2,t1*t2) for t1 in range(1,10) for t2 in range(1,10) ]
