# -*- coding: utf-8 -*-

from redis.connection import BlockingConnectionPool
from db.dbClient import DB
from utils.proxyModel import Proxy
from redis import Redis

class RedisDB(DB):
    def __init__(self, name, config:dict=""):
        if not config:
            self.__config = {
                "host" : "127.0.0.1",
                "port" : "6379"
            }

        # 表名
        self.__name = name

        # connection_pool=BlockingConnectionPool() 阻塞，线程安全
        # decode_responses=True 放入和取出都以字符串形式，为False则为Bytes形式
        self.__db = Redis(connection_pool=BlockingConnectionPool(), decode_responses=True)

    def get(self, proxy_host : str):
    # 从集合中获取Proxy
        info_json = self.__db.hget(self.__name, proxy_host)
        proxy = Proxy.genFromJson(info_json)
        return proxy

    def put(self, proxy : Proxy):
        return self.__db.hset(self.__name, proxy.host, proxy.json)

    def update(self, proxy : Proxy):
        return self.__db.hset(self.__name, proxy.host, proxy.json)

    def delete(self, proxy_host : str):
        self.__db.hdel(self.__name, proxy_host)
    
    def exists(self, proxy_host : str):
        return self.__db.hexists(self.__name, proxy_host)

    def pop(self, **kwargs):
        return None

    def getAll(self):
        itemDict = self.__db.hgetall(self.__name)
        return [Proxy.genFromJson(itemDict[key]) for key in itemDict]

    def clear(self):
        self.__db.delete(self.__name)

    def changeTable(self, name):
        self.__name = name

    def getNumber(self):
        return self.__db.hlen(self.__name)
    