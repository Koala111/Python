import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'job'

    start_urls = ['https://search.51job.com/list/180200%252C00,000000,0000,00,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        for info in response.xpath('//*[@id="resultList"]/div'):
            yield {
                '职位名': info.xpath('p/span/a/@title').extract_first(),
                '公司名': info.xpath('span/a/@title').extract_first(),
                '工作地点': info.css('span.t3::text').extract_first(),
                '薪酬': info.css('span.t4::text').extract_first(),
                '发布时间': info.css('span.t5::text').extract_first(),
            }
        for a in response.css('li.bk a'):
            yield response.follow(a, callback = self.parse)
