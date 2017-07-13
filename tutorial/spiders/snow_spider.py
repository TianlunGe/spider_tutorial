import scrapy
from ..items import balance_item

class snow_spider(scrapy.spiders.Spider):
    name = 'snowball'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://xueqiu.com/S/AAPL/balance']

    def parse(self, response):
        temp = balance_item()
        temp['stock_name'] = response.css('.stockTitle').extract()
        filename = response.url.split('/')[-2] + '.txt'
        with open(filename, 'w') as f:
            f.write(str(temp))
