# -*- coding: utf-8 -*-
"""
webRequst.py
网页获取
"""

import os, sys
import requests
from time import sleep
from urllib.parse import urlparse
from random import random

from utils.utilsBasic import getUserAgent, getHeader

class webRequest(object):
	def __init__(self, url=""):
		self.url = url
	
	def get(self, url="", header=None, timeout=3, retry_time=3,
			retry_interval=2, *args, **kwargs):
		if not url:
			url = self.url

		if 0 > retry_time:
			retry_time = 0

		# 如果形参header也是dict类型并且存在 将其信息加入headers
		headers = getHeader()
		# 不清楚为何加入下句容易崩溃
		headers.update({"Host" : urlparse(url).netloc})
		if header and isinstance(header, dict):
			headers.update(header)

		while True:
			try:
				response = requests.get(url, headers=headers, timeout=timeout, *args, **kwargs)

				# 有可能出现状态码为 200 的空网页的情况
				if 200 == response.status_code and response.text:
					self.html = response.text
					return self.html
				else:
					raise ConnectionError(response.status_code)

			except Exception:
				retry_time -= 1
				if 0 >= retry_time:
					return str("")
				sleep(retry_interval)