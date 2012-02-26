#encoding: utf-8
"""
Scrape qiche365 car recall news
"""
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from carnews import CarNews
from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url


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
        """
        Extract multiple items from a list in each page. Note that
        we don't follow the links to extract the news content.
        """
        x = HtmlXPathSelector(response)
        base_url = get_base_url(response)

        self.news_list = []
        #nested selectors
        for recall_line in x.select('//div[@class="recall_Line"]'):
            news = CarNews()
            news['title'] = recall_line.select('div[@class="recall_title"]/a/text()').extract()
            if not news['title']:
                continue
            relative_url = recall_line.select('div[@class="recall_title"]/a/@href').extract()[0]
            news['url'] = urljoin_rfc(base_url, relative_url)
            news['time'] = recall_line.select('div[@class="recall_time"]/text()').extract()
            news['source'] = u"中国汽车召回网"
            news['topic'] = u"汽车"
            self.news_list.append(news)

        return self.news_list

SPIDER = Qiche365Spider()
