# -*- coding: utf-8 -*-
"""
logHandler.py
记录模块
"""

import os
import logging
import shutil
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

LOGFILEPATH = os.path.join(os.path.dirname(os.getcwd()), "log")

if not os.path.exists(LOGFILEPATH):
    os.mkdir(LOGFILEPATH)

# Log Level

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

class logHandler(Logger):
    def __init__(self, name : str, level=DEBUG, file=True, stream=True):
        self.name = name
        self.level = level
        # self.logFormatter = logging.Formatter("%T %(filename)s:%(lineno)d %(levelname)s %(message)s")
        self.logFormatter = logging.Formatter("%(asctime)s %(name)s %(message)s", "%T")
        super(logHandler, self).__init__(name, level)
        if stream:
            self.__setStreamHandle()
        if file:
            self.__setFileHandler()

    def __setFileHandler(self, level=None):
        if not level:
            level = self.level
        
        fileName = os.path.join(LOGFILEPATH, "{name}.log".format(name=self.name))
        fileHandler = TimedRotatingFileHandler(filename=fileName, when='D', interval=1, backupCount=5)
        fileHandler.setLevel(level)
        fileHandler.setFormatter(self.logFormatter)
        self.__fileHandler = fileHandler
        self.addHandler(fileHandler)

    def __setStreamHandle(self, level=None):
        if not level:
            level = self.level

        streamHandle = logging.StreamHandler()
        streamHandle.setLevel(level)
        streamHandle.setFormatter(self.logFormatter)
        self.addHandler(streamHandle)

    @staticmethod
    def flashFiles(filepath=LOGFILEPATH):
        if os.path.exists(filepath):
            shutil.rmtree(filepath)
            os.mkdir(filepath)