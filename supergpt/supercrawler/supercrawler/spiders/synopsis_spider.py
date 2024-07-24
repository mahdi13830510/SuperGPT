from typing import Self, List
import scrapy
from scrapy.http import Response


class SynopsisSpider(scrapy.Spider):
    """Spider for crawling Synopsis of each episode."""

    name = "synopsis"
    start_url = []

    def __init__(self: Self, episodes: List[str], *args, **kwargs):
        super(SynopsisSpider, self).__init__(*args, **kwargs)
        for episode in episodes:
            self.start_urls.append(f"http://supernaturalwiki.com/{episode}")


    def parse(self: Self, response: Response):
        pass
