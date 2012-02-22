# Scrapy settings for cars project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'cars'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['cars.spiders']
NEWSPIDER_MODULE = 'cars.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['cars.pipelines.JsonWithEncodingPipeline']
