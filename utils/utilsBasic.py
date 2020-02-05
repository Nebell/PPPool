# -*- coding: utf-8 -*-
"""
utilsBasic.py
各种简易函数
"""

import random
from copy import deepcopy
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
	# 若无deepcopy会污染utilsVar.py中的变量(Python默认传递引用)
	header = deepcopy(Headers)
	header.update({"User-Agent":random.choice(UserAgent)})
	return header