# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from utils.proxyModel import Proxy
from db.spcDB import RedisDB
from utils.logHandler import logHandler
from spider.spcCrawl import *
from verify.verifyProxy import verifyProxy
from utils.logHandler import logHandler

if "__main__" == __name__:
    db = RedisDB("ProxyPool")
    logger = logHandler("test")
    spiders = [XiciCrawl(), XilaCrawl(), NimaCrawl()]
    for spi in spiders:
        spi.cocurrent = False
        spi.run()
        logger.info("one task been done")

    for spi in spiders:
        for p in spi.proxyLs:
            if not db.exists(p.host) and verifyProxy(p):
                db.put(p)
