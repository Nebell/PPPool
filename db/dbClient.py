# -*- coding: utf-8 -*-

class DB(object):
    def __init__(self, name, config : dict =""):
        pass

    @property
    def config(self):
        return self.__config
    
    @config.setter
    def config(self, value:dict):
        
        if value["port"].isdigit():
            self.__config = None
        else:
            self.__config = value
    
    def get(self, proxy_str):
        pass

    def put(self, proxy):
        pass
    
    def update(self):
        pass

    def delete(self, proxy_str):
        pass

    def pop(self, **kwargs):
        pass

    def getAll(self):
        pass

    def clear(self):
        pass

    def changeTable(self, name):
        pass

    def getNumber(self):
        pass