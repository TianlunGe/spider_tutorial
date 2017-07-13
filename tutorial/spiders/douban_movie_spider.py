import scrapy


class movie_spider(scrapy.spiders.Spider):
    name = "douban_movie"
    allowed_domains = ["douban.com"]
    start_urls = [
        'https://movie.douban.com'
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
