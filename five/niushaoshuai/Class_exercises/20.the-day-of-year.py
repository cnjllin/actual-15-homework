#!/usr/bin/python
# --*-- coding:UTF-8 --*--
# how to add exception?
def if_r_or_p(y):
    if y%100==0 and y%400==0 :
        return 'R'
    elif y%100 != 0 and y%4==0 :
        return 'R'        
    else:
        pass

if __name__ == '__main__':
    Date=raw_input("please input the date eg:20140918 :")
    Y=int(Date[:4])
    M=int(Date[4:6])
    D=int(Date[6:].strip(' '))
    T=int()
    D_OF_Y=int()
    Days=list()
    if if_r_or_p(Y)=='R':
        Days=[31,29,31,30,31,30,31,31,30,31,30,31]
        for n in range(1,M):
            T+=Days[n]
            D_OF_Y=T+D
    else:
        Days=[31,28,31,30,31,30,31,31,30,31,30,31]
        for n in range(1,M):
            T+=Days[n]
            D_OF_Y=T+D
    print "The day is {} of the year".format(D_OF_Y)
