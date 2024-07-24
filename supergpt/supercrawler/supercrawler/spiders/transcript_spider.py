from typing import Self, List
import scrapy
from scrapy.http import Response


class TranscriptSpider(scrapy.Spider):
    """Spider to crawl Transcript."""

    name = "transcript"
    start_urls = []


    def __init__(self: Self, episodes: List[str], *args, **kwargs):
        super(TranscriptSpider, self).__init__(*args, **kwargs)
        for episode in episodes:
            self.start_urls.append(f"http://supernaturalwiki.com/{episode}_(transcript)")

    def parse(self: Self, response: Response):
        pass
