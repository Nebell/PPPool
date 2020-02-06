# -*- coding: utf-8 -*-
"""
verifyProxy.py
包含验证Proxy以及IP的函数
"""

import re
import time
import os, sys
import requests

from utils.proxyModel import Proxy

def verifyProxy(proxy : Proxy, url : str = "http://www.baidu.com/", timeout = 1):
    if not url:
        url = "http://www.baidu.com/"
    try:
        # 设定代理
        proxies = {
            "http" : proxy.protocol + "://" + ":".join([proxy.host, proxy.port]),
            "https": proxy.protocol + "://" + ":".join([proxy.host, proxy.port])
        }
        resp = requests.get(url, proxies=proxies, timeout=timeout)
        proxy.last_verified_time = time.asctime()

        # 代理可用则修改状态 不可用一律报错
        if 200 == resp.status_code and resp.text:
            proxy.status = "available"
            return True
        else:
            raise BaseException("unavailable")
    except (Exception, BaseException):
        proxy.status = "unavailable"
        proxy.fail_count += 1
        return False
    

def verifyIP(ip : str, critical=False):
    # 不严格形式允许后置端口号
    if ":" in ip and not critical:
        return True if re.match(R"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$", ip) else False
    else:
        return True if re.match(R"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip) else False

