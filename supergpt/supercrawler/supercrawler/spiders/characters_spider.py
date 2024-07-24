from typing import Self, List
import scrapy
from scrapy.http import Response


class CharacterListSpider(scrapy.Spider):
    name = "characters_list"
    start_urls = [
        "http://supernaturalwiki.com/Category:Characters",
        "http://supernaturalwiki.com/index.php?title=Category:Characters&pagefrom=Sid#mw-pages",
    ]

    def parse(self: Self, response: Response):
        pass


class CharactersSpider(scrapy.Spider):
    """Spider to crawl Characters."""

    name = "characters"
    start_urls = []

    def __init__(self: Self, characters: List[str], *args, **kwargs):
        super(CharactersSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"http://supernaturalwiki.com/{character}" for character in characters]

    def parse(self: Self, response: Response):
        pass
