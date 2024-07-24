from typing import Self, List
import scrapy
from scrapy.http import Response


class QuotesSpider(scrapy.Spider):
    """Spider to crawl Quotes."""

    name = "quotes"
    start_urls = []

    def __init__(self: Self, episodes: List[str], *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"http://supernaturalwiki.com/{episode}" for episode in episodes]

    def parse(self: Self, response: Response):
        pass
