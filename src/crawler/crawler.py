from src.crawler.base import CrawlerBase
from typing import List
from logger import logger
from src.parser.html_parser import BasicHTMLParser

class OnePieceCrawler(CrawlerBase):

    def __init__(self, urls: List[str], parser: any):
        super().__init__(urls, parser())

    def _request(self):
        for url in self.urls:
            response = self.requests.get(url)
            self.html_parser.feed(response.text)

    def activate(self):
        self._request()

if __name__ == "__main__":
    urls = ['https://one-piece.com/news/category.html?cc=71',]
    op_crawler = OnePieceCrawler(urls, BasicHTMLParser)
    op_crawler.activate()