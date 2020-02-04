import os
from utils.webRequest import webRequest
from parse.parserBasic import XpathParser

if "__main__" == __name__:
    wr = webRequest("https://www.xicidaili.com/nn")
    html = wr.get()
    if html:
        xp = XpathParser(html, ".//tr")
    
