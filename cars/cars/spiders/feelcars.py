"""
Scrape qiche365 car recall news
"""
from scrapy.contrib.spiders import XMLFeedSpider
from carnews import CarNews

class FeelCarsSpider(XMLFeedSpider):

    name = "feelcars"
    allowed_domains = ["www.feelcars.com"]
    start_urls = ["http://www.feelcars.com/rss/news.xml"]
    itertag = 'item'


    def parse_node(self, response, node):
        news = CarNews()
        news['url'] = node.select('link/text()').extract()
        news['title'] = node.select('title/text()').extract()
        news['content'] = node.select('description/text()').extract()
        news['time'] = node.select('pubDate/text()').extract()

        return news

SPIDER = FeelCarsSpider()
