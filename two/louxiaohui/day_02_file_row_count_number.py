#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys


def statistics_file_count():
    count = len(open('./test.file','a+').readlines())
    print count

statistics_file_count()

def statistics_file_count_v2():
    #count = 1
    for count,line in enumerate(open('./test.file','rU')):
        pass
        count += 1
        print count

statistics_file_count_v2()
