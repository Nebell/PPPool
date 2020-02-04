# -*- coding: utf-8 -*-
"""
verifyProxy.py
包含验证Proxy以及IP的函数
"""

import re
import os, sys
import requests

from parse.proxyModel import Proxy

def verifyProxy(proxy : Proxy, url : str = "http://www.baidu.com/", timeout = 2):
    try:
        proxies = {
            "http" : proxy.protocol + "://" + ":".join([proxy.host, proxy.port]),
            "https": proxy.protocol + "://" + ":".join([proxy.host, proxy.port])
        }
        resp = requests.get(url, proxies=proxies, timeout=timeout)
        return True if 200 == resp.status_code else False
    except Exception:
        return False
    

def verifyIP(ip : str):
    if ":" in ip:
        return True if re.match(R"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$", ip) else False
    else:
        return True if re.match(R"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip) else False

# if "__main__" == __name__:
#     from spider.spcCrawl import NimaCrawl
#     nm = NimaCrawl()
#     nm.run()
#     verifiedls = []
#     for p in nm.proxyLs:
#         if verifyProxy(p):
#             verifiedls.append(p)
#             print(p)
