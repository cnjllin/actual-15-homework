#!/usr/bin/python
# --*-- coding:UTF-8 --*--
# maopao
ml=[1,4,3,5,2,6]
count=len(ml)
for i in range(0,count):
    for j in range(i+1,count):
        if ml[i]>ml[j]:
            ml[i],ml[j]=ml[j],ml[i]
print ml
