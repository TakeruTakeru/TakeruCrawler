from bs4 import BeautifulSoup
from logger import logger
from src.parser.base import ParserBase

class BS_Parser(BeautifulSoup, ParserBase):
    '''BeatifulSoup Wrapper Object'''

    def __init__(self, html, features='html.parser'):
        super().__init__(html, features)

    def find_all_tag(self, tag: str, **kwargs):
        return self.find_all(tag, **kwargs)

    def find_tag(self, tag: str, **kwargs):
        return self.find(tag, **kwargs)

    def _find_parents_(self, c_tag: any, p_tag: str, **kwargs):
        return c_tag.find_parents(p_tag, **kwargs)