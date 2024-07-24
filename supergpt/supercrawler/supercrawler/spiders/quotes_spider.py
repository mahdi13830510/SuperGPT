from typing import Self, List
import scrapy
from scrapy.http import Response


class QuotesSpider(scrapy.Spider):
    """Spider to crawl Quotes."""

    name = "quotes"
    start_urls = []

    def __init__(self: Self, episodes: List[str], *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        for episode in episodes:
            self.start_urls.append(f"http://supernaturalwiki.com/{episode}")

    def parse(self: Self, response: Response):
        pass
