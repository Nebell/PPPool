# -*- coding: utf-8 -*-
"""
utilsBasic.py
各种简易函数
"""

import random
from utils.utilsVar import UserAgent, Headers

def lazyProperty(func):
	attrName = "_lazy_" + func.__name__

	@property
	def _lazyProperty(self):
		if not hasattr(self, attrName):
			setattr(self, attrName, func(self))
		return getattr(self, attrName)
	
	return _lazyProperty

def getUserAgent():
	return random.choice(UserAgent)

def getHeader():
	header = Headers
	header.update({"User-Agent":random.choice(UserAgent)})
	return header