"""
Scrape qiche365 car recall news
"""
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from carnews import CarNews


class Qiche365Spider(CrawlSpider):

    name = "qiche365"
    allowed_domains = ["www.qiche365.org.cn"]
    start_urls = ["http://www.qiche365.org.cn/index/recall/recall.jsp"]
    rules = (
            Rule(
                SgmlLinkExtractor(restrict_xpaths='//form/div'),
                callback="parse_news",
                follow=True),
            )

    def __init__(self):
        super(Qiche365Spider, self).__init__()
        #using a list to collect items
        self.news_list = []

    def parse_news(self, response):
        x = HtmlXPathSelector(response)

        self.news_list = []
        #nested selectors
        for recall_line in x.select('//div[@class="recall_Line"]'):
            news = CarNews()
            news['url'] = recall_line.select('div[@class="recall_title"]/a/@href').extract()
            news['title'] = recall_line.select('div[@class="recall_title"]/a/text()').extract()
            news['time'] = recall_line.select('div[@class="recall_time"]/text()').extract()
            news['source'] = ""
            self.news_list.append(news)

        return self.news_list

SPIDER = Qiche365Spider()
