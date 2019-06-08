import sys
from src.crawler.crawler import OnePieceCrawler
from src.parser.parser import BS_Parser
from logger import logger


if __name__ == "__main__":
    urls = ['https://one-piece.com/news/category.html?cc=71',]
    op_crawler = OnePieceCrawler(urls, BS_Parser)
    ps = op_crawler.activate()
    p = ps.find_all_tag('p')
    logger.info(p)