# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from utils.proxyModel import Proxy
from db.spcDB import RedisDB
from utils.logHandler import logHandler
from spider.spcCrawl import *
from verify.verifyProxy import verifyProxy
from utils.logHandler import logHandler
from verify.judger import Judger

db = RedisDB("ProxyPool")
Adb = RedisDB("ProxyAva")
logger = logHandler("test")

def testSpider():
    spiders = [XiciCrawl(db=db), XilaCrawl(db=db), NimaCrawl(db=db)]
    for spi in spiders:
        spi.run()
        logger.info("{name} has BALA".format(name=spi.name))

    for spi in spiders:
        for p in spi.proxyLs:
            if not db.exists(p.host):
                db.put(p)

if "__main__" == __name__:
    J = Judger(threads=10, timeout=0.3)
    if db.getNumber() <= 0:
        testSpider()
    
    J.proxylist = db.getAll()
    J.run()
    Adb.clear()
    for proxy in J.verifiedlist:
        logger.info("verified {proxy}".format(proxy=str(proxy)))
        db.update(proxy)
        if "available" ==  proxy.status:
            Adb.put(proxy)
