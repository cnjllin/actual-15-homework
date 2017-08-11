tmp={'q':4,'g':4,'b':4,'w':5,'m':5,'n':5,'e':6,'v':6,'r':7,'a':7,'c':7,'k':7,'t':8,'g':8,'y':9,'p':9}
a=[4,5,6,7,8,9]
for i in range(0,19):
    for k,v in tmp.items():
        if v==a[i]:
            print "%s,%s" % (k,tmp.pop(k))
             
        else:
            continue
