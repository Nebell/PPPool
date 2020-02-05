# -*- coding: utf-8 -*-
"""
parserBasic.py
职业解析网页
"""

import re
from lxml import etree
from utils.utilsBasic import lazyProperty
from utils.logHandler import logHandler

class Parser(object):
	def __init__(self, html):
		self.html = html
		self.logger = logHandler("Parse")

	def parse(self):
		pass

	@lazyProperty
	def rawResultls(self):
		self.parse()

# Xpath解析 (html, xpath) 返回值：对应字符的列表
class XpathParser(Parser):
	def __init__(self, html, xpath):
		super(XpathParser ,self).__init__(html)
		self.xpath = xpath
		self.textResultls = list()

	@lazyProperty
	def rawResultls(self):
	# 获取按Xpath法则匹配的原始列表
		try:
			rawls = etree.HTML(self.html).xpath(self.xpath)
		except Exception as e:
			self.logger.error(e, self.xpath)
			return list()
		return rawls

	def parse(self):
		try:
			if not self.html or not self.rawResultls:
				return list()

			# 转换成文本
			for i in self.rawResultls:
				self.textResultls.append(i.text)
			return self.textResultls
		except Exception as e:
			self.logger.error(e)
			return list()

class RegexParser(Parser):
	def __init__(self, html, regex):
		super(RegexParser, self).__init__(html)
		self.__regex = regex