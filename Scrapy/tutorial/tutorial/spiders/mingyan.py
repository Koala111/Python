import scrapy

class quotoSpider(scrapy.Spider):
    name = "quoto"
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        quoto = response.xpath('//*[@id="main"]/div')
        for q in quoto:
            text = q.xpath('span[@class="text"]/text()').extract_first()
            author = q.xpath('span/small[@class="author"]/text()').extract_first()
            tags = q.xpath('div/a[@class="tag"]/text()').extract()
            tags = ','.join(tags)
            fileName = '%s-语录.txt' % author

            with open('F:/File/%s'% fileName, "a+") as f:
                f.write(text)
                f.write('\n')
                f.write('标签：' + tags)
                f.write('\n-----------------------\n')
                f.close()
        for a in response.css('li.next a'):
            yield response.follow(a, callback = self.parse)
