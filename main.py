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
            if "cookie" in rule_obj:
                cookie = rule_obj['cookie']
            else:
                cookie = "";
            result_obj = testbug.beautifulBug(  url, selector, name,cookie)
            resut_array.append(result_obj)
        self.render("./template/index.htm",items = resut_array)

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./template/add.htm")
    def post(self):
        name = self.get_argument('name')
        url = self.get_argument('url')
        selector = self.get_argument('selector')
        cookie = self.get_argument('cookie')
        result = store.add_rule( name, url, selector, cookie)
        self.write(result)
        
class RemoveHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./template/remove.htm")
    def post(self):
        name = self.get_argument("name")
        result = store.delete_rule(name)
        self.write(result)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/add/*",AddHandler),
    (r"/remove/*",RemoveHandler),
])

if __name__ == '__main__':
    print "listen 1992 port"
    application.listen(1992)
    tornado.ioloop.IOLoop.instance().start()