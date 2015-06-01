# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
import chardet
import MySQLdb.cursors
from scrapy.exceptions import DropItem
from scrapy.http import Request
from twisted.enterprise import adbapi
from scrapy.contrib.pipeline.images import ImagesPipeline

class Tc58Pipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',user='root',passwd='gs123456',db='scrapy',host='192.168.2.201',port=3306,charset="utf8",cursorclass = MySQLdb.cursors.DictCursor)
        # self.conn = MySQLdb.connect(user='root',passwd='gs123456',db='scrapy',host='192.168.2.201',port=3306,charset="utf8")
        # self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item
        '''
        title = item['title'][0]
        car_config = item['config'][0]
        name = item['name'][0]
        telephone = item['telephone'][0]
        address = item['address'][0]
        release_time = item['release_time'][0]
        price = item['price'][0]
        link = item['link']
        try:
            self.cursor.execute("insert into sell_car_info(title,car_config,name,telephone_num,addrs,release_time,prices,info_src,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    [title,car_config,name,telephone,address,release_time,price,'58',link])
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item
        '''
    def _conditional_insert(self, tx, item):
        if item.get('title'):
            for i in range(len(item['title'])):
                title = item['title'][i]
                try:
                    car_config = item['config'][i]
                except:
                    car_config = ''
                try:
                    name = item['name'][i]
                except:
                    name = ''
                try:
                    telephone = item['telephone'][i]
                except:
                    telephone = ''
                try:
                    release_time = item['release_time'][i]
                except:
                    release_time = ''
                try:
                    price = item['price'][i]
                except:
                    price = ''
                try:
                    link = item['link']
                except:
                    link = ''
                try:
                    print type(item['address'][i])
                    #print chardet.detect(str(item['address'][i]))
                    address = u'江苏' + item['address'][i]

                except:
                    if 'nj.58.com' in link:
                        address = '江苏南京'
                    elif 'su.58.com' in link:
                        address = '江苏苏州'
                    elif 'wx.58.com' in link:
                        address = '江苏无锡'
                    elif 'cz.58.com' in link:
                        address = '江苏常州'
                    elif 'xz.58.com' in link:
                        address = '江苏徐州'
                    elif 'nt.58.com' in link:
                        address = '江苏南通'
                    elif 'yz.58.com' in link:
                        address = '江苏扬州'
                    elif 'yancheng.58.com' in link:
                        address = '江苏盐城'
                    elif 'ha.58.com' in link:
                        address = '江苏淮安'
                    elif 'lyg.58.com' in link:
                        address = '江苏连云港'
                    elif 'taizhou.58.com' in link:
                        address = '江苏泰州'
                    elif 'suqian.58.com' in link:
                        address = '江苏宿迁'
                    elif 'zj.58.com' in link:
                        address = '江苏镇江'
                    elif 'shuyang.58.com' in link:
                        address = '江苏沭阳'
                    elif 'dafeng.58.com' in link:
                        address = '江苏大丰'

                try:
                    is_seller = item['is_seller'][i]
                except:
                    is_seller = '商家'
                try:
                    tx.execute("select id from sell_car_info where url='%s'" % link)
                    result = tx.fetchall()
                    if not result:
                        try:
                            tx.execute("insert into sell_car_info(title,car_config,name,telephone_num,addrs,release_time,prices,is_seller,info_src,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(title,car_config,name,telephone,address,release_time,price,is_seller,'58',link))
                        except MySQLdb.Error, e:
                            print "Insert error %d: %s" % (e.args[0], e.args[1])
                    else:
                        print "The car information is already in the database."
                except MySQLdb.Error,e:
                    print "Select error %d: %s" % (e.args[0], e.args[1])

