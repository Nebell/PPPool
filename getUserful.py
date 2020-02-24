# -*- coding: utf-8 -*-

from db.spcDB import RedisDB
from utils.proxyModel import Proxy

if "__main__" == __name__:
    db = RedisDB("ProxyPool")
    for proxy in db.getAll():
        if proxy.status == "available":
            print(proxy)