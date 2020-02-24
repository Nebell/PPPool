# -*- coding: utf-8 -*-
"""
manager.py
管理任务的进行，定期爬取和检验
"""

import time
from apscheduler.schedulers.blocking import BlockingScheduler

from utils.proxyModel import Proxy
from utils.logHandler import logHandler
from spider.spcCrawl import *
from db.spcDB import RedisDB
from verify.judger import Judger

class Manager(object):
    """
    管理模块，定期爬取和检验
    """
    def __init__(self, dbname : str = "ProxyPool", spiders=list()):
        self.__db = RedisDB(dbname)
        self.__schd = BlockingScheduler()
        self.__judger = Judger(threads=10, db=self.__db)
        self.__logger = logHandler("Manager")

        # 是否在爬取的标识符
        self.__Getting = False

        # 将没有数据库的爬虫的数据库设置成自己的
        if not spiders:
            spiders = [
                XiciCrawl(db=self.__db), 
                XilaCrawl(db=self.__db), 
                NimaCrawl(db=self.__db)]
        else:
            for spi in spiders:
                if not spi.db:
                    spi.db = self.__db
        
        self.spiders = spiders

    def getProxies(self):
        if not self.__Getting:
            self.__Getting = True
        else: return
        self.__logger.info("Start to Get Proxies")
        for spi in self.spiders:
            spi.run()
        self.__Getting = False

    def checkProxies(self):
        # 在爬取的时候加把锁

        self.__logger.info("Start to Check Proxies")
        self.__judger.run()

    def clearPool(self):
    # 清空池
        self.__db.clear()

    def clearUnavailable(self, times=5):
    # 清理五次检验后仍不能用的
        for proxy in self.__db.getAll():
            if proxy.fail_count > times:
                self.__db.delete(proxy.host)

    def run(self):
        self.getProxies()
        self.__schd.add_job(self.getProxies, "interval", seconds=600)
        self.__schd.add_job(self.checkProxies, "interval", seconds=300)
        self.__schd.start()

        