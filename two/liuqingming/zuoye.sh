time awk 'BEGIN{FS="[- ]+"}{a[$1]+=1}END{for(i in a)printf ("%-20s  %10d\n",i,a[i])|"sort -rn -k2|head -n 10" }' /root/access.txt
