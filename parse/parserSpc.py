# -*- coding: utf-8 -*-
"""
parserSpc.py
特定实例解析器 Special Parser
-------------------------------------------------------------------
原打算Getter/Parser模块化拼凑爬取，但网站常常又是一起的
本模块已经弃用，并入爬虫模块中
"""

from parse.parserBasic import Parser, XpathParser, RegexParser
from parse.proxyModel import Proxy

class XiciParser(XpathParser):
    def __init__(self, html):
        super(XiciParser, self).__init__(html, ".//tr/td")

    def genProxy(self, rawls):
        for i in range(1, len(rawls), 8):
            try:
                if rawls[i:i+7]:
                    # print(rawls[i:i+7])
                    yield Proxy(rawls[i], rawls[i+1], rawls[i+4])
            except IndexError:
                pass

    def parse(self):
        rawls = super(XiciParser, self).parse()
        self.result = [i for i in self.genProxy(rawls)]
        return self.result
