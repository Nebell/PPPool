# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from db.spcDB import RedisDB
from utils.proxyModel import Proxy

if "__main__" == __name__:
    db = RedisDB("test")
    p = Proxy.genFromStr("127.0.0.1 1080 SOCKS5")
    p.level = "High"
    p.region = "China"

    db.put(p)
    p2 = db.get(p.host)
    db.clear()
    print(db.exists(p.host))
