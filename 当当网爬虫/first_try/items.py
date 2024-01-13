# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstTryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name=scrapy.Field()
    picture=scrapy.Field()
    auther_name=scrapy.Field()
    Press=scrapy.Field()
    price=scrapy.Field()
    hyperlink=scrapy.Field()
    pass
