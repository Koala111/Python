# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

class NewsPipeline(object):

    #魔法函数
    def __init__(self): #启动的第一个函数
        self.file=open('news_data.csv','wb')
        self.exporter=CsvItemExporter(self.file,encoding='utf-8')
        self.exporter.start_exporting()
        
    def close_spider(self,spider): #关闭函数,把进程关闭,文件关闭
        self.exporter.finish_exporting()
        self.file.close()
        
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
