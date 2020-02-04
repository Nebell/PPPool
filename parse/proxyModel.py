# -*- coding: utf-8 -*-
"""
proxyModel.py
代理服务器模型
"""

# 简陋，Todo:@property 最后一次检验时间
class Proxy(object):
    def __init__(self, host : str, port : str, protocol : str, level ="",
            region=""):
        self.host = host
        self.port = port
        self.region = region
        self.level = level
        self.protocol = protocol

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        if "socks" in value or "SOCKS" in value:
            self._protocol = "socks5"
        elif "https" in value or "HTTPS" in value:
            self._protocol = "https"
        elif "http" in value or "HTTP" in value:
            self._protocol = "http"
        else:
            self._protocol = "unknown"

    def __str__(self):
        return "%s %s %s %s %s" % (self.host, self.port, self.protocol, 
            self.region, self.level)

    def __repr__(self):
        return "%s://%s:%s" % (self.protocol, self.host, self.port)
