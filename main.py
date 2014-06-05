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
import os
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
            rule_obj['info'] = 'Loading'
            result_obj = rule_obj
            resut_array.append(result_obj)
        self.render("./template/index.htm",items = resut_array)

class AddHandler(tornado.web.RequestHandler):
    def get(self,add_info):
        self.render("./template/add.htm")
    def post(self,add_info):
        name = self.get_argument('name')
        url = self.get_argument('url')
        selector = self.get_argument('selector')
        cookie = self.get_argument('cookie')
        result = store.add_rule( name, url, selector, cookie)
        self.write(result)
        
class RemoveHandler(tornado.web.RequestHandler):
    def get(self,remove_info):
        self.render("./template/remove.htm",remove_info=remove_info)
    def post(self,remove_info):
        name = self.get_argument("name")
        result = store.delete_rule(name)
        self.write(result)

class APIHandler(tornado.web.RequestHandler):
    def get(self,api_info):
        result = read_info(api_info)
        self.write(result)

def read_info(api_info):
    rule_obj = store.get_rule(api_info)
    name = rule_obj['name']
    selector = rule_obj['selector']
    url = rule_obj['url']
    if "cookie" in rule_obj:
        cookie = rule_obj['cookie']
    else:
        cookie = "";
    result_obj = testbug.beautifulBug(  url, selector, name,cookie)
    print result_obj
    return result_obj['info']

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "statics"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/add/(.*)",AddHandler),
    (r"/remove/(.*)",RemoveHandler),
    (r"/api/(.*)",APIHandler),
    (r"/statics/(.*)",tornado.web.StaticFileHandler, dict(path=settings['static_path']))
],**settings)

if __name__ == '__main__':
    print "listen 1992 port"
    application.listen(1992)
    tornado.ioloop.IOLoop.instance().start()