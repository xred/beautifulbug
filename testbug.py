#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf8')
import requests
from pyquery import PyQuery as pq


def beautifulBug(url,selector,name):
    result = dict();
    try:
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36',
            'Pragma':'no-cache',
            'Cookie':'__cfduid=d89d38faf312501122304036416165dee1395979292408; __utma=264820115.202194311.1395979293.1399386482.1399535755.25; __utmz=264820115.1395979293.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); session_id=dkngoiv0njhbsts4ao7mkbh0i7; visid_incap_152969=x4nEeWfATBiAaxIVJhRoktyJiFMAAAAAQUIPAAAAAAAkzhq+qaIvmKasjRKukbQr; MintPal=thc7r66ugdd97r8i6a8gfu3763; visid_incap_152968=W5SOr0tcS+e5Uy2+xCsSSSz1flMAAAAAQUIPAAAAAABcrHXjSntyYOgd2SeyiWvE; incap_ses_200_152968=bWqHBoLpUAAZQZWqE4vGAqeriVMAAAAAPL3Tg4aeJLWyUQ0v3y6o+w=='
        }
        r = requests.get(url,headers=headers)
        d = pq(r.content)
        info = d(selector)
        info = info.text()
        if info == "":
            info = "error"
        result['name'] = name
        result['url'] = url
        result['selector'] = selector
        result['info']  = info
        return result
    except Exception, e:
        return "error"

