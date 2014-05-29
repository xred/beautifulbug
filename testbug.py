#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf8')
import requests
from pyquery import PyQuery as pq


def beautifulBug(url,selector):
    try:
        r = requests.get(url)
        d = pq(r.content)
        info = d(selector)
        return info.text()
    except Exception, e:
        return "error"