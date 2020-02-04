import sys

sys.path.append("../")
from utils.webRequest import webRequest
from parse.parserBasic import Parser, XpathParser
from parse.parserSpc import XiciParser

def ps(parser : Parser):
    return parser.parse()

if "__main__" == __name__:
    wr = webRequest()
    html = wr.get("https://www.xicidaili.com/nn")
    # xp = XpathParser(html, './/tr/td')
    xc = XiciParser(html)
    # for p in xc.parse():
    #     print(p)

    # print(xc.parse())
    print(ps(xc))