from typing import Self
import scrapy
from scrapy.http import Response


class CharactersSpider(scrapy.Spider):
    """Spider to crawl Characters."""

    name = "characters"
    start_urls = []

    def parse(self: Self, response: Response):
        pass
