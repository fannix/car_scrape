from scrapy.item import Item, Field

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
