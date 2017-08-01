def nginxIpCounter(nginxFile):
    ipCounter = { }
    with open(nginxFile) as f:
        for line in f:
            ip = line.split(" ",1)[0]
            if 6<=len(ip) <= 15:
                ipCounter[ip] = ipCounter.get(ip,0) + 1
    return ipCounter
nginxIp = { }
nginxIpBySort = { }
nginxIp = nginxIpCounter("/root/access.txt")
nginxIpBySort = sorted(nginxIp.iteritems(),key = lambda d:d[1] ,reverse = True)[:10]
for i,j in nginxIpBySort:
    print "%s => %d"%(i,j)
