from typing import Self, List
import scrapy
from scrapy.http import Response
from scrapy.crawler import CrawlerProcess

class LibrarySpider(scrapy.Spider):
    """Spider to crawl list of difinitions."""

    name = "library"
    start_urls = [
        "http://supernaturalwiki.com/Category:Library",
    ]

    def parse(self: Self, response: Response):
        names = []
        sections = response.xpath("/html/body/div/div[1]/div/div[2]/div[4]/div[2]/div[2]/div/div/div")
        for section in sections:
            for div in section.xpath("ul/li"):
                if "title" in div.xpath("a").attrib:
                    names.append(div.xpath("a").attrib["title"])
        process = CrawlerProcess()
        process.crawl(DefinitionsSpider, definitions=names)


class DefinitionsSpider(scrapy.Spider):
    """Spider to crawl Definitions."""

    name = "definitions"
    start_urls = []
    
    def __init__(self: Self, definitions: List[str], *args, **kwargs):
        super(DefinitionsSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"http://supernaturalwiki.com/{definition}" for definition in definitions]

    def parse(self: Self, response: Response):
        pass
