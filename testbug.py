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
        r = requests.get(url)
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

