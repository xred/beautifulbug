#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf8')
import requests
from pyquery import PyQuery as pq


def beautifulBug(url,selector,name,cookie):
    result = dict();
    try:
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36',
            'Pragma':'no-cache'
        }
        if cookie != "":
            headers['cookie'] = cookie
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

