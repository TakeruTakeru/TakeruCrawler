from src.crawler.base import CrawlerBase
from typing import List
from logger import logger

class OnePieceCrawler(CrawlerBase):

    def __init__(self, urls: List[str], parser: any):
        super().__init__(urls, parser)

    def _request(self) -> any:
        for url in self.urls:
            response = self.requests.urlopen(url)
            return response

    def _initialize_parser(self, html: any):
        html_parser = self.parser(html)
        return html_parser

    def activate(self):
        parser = self._initialize_parser(self._request())
        return parser
