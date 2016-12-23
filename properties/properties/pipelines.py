# coding:utf-8
# import json
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SomePipeline(object):

    def __init__(self):
        self.file = open('item.jl', 'ab')
        self.db = MySQLdb.connect('localhost', 'root', '', 'test')

    def process_item(self, item, spider):
        for x in item.get('imgInfo'):
            print x
            sql = '''insert into imgDB values("%s","%s")''' % (
                x.get('title').encode('utf-8'), x.get('imgUrl').encode('utf-8'))
            cursor = self.db.cursor()

            try:
                cursor.execute(sql.encode('utf-8'))
                self.db.commit()
            except:
                self.db.rollback()
            self.file.write(sql)

        # line = json.dumps(dict(item), sort_keys=True,
        #                   indent=4, ensure_ascii=False) + '\n'
        return item

    def close_spider(self, spider):
        self.file.close()
        self.db.close()
