# -*- coding: utf-8 -*-
"""
proxyModel.py
代理服务器模型
"""

import json

# 简陋，Todo:@property 最后一次检验时间
class Proxy(object):
    def __init__(self, host : str, port : str, protocol : str, level ="",
            region=""):
        self.host = host
        self.port = port
        self.region = region
        self.level = level
        self.protocol = protocol
        self.status = "untested"
        self.last_verified_time = "/"
        self.fail_count = 0

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, value):
    # 验证协议
        if "socks" in value or "SOCKS" in value:
            self.__protocol = "socks5"
        elif "https" in value or "HTTPS" in value:
            self.__protocol = "https"
        elif "http" in value or "HTTP" in value:
            self.__protocol = "http"
        else:
            self.__protocol = "unknown"

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if U"透明" in value or "Transparent" in value:
            self.__level = "Transparent"
        elif U"高匿" in value or U"高级" in value or "High" in value:
            self.__level = "High"
        else:
            self.__level = "Common"

    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, value):
        if not value:
            self.__region = "Unknown"
        else:
            self.__region = value.replace(' ', "")

    @property
    def info(self):
        return  "%s %s %s %s %s %d" % (self.__str__(), 
            self.level, self.region, self.status, self.last_verified_time, self.fail_count)
    
    @info.setter
    def info(self, value : str):
        infols = value.split(' ')
        try:
            self.level = infols[0]
            self.region = infols[1]
            self.status = infols[2]
            self.last_verified_time = infols[3]
            self.fail_count = int(infols[4])
        except Exception:
            pass

    @property
    def json(self):
        return json.dumps({
            "host":self.host,
            "port":self.port,
            "protocol":self.protocol,
            "level":self.level,
            "region":self.region,
            "status":self.status,
            "last_verified_time" : self.last_verified_time,
            "fail_count" : self.fail_count
        })

    @staticmethod
    def genFromStr(proxystr:str):
        strls = proxystr.split(' ')
        try:
            return Proxy(strls[0], strls[1], strls[2])
        except Exception:
            return None

    @staticmethod
    def genFromJson(jsonObj):
        try:
            proxyDict = json.loads(jsonObj)
            proxy = Proxy.genFromStr(" ".join([proxyDict["host"], proxyDict["port"], proxyDict["protocol"]]))
            proxy.info = (" ".join([proxyDict.get("level"), 
                        proxyDict.get("region", "None"), 
                        proxyDict.get("status", "untested"),
                        proxyDict.get("last_verified_time", "/"), 
                        str(proxyDict.get("fail_count", 0))]))
            return proxy
        except Exception:
            return None


    def __str__(self):
        # return "%s://%s:%s" % (self.protocol, self.host, self.port)
        return "%s %s %s" % (self.host, self.port, self.protocol)

    def __repr__(self):
        return "%s://%s:%s" % (self.protocol, self.host, self.port)