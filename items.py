# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TagcheckerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    hasUniversal = scrapy.Field()
    hasClassic = scrapy.Field()
    hasTagManager = scrapy.Field()
