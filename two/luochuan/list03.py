log = '124.238.248.52 - - [30/Jul/2017:15:22:42 +0800] "POST /crontab/collect HTTP/1.1" 200 151 "-" "Python-urllib/2.6" "-" "0.166" "10.3.0.136:5000" "200" "0.106"'

print log.split(' ')
print log.split(' ')[0]
print log.split(' ')[3:4]
print log.split('"')[-4:-3]


print log.split(' ')[0]
print log.split(' ')[3]
print log.split(' ')[8]

loggs = []
#loggs.append(log.split(' ')[0],log.split(' ')[3],log.split(' ')[7])
print log.split(' ')[0],log.split(' ')[3],log.split(' ')[8]


