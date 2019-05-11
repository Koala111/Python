import scrapy
from ImageSpider.items import ImagespiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImagespiderItem() # 实例化item
        imgurls = response.css(".post img::attr(src)").extract() # 存入多张图片的集合
        item['imgurl'] = imgurls
        yield item
        pass