Hi,

import pymysql, subprocess,os

f=open('datanames.txt','w')
c=pymysql.connect(host='localhost',user='root',passwd='amroot')
cur=c.cursor()
cur.execute('show databases')
for i in cur.fetchall():
                if (str(i[0]) == 'performance_schema' or str(i[0]) == 'information_schema'):
                                pass

                else:
                                f.write(i[0])
                                f.write('\n')
f.close()
c.close()
f1=open('datanames.txt','r')
for j in f1.read().split('\n'):
                subprocess.call('mysqldump -h localhost -u root -pamroot  {0}  > /home/admin/python/backups/{1}.sql' .format(j,j) ,shell=True,stderr=subprocess.DEVNULL)
f1.close()
subprocess.call('rsync -avze  "ssh -p 22" /home/admin/python/backups/ root@192.168.56.103:/home/python/',shell=True,stderr=subprocess.DEVNULL)

print('Backup is taken and pushed to backup server')
