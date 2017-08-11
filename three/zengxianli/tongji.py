#coding:utf-8

content="who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forg otten past you can’t go on well in lifeuntil you let go of your past failures and heartaches"

result={}
res={}

for s in content.split(" "):
    if s in result:
        result[s]+=1
    else:
        result[s]=1




        
for k,v in result.items():
    res.setdefault(v,[])
    res[v].append(k)


count=0
f=open('tongji.html','a+')
f.write("<html>")
f.write("<table style='height:30px;' border='3' cellspacing='3' cellpadding='3'>")
f.write("<tr><td>出现次数</td><td>单词</td></tr>")
while count<4:
    key=max(res.keys())
    for word in res[key]:
        f.write("<tr><td>%s</td><td>%s</td></tr>" % (key,word))
    res.pop(key)
    count=count+1
f.write("</table></html>") 
f.close()   
