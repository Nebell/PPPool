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

class Crawl(object):

	def __init__(self, threads=5):
		# self.html = str()
		self.proxyLs = list()
		# self.htmlQue = Queue() # 若解析线程和获取网页线程分离
		# self.threadTimeout = 5
		# 默认5个线程
		self.downloadSema = threading.BoundedSemaphore(threads)

	def _genUrl(self):
	# 生成要爬的URL
		return []

	def _pageParse(self, html):
	# 网页解析
		pass

	def _getWeb(self, url):
	# 获取要代理网页的源代码
		webReq = webRequest()
		# 加锁，如果get出错会导致下面锁一直解不开
		self.downloadSema.acquire()
		html = webReq.get(url=url)
		self.downloadSema.release()
		return html
		# if html:	# 若解析/获取线程量相等，则有部分解析线程无法获取数据
		# 	self.htmlQue.put(html)

	def task(self, url):
	# 每个要做的任务
		# 太快会导致有些网页获取不了 随机延时零点几秒
		sleep(random())
		html = self._getWeb(url)
		if html:
			self._pageParse(html)

	def run(self):
	# 开启爬取线程
		taskls = list()
		for url in self._genUrl():
			taskls.append(Thread(target=self.task, args=(url,)))
		for task in taskls:
			task.start()
		for task in taskls:
			task.join()

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