# -*- coding: utf-8 -*-
"""
Crawl.py
辣鸡爬虫模型
"""
import threading
from queue import Queue
from threading import Thread
from random import random
from time import sleep

from utils.webRequest import webRequest
from utils.logHandler import logHandler
from db.dbClient import DB

class Crawl(object):

	def __init__(self, name="", cocurrent=False, threads=3, db:DB=None, retryTimes=2, pages=3):
		self.name = "Crawl Model" if not name else name
		self.logger = logHandler("Crawl")
		self.db = db
		self.proxyLs = list()
		self.reqRetryTimes = retryTimes
		# 是否启动多线程
		self.cocurrent = cocurrent
		# 每个副栏爬取多少页
		self.pages = pages
		self.downloadSema = threading.BoundedSemaphore(threads)

		if not db:
			self.logger.warning("{name} is running without db!".format(name=self.name))

	def setThreads(self, threads : int):
		self.downloadSema = threading.BoundedSemaphore(threads)

	def _genUrl(self):
	# 生成要爬的URL
		return []

	def _pageParse(self, html):
	# 网页解析
		pass

	def _getWeb(self, url, **kwargs):
	# 获取要代理网页的源代码
		webReq = webRequest()
		
		if self.cocurrent:
			# 加锁，如果get出错会导致下面锁一直解不开
			self.downloadSema.acquire()
			html = webReq.get(url=url, **kwargs)
			self.downloadSema.release()
		else:
			html = webReq.get(url=url, **kwargs)
		return html
		# if html:	# 若解析/获取线程量相等，则有部分解析线程无法获取数据
		# 	self.htmlQue.put(html)

	def task(self, url):
	# 每个要做的任务
		# 太快会导致有些网页获取不了 随机延时零点几秒
		# sleep(random())
		try:
			html = self._getWeb(url)
			if html:
				self._pageParse(html)
			else:
				self.logger.warning("Failed to get %s" % url)
		except Exception as e:
			self.logger.warning("{url} {exception}".format(url=url, exception=str(e)))

	def run(self):
	# 开启爬取线程
		taskls = list()
		if self.cocurrent:
			for url in self._genUrl():
				taskls.append(Thread(target=self.task, args=(url,)))
			for task in taskls:
				task.start()
			for task in taskls:
				task.join()
		else:
			for url in self._genUrl():
				self.task(url)

"""
	def run(self):
		# downloadTaskLs = list()
		# parseTaskLs = list()
		# for url in self._genUrl():
		# 	downloadTaskLs.append(Thread(target=self._getWeb, args=(url,)))
		# 	parseTaskLs.append(Thread(target=self._pageParse))
		# for downloadTask in downloadTaskLs:
		# 	downloadTask.start()
		# for parseTask in parseTaskLs:
		# 	parseTask.start()
		# 	parseTask.join()


若解析网页线程和获取网页线程分离，使用htmlQue队列进行通讯
则有可能获取网页失败，相同量的解析网页线程和获取网页线程时，
htmlQue.get()则可能一直阻塞

故而将解析及获取网页放入同一个线程中，根据获取情况决定是否解析
"""