#encoding:utf-8
"""
Scrape biatuo car recall news
"""
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from carnews import CarNews

class CarNewsSpider(CrawlSpider):

    name = "biauto"
    allowed_domains = []
    start_urls = ["http://news.bitauto.com/newslist/a886-1.html"]
    rules = (
            Rule(
                SgmlLinkExtractor(
                    #allow=r".*",
                    #use the following xpath to crawl the start page
                    #restrict_xpaths='//div[@id="newslist"]'),
                    #use the following xpath to crawl multiple pages
                    restrict_xpaths='//div[@class="line_box all_newslist mainlist_box"]'),
                callback="parse_news",
                follow=True),
            )

    def parse_news(self, response):
        """
        Extract one item from one page
        """
        x = HtmlXPathSelector(response)
        if "recall_" not in response.url:
            return None

        news = CarNews()
        news['url'] = response.url
        news['title'] = x.select('//h1[@class="con"]//text()').extract()
        news['topic'] = u"汽车"
        news['time'] = x.select('//li[@id="time"]/text()').extract()
        news['source'] = u"易车网"
        # Use string() or //text() to select nested text
        # Temporarily disable the content field to simplify output
        #news['content'] = [e.strip() for e in x.select('//div[@class="con_main"]//text()').extract()]

        return news

SPIDER = CarNewsSpider()
