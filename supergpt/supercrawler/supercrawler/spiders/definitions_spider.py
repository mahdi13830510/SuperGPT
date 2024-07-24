from typing import Self
import scrapy
from scrapy.http import Response


class DefinitionsSpider(scrapy.Spider):
    """Spider to crawl Definitions."""

    name = "definitions"
    start_urls = []

    def parse(self: Self, response: Response):
        pass
