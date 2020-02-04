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
		self.status_code = 0
	
	def get(self, url="", header=None, retry_time=3, timeout=3,
			retry_interval=2, *args, **kwargs):
		if not url:
			url = self.url

		if 0 > retry_time:
			retry_time = 0

		# 如果形参header也是dict类型并且存在 将其信息加入headers
		headers = getHeader()
		headers.update({"Host" : urlparse(url).netloc})
		if header and isinstance(header, dict):
			headers.update(header)

		while True:
			try:
				response = requests.get(url, headers=headers, timeout=timeout, *args, **kwargs)

				# 有可能出现状态码为 200 的空网页的情况
				if 200 == response.status_code and response.text:
					self.html = response.text
					self.status_code = response.status_code
					return self.html
				else:
					raise ConnectionError(response.status_code)

			except Exception as e:
				print(url, str(e))
				retry_time -= 1
				if 0 >= retry_time:
					print("Fail to get", url)
					return str("")
				sleep(retry_interval)