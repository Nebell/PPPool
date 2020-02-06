# -*- coding: utf-8 -*-
"""
spcCrawl.py
各种特定网站的爬虫
"""
from threading import Thread
from queue import Queue
from time import sleep

from spider.Crawl import Crawl
from utils.webRequest import webRequest
from utils.proxyModel import Proxy
from parse.parserBasic import XpathParser

class XiciCrawl(Crawl):
# 西刺代理
	def __init__(self, **kwargs):
		self.name = "XiciProxy"
		super(XiciCrawl, self).__init__(name=self.name, **kwargs)

	def _genUrl(self):
		types = ["nn", "nt", "wn", "wt", "qq"]
		urlBasic = ["https://www.xicidaili.com/" + x + "/" for x in types]
		taskUrls = list()
		for i in range(1, self.pages+1):
			for url in urlBasic:
				taskUrls.append(url + str(i) + "/")
		
		return taskUrls

	def _pageParse(self, html):
		try:
			xpParser = XpathParser(html, ".//table[@id='ip_list']/tr")
		except:
			pass
		
		for trElem in xpParser.rawResultls[1:]:
			try:
				if trElem[1].text:
					proxy = Proxy(trElem[1].text, trElem[2].text, trElem[5].text.replace("QQ", "socks"), trElem[4].text)
					# 如果存在数据库则储存在数据库里
					self.db.put(proxy) if self.db else self.proxyLs.append(proxy)
			except IndexError:
				pass
	

class NimaCrawl(Crawl):
# 泥马ip代理
	def __init__(self, **kwargs):
		self.name = "NimaProxy"
		super(NimaCrawl, self).__init__(name=self.name, threads=3, **kwargs)

	# e.g. http://www.nimadaili.com/http/2
	def _genUrl(self):
		# 二级目录
		types = ["gaoni", "http", "https"]
		urlBasic = ["http://www.nimadaili.com/" + x + "/" for x in types]
		taskUrls = list()
		for i in range(1, self.pages+1):
			for url in urlBasic:
				taskUrls.append(url + str(i) + "/")
		
		return taskUrls

	def _pageParse(self, html):
		xpParser = XpathParser(html, ".//tr")
		for trElem in xpParser.rawResultls:
			try:
				proxy = Proxy(trElem[0].text.split(':')[0], 
					trElem[0].text.split(':')[1], trElem[1].text, trElem[2].text,
					trElem[3].text)
				self.db.put(proxy) if self.db else self.proxyLs.append(proxy)
			except IndexError:
				pass


class XilaCrawl(Crawl):

	def __init__(self, **kwargs):
		self.name = "XilaProxy"
		super(XilaCrawl, self).__init__(name=self.name, **kwargs)
		

	def _genUrl(self):
		# 二级目录
		types = ["gaoni", "http", "https", "putong"]
		urlBasic = ["http://www.xiladaili.com/" + x + "/" for x in types]
		taskUrls = list()
		for i in range(1, self.pages+1):
			for url in urlBasic:
				taskUrls.append(url + str(i) + "/")
		
		return taskUrls

	def _pageParse(self, html):
		xpParser = XpathParser(html, ".//table[@class='fl-table']//tr")
		for trElem in xpParser.rawResultls:
			try:
				proxy = Proxy(trElem[0].text.split(':')[0], 
					trElem[0].text.split(':')[1], trElem[1].text, trElem[2].text,
					trElem[3].text)
				self.db.put(proxy) if self.db else self.proxyLs.append(proxy)
			except IndexError:
				pass
