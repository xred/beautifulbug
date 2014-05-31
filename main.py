#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf8')

import tornado.ioloop
import tornado.web
import tornado.autoreload
import store
import json
import testbug


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        rule_name = ""
        resut_array = list()
        rules_list = store.list_rules()
        for rule in rules_list:
            rule_obj = store.read_rule(rule)
            name = rule_obj['name']
            selector = rule_obj['selector']
            url = rule_obj['url']
            result_obj = testbug.beautifulBug(  url, selector, name)
            resut_array.append(result_obj)
        self.render("./template/index.htm",items = resut_array)


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == '__main__':
    print "listen 1992 port"
    application.listen(1992)
    tornado.ioloop.IOLoop.instance().start()