import os, sys

sys.path.append("../")
from spider.Crawl import Crawl
from spider.spcCrawl import NimaCrawl, XiciCrawl
from utils.webRequest import webRequest
from parse.proxyModel import Proxy
from parse.parserBasic import Parser, XpathParser, RegexParser
from threading import Thread

def testNimaCrawl():
    nm = NimaCrawl()
    nm.run()
    print(nm.proxyLs)

def testXiciCrawl():
    xc = XiciCrawl()
    xc.run()
    print(xc.proxyLs)

def spide(spiders:list):
    for spi in spiders:
        # t = Thread(target=spi.run)
        # t.start()
        # t.join()
        spi.run()
        print(len(spi.proxyLs))
        for i in spi.proxyLs:
            if "socks5" == i.protocol:
                print(i)
    # for spi in spiders:
    #     print(len(spi.proxyLs))

if "__main__" == __name__:

    spide([NimaCrawl()])

    # testXiciCrawl()
    # wr = webRequest("https://www.xicidaili.com/nn")
    # html = wr.get()
    # xp = XpathParser(html, ".//table[@id='ip_list']/tr")
    # for trElem in xp.rawResultls[1:]:
    #     try:
    #         if trElem[1].text:
    #             print(trElem[1].text, trElem[2].text, trElem[5].text, trElem[4].text)
    #     except IndexError:
    #         pass
    # print(xp.rawResultls[1][2].text)

    
    