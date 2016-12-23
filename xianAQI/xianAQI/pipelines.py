# -*- coding: utf-8 -*-
import MySQLdb


class XianaqiPipeline(object):

    def open_spider(self, spider):
        self.db = MySQLdb.connect('localhost', 'root', '', 'test')

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        sql = '''insert into environment VALUES('%s','%s',%s,'%s','%s',%s,%s,%s,%s,%s,%s,%s)''' %\
            (item['city'], item['date'], item['aqi'], item['ranges'],
             item['level'], item['pm25'], item['pm10'], item['so2'],
             item['co'], item['no2'], item['o3'], item['rank'])

        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        return item

    def close_spider(self, spider):
        self.db.close()
