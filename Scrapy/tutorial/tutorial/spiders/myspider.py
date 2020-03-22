import scrapy

class MySpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    
    def start_requests(self):
        yield scrapy.Request('http://www.example.com/categories/%s' % self.category)


    def start_requests(self):
        yield scrapy.Request('http://www.example.com/1.html', self.parse)
        yield scrapy.Request('http://www.example.com/2.html', self.parse)
        yield scrapy.Request('http://www.example.com/3.html', self.parse)
    
    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield {"title": h3}

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback = self.parse)