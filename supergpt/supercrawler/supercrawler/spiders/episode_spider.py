from typing import Self
import scrapy
from scrapy.http import Response
from scrapy.crawler import CrawlerProcess
from supergpt.supercrawler.supercrawler.spiders import (
    QuotesSpider,
    SynopsisSpider,
    TranscriptSpider
)


class EpisodeSpider(scrapy.Spider):
    """Spider for crawling episode list."""

    name = "episodes"
    start_urls = [
        "http://supernaturalwiki.com/Category:Canon"
    ]

    def parse(self: Self, response: Response):
        names = []
        links_section = "/html/body/div/div[1]/div/div[2]/div[4]/div[2]/div[2]/div/div/div"
        links = response.xpath(links_section)[:10]
        for link in links:
            for episode in link.xpath("ul/li"):
                name = episode.xpath("a").attrib["title"]
                names.append(name)

        process = CrawlerProcess()
        process.crawl(QuotesSpider, episodes=names)
        process.crawl(TranscriptSpider, episodes=names)
        process.crawl(SynopsisSpider, episodes=names)
        
