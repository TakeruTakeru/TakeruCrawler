from abc import abstractmethod
from typing import List
import requests

class CrawlerBase:

    def __init__(self, urls: List[str], parser: any):
        self.urls = urls
        self.requests = requests
        self.html_parser = parser
    
    @abstractmethod
    def activate(self):
        pass

if __name__ == "__main__":
    pass