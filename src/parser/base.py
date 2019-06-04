from html.parser import HTMLParser
from abc import abstractmethod

class ParserBase(HTMLParser):

    @abstractmethod
    def handle_starttag(self, tag, attrs):
        pass

    @abstractmethod
    def handle_endtag(self, tag):
        pass

    @abstractmethod
    def handle_data(self, data):
        pass
