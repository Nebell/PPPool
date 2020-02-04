# -*- coding: utf-8 -*-
"""
spcCrawl.py
辣鸡爬虫模型
"""
from threading import Thread
from queue import Queue
from time import sleep

from spider.Crawl import Crawl
from utils.webRequest import webRequest
from parse.proxyModel import Proxy
from parse.parserBasic import Parser, XpathParser, RegexParser
from verify.verifyProxy import verifyProxy

class XiciCrawl(Crawl):
# 西刺代理

	def _genUrl(self, pages=2):
		types = ["nn", "nt", "wn", "wt", "qq"]
		urlBasic = ["https://www.xicidaili.com/" + x + "/" for x in types]
		taskUrls = list()
		for i in range(1, pages+1):
			for url in urlBasic:
				taskUrls.append(url + str(i) + "/")
		
		return taskUrls

	def _pageParse(self, html):
		try:
			xpParser = XpathParser(html, ".//table[@id='ip_list']/tr")
		except Exception as e:
			print(e)
			return
		
		for trElem in xpParser.rawResultls[1:]:
			try:
				if trElem[1].text:
					self.proxyLs.append(Proxy(trElem[1].text, trElem[2].text, 
						trElem[5].text.replace("QQ", "socks"), trElem[4].text))
			except IndexError:
				pass
	

class NimaCrawl(Crawl):
# 泥马ip代理

	# e.g. http://www.nimadaili.com/http/2
	def _genUrl(self, pages=5):
		# 二级目录
		types = ["gaoni", "http", "https"]
		urlBasic = ["http://www.nimadaili.com/" + x + "/" for x in types]
		taskUrls = list()
		for i in range(1, pages+1):
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
				self.proxyLs.append(proxy)
			except IndexError:
				pass