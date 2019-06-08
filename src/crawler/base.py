from abc import abstractmethod
from typing import List
from urllib import request

class CrawlerBase:

    def __init__(self, urls: List[str], parser: any):
        self.urls = urls
        self.requests = request
        self.parser = parser
    
    @abstractmethod
    def activate(self):
        pass

if __name__ == "__main__":
    pass