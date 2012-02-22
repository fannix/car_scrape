"""
Scrape car recall news
"""
from scrapy.item import Item, Field
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class CarNews(Item):
    """
    Data structure for car news
    """
    url = Field()
    title = Field()
    topic = Field()
    time = Field()
    source = Field()
    content = Field()

class CarNewsSpider(CrawlSpider):

    name = "biauto"
    #allowed_domains = ['news.biauto.com']
    allowed_domains = []
    #allowed_domains = [
            #"news.biauto.com/recall_gn",
            #"news.biauto.com/recall_gw",
            #"news.biauto.com/newslist" ]
    #news_domains = [
            #"news.biauto.com/recall_gn",
            #"news.biauto.com/recall_gw"]
    start_urls = ["http://news.bitauto.com/newslist/a886-1.html"]
    rules = (
            Rule(
                SgmlLinkExtractor(
                    #allow=r".*",
                    restrict_xpaths='//div[@class="line_box all_newslist mainlist_box"]'),
                callback="parse_news",
                follow=True),
            #Rule(SgmlLinkExtractor(allow=('newslist/a886-2\.html')))
            )

    def parse_news(self, response):
        x = HtmlXPathSelector(response)

        #print "----", self.allowed_domains

        print "----", response.url
        if "recall_" not in response.url:
            return None

        news = CarNews()
        news['url'] = response.url
        news['title'] = x.select('//a[@class="yuanchuang"]/text()').extract()
        news['topic'] = ""
        news['time'] = x.select('//li[@id="time"]/text()').extract()
        news['source'] = ""
        # Use string() or //text() to select nested text
        news['content'] = x.select('//div[@class="con_main"]//text()').extract()
        print news['title']

        return news

SPIDER = CarNewsSpider()
