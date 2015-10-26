# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect("localhost", "root", "cwy911019", "spider", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO spider_items (area, salary, link) 
                                VALUES (%s, %s, %s)""",
                                (item['area'][0].encode('utf-8'), 
                               item['salary'][0].encode('utf-8'),
                               item['link'].encode('utf-8')))
         
                       

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item


    
  
    

