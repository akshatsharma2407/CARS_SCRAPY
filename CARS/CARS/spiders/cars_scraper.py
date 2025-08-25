import scrapy


class CarsScraperSpider(scrapy.Spider):
    name = "cars_scraper"
    allowed_domains = ["cars.com"]
    start_urls = ["https://cars.com"]

    def parse(self, response):
        pass
