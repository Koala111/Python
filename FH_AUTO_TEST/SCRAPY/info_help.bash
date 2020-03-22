scrapy startproject news #创建一个项目

You can start your first spider with:
    cd news
    scrapy genspider example example.com #建立一个爬虫模板
	
scrapy genspider -t crawl news163 news.163.com
Created spider 'news163' using template 'crawl' in module:


XXX does not support field: xxx  #可能 是制表符号问题，需要排查

scrapy crawl news163 #执行爬虫任务