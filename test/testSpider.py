import os, sys

sys.path.append("../")
from spider.Crawl import Crawl
from spider.spcCrawl import NimaCrawl, XiciCrawl, XilaCrawl
from utils.webRequest import webRequest
from utils.proxyModel import Proxy
from parse.parserBasic import Parser, XpathParser, RegexParser
from threading import Thread

def spide(spiders:list):
    for spi in spiders:
        spi.cocurrent = True
        spi.run()
        print(len(spi.proxyLs))
        for p in spi.proxyLs:
            print(p)

if "__main__" == __name__:

    spide([XilaCrawl(), NimaCrawl(), XiciCrawl()])    
    