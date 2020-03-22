import scrapy

class itemSpider(scrapy.Spider):
    # name = '<a href="http://www.scrapyd.cn/doc/149.html" target="_blank"><u>listSpider</u></a>'
    name = "content"
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        mingyan = response.css('div.quote') #提取首页所有的名言，保存至变量
        for v in mingyan:

            text = v.css('.text::text').extract_first() #提取名言
            autor = v.css('.author::text').extract_first() #提取作者
            tags = v.css('.tags .tag::text').extract() #提取标签
            tags = ','.join(tags) #数组转换为字符串
        
            fileName = '%s-语录.txt' % autor #攫取的内容存入文件，文件名为

            with open(fileName, "a+") as f: #追加写入文件
                f.write(text) #定稿名言内容
                f.write('\n') #换行
                f.write('标签：' + tags) #写入标签
                f.write('\n--------\n')
                f.close() #关闭文件操作