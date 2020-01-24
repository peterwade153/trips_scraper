# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import MapCompose


def clean_price(price):
    if price:
        price = price.replace("US$ ", "")
        return float(price.replace(",", ""))


def remove_whitespaces(value):
    if value:
        return value.strip()


def format_days(days):
    if days:
        return int(days)


class TripItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_whitespace))
    price = scrapy.Field(input_processor=MapCompose(clean_price))
    activities = scrapy.Field()
    tour_type = scrapy.Field()
    next_departure_date = scrapy.Field()
    days = scrapy.Field(input_processor=MapCompose(format_days))
    country = scrapy.Field()
