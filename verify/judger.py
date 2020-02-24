# -*- coding: utf-8 -*-
"""
judger.py
多线程测试代理是否可用
"""

from threading import Thread, BoundedSemaphore
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, wait
from verify.verifyProxy import verifyIP, verifyProxy
from utils.proxyModel import Proxy
from db.dbClient import DB

class Judger(object):
    """
    多线程判断代理服务器是否可用，如果设置了数据库，则优先使用数据库
    """

    def __init__(self, testurl="", threads=5, db:DB=None, timeout=1):
        self.proxylist = list()
        self.verifiedlist = list()
        self.timeout = timeout
        self.db = db
        self.semalock = BoundedSemaphore(threads)
        self.__threads = threads
        self.testurl = "https://www.baidu.com/" if not testurl else testurl

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        self.__timeout = value if 0 <= value else 0

    def task(self, proxy : Proxy):
        # self.semalock.acquire()
        # 检测并更新爬虫
        verifyProxy(proxy, url=self.testurl, timeout=self.timeout)
        self.db.update(proxy) if self.db else self.verifiedlist.append(proxy)
        # self.semalock.release()

    def run(self): 
        # taskls = list()
        # for proxy in self.db.getAll() if self.db else self.proxylist:
        #     taskls.append(Thread(target=self.task, args=(proxy,)))
        
        # for t in taskls:
        #     t.start()
        #     t.join()

        proxyls = self.db.getAll() if self.db else self.proxylist
        with ThreadPoolExecutor(max_workers=self.__threads) as exeJudge:
            jdgfurture = [exeJudge.submit(self.task, (proxy)) for proxy in proxyls]
            wait(jdgfurture, return_when=ALL_COMPLETED)