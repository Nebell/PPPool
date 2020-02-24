import os
from utils.manager import Manager
from spider.spcCrawl import XiciCrawl, XilaCrawl, NimaCrawl
from verify.judger import Judger
from db.spcDB import RedisDB

if "__main__" == __name__:
    # db = RedisDB("test")
    spiders = [XiciCrawl(), XilaCrawl(), NimaCrawl()]
    for spi in spiders:
        spi.cocurrent = True
    #     if not spi.db:
    #         spi.db = db
        # spi.run()
        # print(spi.proxyLs)
    # Judger().run()
    manager = Manager()
    manager.run()
    
