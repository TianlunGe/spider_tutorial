import scrapy


class finance_spider(scrapy.spiders.Spider):
    name = 'yahoo'
    allowed_domains = ['yahoo.com']
    start_urls = ['https://finance.yahoo.com/quote/AAPL/financials?p=AAPL']

    def parse(self, response):
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)