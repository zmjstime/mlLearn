# coding:utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


db = MySQLdb.connect('localhost', 'root', '', 'test')
cursor = db.cursor()
# cursor.execute("insert into imgDB values('wwwwwww', '2dsdad')")
# ss = '''insert into imgDB values("我的天，战斗民族的带娃日常 厉害了我的", "Http://Storage.Slide.News.Sina.Com.Cn/Slidenews/77_Ori/2016_49/74766_740440_595168.Gif")'''
# cursor.execute(ss.encode('utf-8'))

cursor.execute('select * from environment')

data = cursor.fetchall()

# db.commit()

print len(data), type(data)
# print data
print 'all:'
for x in data:
    print x[0], x[1], x[2], x[3], x[4]

db.close()
