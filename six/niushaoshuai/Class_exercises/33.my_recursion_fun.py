#!/usr/bin/python
'''
def recursion(mytime):
    if mytime > 0:
        print "least %d" % (mytime)
        mytime-=1
        return recursion(mytime)
print recursion(10)
'''
def recursion(mytime):
    if mytime > 0 :
        return mytime + recursion(mytime-1)
    else:
        return 0

print recursion(10)
