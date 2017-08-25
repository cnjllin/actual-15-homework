from apps import app
from apps import db
from apps.models import Users,Nginxlog


def add_nginx_log():
    with open(app.config['LOG'], 'r') as f:
        ip = [(x.split(" ")[0],x.split(" ")[6],x.split(" ")[8]) for x in f]
        #for i in ip:

         #   user = Nginxlog(ip=i[0], url=i[1], status=i[2], counts="null")
         #   db.session.add(user)
         #   db.session.commit()
        #for i in ip:
        #    print i[0]

        #print {x for x in ip[0]}
        #a = ((x,ip.count(x)) for x in {i[0] for i in ip})
        #for i in a:
        #    print i
        iplist = []
        for i in ip:
             iplist.append(i[0])

        iplist2 = []
        for  i in iplist:
            if i in iplist2:
                continue
            else:
                iplist2.append(i)

        iplist3 = []

        for i in iplist2:
            iplist3.append((i,iplist.count(i)))

        for i in range(0, len(iplist3)):
            for j in range(i + 1, len(iplist3)):
                if iplist3[i][1] > iplist3[j][1]:
                    iplist3[i], iplist3[j] = iplist3[j], iplist3[i]

        iplist4 = iplist3[-10:]
        iplist4.reverse()



#add_nginx_log()


def query():
    user = Nginxlog.query.paginate(1,3 ,False)

    print user.url
    #for i in user:
    #    print i.url
#query()