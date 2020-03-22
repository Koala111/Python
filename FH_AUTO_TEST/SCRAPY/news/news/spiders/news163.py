# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import NewsItem #保持与文件名子一致，不要写错了

#https://news.163.com/20/0229/22/F6JB5UKL0001899O.html
#https://news.163.com/20/0301/09/F6KEATPN000189FH.html
#https://news.163.com/20/\d+/.*?html
class News163Spider(CrawlSpider):
    name = 'news163'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://news.163.com/20/\d+/.*?html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        '''
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
        '''
        item=NewsItem()
        item['news_thread']=response.url.strip().split('/')[-1][:-5]
        self.get_title(response,item)
        self.get_time(response,item)
        self.get_source(response,item)
        self.get_source_url(response,item)
        self.get_news_body(response,item)
        self.get_url(response,item)
        return item
        
    def get_url(self,response,item):
        url=response.url
        if url:
            print('news_url:{}'.format(url))
            item['news_url']=url
            
    def get_news_body(self,response,item):
        news_body=response.css('.post_text p::text').extract()
        if news_body:
            print('news_body:{}'.format(news_body))
            item['news_body']=news_body
            
    def get_source_url(self,response,item):
        source_url=response.css('#ne_article_source::attr(href)').extract()
        if source_url:
            print('source_url:{}'.format(source_url[0]))
            item['source_url']=source_url[0]
            
    def get_source(self,response,item):
        source=response.css('#ne_article_source::text').extract()
        if source:
            print('source:{}'.format(source[0]))
            item['news_source']=source[0]
            
    def get_time(self,response,item):
        time=response.css('div.post_time_source::text').extract()
        if time:
            print('time:{}'.format(time[0].strip().replace('来源:','').replace('\u3000','')))
            item['news_time']=time[0].strip().replace('来源:','').replace('\u3000','')
        
    def get_title(self,response,item):
        title=response.css('title::text').extract()
        if title:
            print('title:{}'.format(title[0]))
            item['news_title']=title[0]
