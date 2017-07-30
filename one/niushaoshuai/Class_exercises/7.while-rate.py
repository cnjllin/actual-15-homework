#!/usr/bin/python
# -*- coding:UTF-8 -*-
def double(m,r):
    money=m*1.0
    years=0
    while money/m<2:
        money=money*(1+r)
        years+=1
    return years
if __name__ ==  '__main__':
    benjin=float(raw_input("请输入你的本金："))
    lilv=float(raw_input("请输入当年的利率："))
    print "After %2f years ,you can double " % double(benjin,lilv)
